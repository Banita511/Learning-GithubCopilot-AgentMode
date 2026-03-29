from django.core.management.base import BaseCommand
from django.contrib.auth import get_user_model
# Import your models here
# from octofit_tracker.models import Activity, Team, Workout

class Command(BaseCommand):
    help = 'Populates the database with initial data for Octofit Tracker.'

    def handle(self, *args, **options):
        User = get_user_model()
        # Example: Create a superuser if not exists
        if not User.objects.filter(username='admin').exists():
            User.objects.create_superuser('admin', 'admin@example.com', 'adminpass')
            self.stdout.write(self.style.SUCCESS('Created superuser admin'))
        else:
            self.stdout.write(self.style.WARNING('Superuser admin already exists'))

        # Add your data population logic here
        # Example:
        # if not Team.objects.filter(name='Team Alpha').exists():
        #     Team.objects.create(name='Team Alpha')
        #     self.stdout.write(self.style.SUCCESS('Created Team Alpha'))
        # else:
        #     self.stdout.write(self.style.WARNING('Team Alpha already exists'))

        self.stdout.write(self.style.SUCCESS('Database population complete.'))
