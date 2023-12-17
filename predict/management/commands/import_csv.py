import csv
from django.core.management.base import BaseCommand
from django.utils import timezone
from datetime import datetime
from predict.models import Match


class Command(BaseCommand):
    help = 'Import data from CSV file'

    def handle(self, *args, **options):
        csv_filename = 'predict/static/predict/data/fixture.csv'

        with open(csv_filename, 'r', encoding='utf-8') as csv_file:
            csv_reader = csv.DictReader(csv_file)

            for row in csv_reader:
                # Parse the date and convert it to the correct format
                date_str = row['Date']
                date_obj = datetime.strptime(date_str, '%d/%m/%Y %H:%M')
                formatted_date = timezone.make_aware(date_obj)

                Match.objects.create(
                    team1=row['HomeTeam'],
                    team2=row['AwayTeam'],
                    date=formatted_date,
                    location=row['Location']
                )

        self.stdout.write(self.style.SUCCESS('Data imported successfully'))
