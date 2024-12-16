from django.core.management.base import BaseCommand
from django.utils import timezone
from django.contrib.auth.models import User
from rest_api.models import Tasks

class Command(BaseCommand):
    help = 'Populates the auth_user and rest_api_tasks tables with sample data'

    def handle(self, *args, **options):
        # Check if the admin user already exists
        user, created = User.objects.get_or_create(
            username='admin',
            defaults={
                'password': 'root',
                'first_name': 'Mr.',
                'last_name': 'Admin',
                'email': 'admin@admin.edu',
                'is_superuser': True,
                'is_staff': True
            }
        )

        # If user is created, set the password (since get_or_create() doesn't set it)
        if created:
            user.set_password('root')
            user.save()

        # List of task data to insert
        tasks_data = [
            (1,'Make soup', 'Gather the ingredients', '2024-12-15 20:13:20.566959+00', False, '2024-12-15 20:13:20.566978+00'),
            (2,'Get the dog', 'Animal shelter near the store.', '2024-12-15 20:13:33.205051+00', False, '2024-12-15 20:13:33.205082+00'),
            (3,'New Simple Task', 'Be productive', '2024-12-15 20:30:56.693376+00', True, '2024-12-15 20:30:56.6934+00'),
            (4,'Finish the Project', 'Do everything', '2024-12-15 20:37:17.940634+00', False, '2024-12-15 20:37:17.940653+00'),
            (5,'Touch grass', 'You know what to do.', '2024-12-15 20:15:03.86957+00', False, '2024-12-15 20:15:03.869768+00'),
        ]

        # Iterate through tasks data and create Task instances
        for task_data in tasks_data:
            # Check if the task already exists
            task, created = Tasks.objects.get_or_create(
                id=task_data[0],
                defaults={
                    'task': task_data[1],
                    'description': task_data[2],
                    'timestamp': timezone.datetime.fromisoformat(task_data[3]), 
                    'completed': task_data[4],
                    'updated': timezone.datetime.fromisoformat(task_data[5]), 
                    'user': user
                }
            )

            # Check if task was created or already existed
            if created:
                self.stdout.write(self.style.SUCCESS(f'Task {task.id} created successfully'))
            else:
                self.stdout.write(self.style.SUCCESS(f'Task {task.id} already exists'))

        self.stdout.write(self.style.SUCCESS('Successfully populated the tables'))
