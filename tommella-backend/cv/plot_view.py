import pandas as pd
from plotly.subplots import make_subplots

import plotly.graph_objects as go
from django.http import HttpResponse, HttpResponseNotAllowed
from django.templatetags.static import static
from .models import Experience, Education

def min_max_scale(ranking, min_val=0.6, max_val=1.4):
    """Scale the ranking to the range [min_val, max_val]."""
    min_ranking = ranking.min()
    max_ranking = ranking.max()
    scaled_ranking = (ranking - min_ranking) / (max_ranking - min_ranking)
    return scaled_ranking * (max_val - min_val) + min_val

def generate_plot(request):
    if request.method == 'GET':
        # Fetch data from Django models
        experiences_queryset = Experience.objects.all().order_by("ranking").reverse()
        education_queryset = Education.objects.all().order_by("ranking").reverse()

        # Convert QuerySets to pandas DataFrames
        experiences_df = pd.DataFrame(list(
            experiences_queryset.values('title', 'company', 'ranking', 'start_date', 'end_date', 'role')
        ))
        experiences_df['type'] = 'Experience'
        experiences_df['ranking_compressed'] = min_max_scale(experiences_df['ranking'])
        experiences_df['company_title'] = experiences_df['title'] + ' - ' + experiences_df['company']

        education_df = pd.DataFrame(list(
            education_queryset.values('title', 'institution', 'ranking', 'start_date', 'end_date', 'role')
        ))
        education_df['type'] = 'Education'
        education_df['ranking_compressed'] = min_max_scale(education_df['ranking']) - 1
        education_df = education_df.loc[education_df['ranking'].astype(int) > 3]
        education_df['company_title'] = education_df['title'] + ' - ' + education_df['institution']

        # Ensure dates are in datetime format
        experiences_df['start_date'] = pd.to_datetime(experiences_df['start_date'])
        experiences_df['end_date'] = pd.to_datetime(experiences_df['end_date'])
        education_df['start_date'] = pd.to_datetime(education_df['start_date'])
        education_df['end_date'] = pd.to_datetime(education_df['end_date'])

        # Combine DataFrames
        combined_df = pd.concat([experiences_df, education_df]).reset_index(drop=True).sort_values('start_date')
        today = pd.Timestamp.today().normalize()
        combined_df['end_date'] = combined_df['end_date'].fillna(today)

        roles = combined_df['role'].unique()

        # Define transparent color mapping based on role
        color_map = {
            f'{roles[0]}': 'rgba(255,0,0,0.3)',  # Example role with red color
            f'{roles[1]}': 'rgba(0,255,0,0.3)',  # Example role with green color
            f'{roles[2]}': 'rgba(0,0,255,0.3)',  # Example role with blue color
            'Default': 'rgba(128,128,128,0.3)'  # Default color with transparency
        }

        # Calculate min and max dates
        min_date = combined_df['start_date'].min()
        max_date = combined_df['end_date'].max() + pd.Timedelta(days=180)
        
        # Create a Plotly scatter plot
        fig = go.Figure()

        # Define the height offset for rectangles
        height_offset = 0.05  # Adjust as needed
        
        fig = make_subplots(specs=[[{"secondary_y": True}]])

        # Add scatter plot and rectangles for each row in the combined DataFrame
        for _, row in combined_df.iterrows():
            role_color = color_map.get(row['role'], color_map['Default'])  # Use role-based color or default
            
            # Define the y-coordinates for the rectangle
            y_bottom = row['ranking_compressed'] - height_offset
            y_top = row['ranking_compressed'] + height_offset

            # Add scatter plot with rectangle properties
            fig.add_trace(go.Scatter(
                x=[row['start_date'], row['end_date'], row['end_date'], row['start_date'], row['start_date']],
                y=[y_bottom, y_bottom, y_top, y_top, y_bottom],
                # fill='toself',
                fillcolor=role_color,
                line=dict(color='rgba(0,0,0,0)'),
                text=[row['company_title']],  # Add company title for hover text
                textposition='middle center',
                mode='markers+lines',  # Use markers and lines for better visibility
                marker=dict(color=role_color, size=1),  # Adjust marker size as needed
                name=row['role'],  # Assign role as the trace name (for legend), 
            ))

            # Define the y-coordinates for the rectangle
            y_bottom = row['ranking_compressed'] - height_offset
            y_top = row['ranking_compressed'] + height_offset

            # Add rectangle to represent the area
            fig.add_trace(go.Scatter(
                x=[row['start_date'], row['end_date'], row['end_date'], row['start_date'], row['start_date']],
                y=[y_bottom, y_bottom, y_top, y_top, y_bottom],
                fill='toself',
                fillcolor=role_color,
                line=dict(color='rgba(0,0,0,0)'),
                showlegend=False,
            ))

            # Add annotation at the midpoint with bold text formatting
            midpoint_x = row['start_date'] + (row['end_date'] - row['start_date']) / 2
            midpoint_y = row['ranking_compressed'] 
            
            # Format company_title with line breaks
            formatted_title = f"<b>{row['company_title'].split(' - ')[0]}</b>"
            formatted_title += "<br>"
            formatted_title += f"{row['company_title'].split(' - ')[1]}"

            fig.add_trace(go.Scatter(
                x=[midpoint_x],
                y=[midpoint_y],
                text=[formatted_title], 
                mode='text',
                textposition='middle center',
                showlegend=False,
            ))
        

        # Update layout with images
        fig.update_layout(
            title='<b>JOB HISTORY</b>',  # Set title with bold formatting
            title_x=0.5,  # Center the title horizontally
            xaxis_title='Start Date',
            yaxis_title='JOB',
            yaxis=dict(showticklabels=False),
            xaxis=dict(
                tickformat='%b %Y',  # Display month and year
                tickangle=-45,  # Rotate x-axis labels
                range=[min_date, max_date],
                tickvals=combined_df['start_date'].tolist() + combined_df['end_date'].tolist(),
            ),
            paper_bgcolor='lightgrey',  # Set the background color of the entire plot
            plot_bgcolor='lightgrey',
            showlegend=False,
        )

        # Convert the plot to HTML
        plot_html = fig.to_html(full_html=False)

        # Return the plot HTML directly
        return HttpResponse(plot_html, content_type='text/html')
    
    return HttpResponseNotAllowed(['GET'])
