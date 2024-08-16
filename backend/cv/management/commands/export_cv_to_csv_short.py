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

        return df

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

        return df



    def get_combined_dataframe(self):
        # Get the education and experience dataframes
        education_df = self.get_education_dataframe()
        experience_df = self.get_experience_dataframe()

        # Concatenate dataframes
        combined_df = pd.concat([education_df, experience_df], ignore_index=True)
        combined_df = self.get_time_integers(combined_df)

        # Add time_integer to the combined dataframe
        # combined_df = self.add_time_integer(combined_df)
        
        return combined_df


    def get_time_integers(self, df):
        # time in job
        df['months_diff'] = (df['end_date'] - df['start_date']) / pd.Timedelta(days=30)
        df['months_diff'] = df['months_diff'].apply(lambda x: int(x) + 1)

        # time from first month
        first_month = df['start_date'].min()
        df['diff_start_from_first_month'] = (df['start_date'] - first_month) / pd.Timedelta(days=30)
        df['diff_start_from_first_month'] = df['diff_start_from_first_month'].apply(lambda x: int(x) + 1)

        df['diff_end_from_first_month'] = (df['end_date'] - first_month) / pd.Timedelta(days=30)
        df['diff_end_from_first_month'] = df['diff_end_from_first_month'].apply(lambda x: int(x) + 1)

        df['middle_month'] = (df['diff_end_from_first_month'] + df['diff_start_from_first_month']) / 2
        df['middle_month'] = df['middle_month'].apply(lambda x: int(x) + 1)

        df['y'] = df['ranking'] * (.1)
        
        return df
