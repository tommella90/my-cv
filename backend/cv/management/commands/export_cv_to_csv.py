import csv
import pandas as pd
from django.core.management.base import BaseCommand
from cv.models import Education, Experience
from datetime import datetime

class Command(BaseCommand):
    help = 'Export data from Education and Experience models to a combined CSV'

    def handle(self, *args, **kwargs):
        # Define CSV file path
        combined_file_path = '../touchdesigner_plotter/cv_timeseries.csv'

        # Export Education and Experience data
        try:
            # Get the combined dataframe with time_integer
            combined_df = self.get_combined_dataframe()
            
            # Save to CSV
            combined_df.to_csv(combined_file_path, index=False)
            self.stdout.write(self.style.SUCCESS(f'Successfully exported combined data to {combined_file_path}'))
        except Exception as e:
            self.stderr.write(self.style.ERROR(f'Error exporting data: {e}'))

    def get_education_dataframe(self):
        # Query Education data and convert to DataFrame
        data = list(Education.objects.all().values(
            'id', 'title', 'institution', 'subtitle', 'role', 'location', 'grade', 'start_date', 'end_date', 'ranking'
        ))
        
        df = pd.DataFrame(data)
        
        # Convert date columns to datetime
        df['start_date'] = pd.to_datetime(df['start_date'])
        df['end_date'] = pd.to_datetime(df['end_date'], errors='coerce')

        # Handle NaT values in 'end_date' by replacing with today's date
        today = pd.Timestamp.now()
        df['end_date'] = df['end_date'].fillna(today)

        # Generate monthly rows
        rows = []
        for _, row in df.iterrows():
            months = pd.date_range(start=row['start_date'], end=row['end_date'], freq='MS')
            for month in months:
                rows.append([
                    row['id'],
                    row['title'],
                    row['institution'],
                    row['subtitle'],
                    row['role'],
                    row['location'],
                    month.strftime('%Y-%m'),
                    row['ranking']
                ])
                
        education_df = pd.DataFrame(rows, columns=[
            'id', 'title', 'institution', 'subtitle', 'role', 'location', 'month', 'ranking'
        ])
        return education_df

    def get_experience_dataframe(self):
        # Query Experience data and convert to DataFrame
        data = list(Experience.objects.all().values(
            'id', 'title', 'company', 'subtitle', 'role', 'location', 'start_date', 'end_date', 'ranking'
        ))
        
        df = pd.DataFrame(data)
        
        # Convert date columns to datetime
        df['start_date'] = pd.to_datetime(df['start_date'])
        df['end_date'] = pd.to_datetime(df['end_date'], errors='coerce')

        # Handle NaT values in 'end_date' by replacing with today's date
        today = pd.Timestamp.now()
        df['end_date'] = df['end_date'].fillna(today)

        # Generate monthly rows
        rows = []
        for _, row in df.iterrows():
            months = pd.date_range(start=row['start_date'], end=row['end_date'], freq='MS')
            for month in months:
                rows.append([
                    row['id'],
                    row['title'],
                    row['company'],
                    row['subtitle'],
                    row['role'],
                    row['location'],
                    month.strftime('%Y-%m'),
                    row['ranking']
                ])
                
        experience_df = pd.DataFrame(rows, columns=[
            'id', 'title', 'company', 'subtitle', 'role', 'location', 'month', 'ranking'
        ])
        return experience_df

    def add_time_integer(self, df):
        # Convert 'month' to datetime to sort and create a sequential index
        df['month'] = pd.to_datetime(df['month'], format='%Y-%m')
        
        # Create a unique sorted list of months
        unique_months = sorted(df['month'].unique())
        
        # Create a mapping from month to time_integer
        month_to_integer = {month: i + 1 for i, month in enumerate(unique_months)}
        
        # Map the time_integer to the DataFrame
        df['time_integer'] = df['month'].map(month_to_integer)
        return df

    def get_combined_dataframe(self):
        # Get the education and experience dataframes
        education_df = self.get_education_dataframe()
        experience_df = self.get_experience_dataframe()

        # Concatenate dataframes
        combined_df = pd.concat([education_df, experience_df], ignore_index=True)

        # Add time_integer to the combined dataframe
        combined_df = self.add_time_integer(combined_df)
        return combined_df
