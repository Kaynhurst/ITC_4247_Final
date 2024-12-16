from django.core.management.base import BaseCommand
from django.contrib.auth.models import User
from rest_api.models import Tasks
from django.utils.timezone import datetime as timezone_datetime


class Command(BaseCommand):
    help = 'Populates the auth_user and rest_api_tasks tables with sample data'

    def handle(self, *args, **options):
        # List of user data
        users_data = [
            {
                'username': 'admin',
                'password': 'root',
                'first_name': 'Mr.',
                'last_name': 'Admin',
                'email': 'admin@admin.edu',
                'is_superuser': True,
                'is_staff': True
            },
            {
                'username': 'johnp',
                'password': 'john123',
                'first_name': 'John',
                'last_name': 'Patsios',
                'email': 'john@admin.edu',
                'is_superuser': False,
                'is_staff': True
            },
            {
                'username': 'kpap',
                'password': 'kostas123',
                'first_name': 'Kostas',
                'last_name': 'Papadopoulos',
                'email': 'kostas@admin.edu',
                'is_superuser': False,
                'is_staff': True
            },
            {
                'username': 'mikes',
                'password': 'mike123',
                'first_name': 'Mike',
                'last_name': 'Strintzis',
                'email': 'mike@admin.edu',
                'is_superuser': False,
                'is_staff': True
            }
        ]

        # Create or update users
        for user_data in users_data:
            user, created = User.objects.get_or_create(
                username=user_data['username'],
                defaults={
                    'first_name': user_data['first_name'],
                    'last_name': user_data['last_name'],
                    'email': user_data['email'],
                    'is_superuser': user_data['is_superuser'],
                    'is_staff': user_data['is_staff']
                }
            )
            if created:
                user.set_password(user_data['password'])
                user.save()
                self.stdout.write(f"User '{user_data['username']}' created.")
            else:
                self.stdout.write(f"User '{user_data['username']}' already exists.")

        # List of task data
        tasks_data = [
            ('Make soup', 'Gather the ingredients', '2024-12-15 20:13:20.566959+00', False, '2024-12-15 20:13:20.566978+00', 1),
            ('Get the dog', 'Animal shelter near the store.', '2024-12-15 20:13:33.205051+00', False, '2024-12-15 20:13:33.205082+00', 1),
            ('New Simple Task', 'Be productive', '2024-12-15 20:30:56.693376+00', True, '2024-12-15 20:30:56.6934+00', 1),
            ('Finish the Project', 'Do everything', '2024-12-15 20:37:17.940634+00', False, '2024-12-15 20:37:17.940653+00', 1),
            ('Touch grass', 'You know what to do.', '2024-12-15 20:15:03.86957+00', False, '2024-12-15 20:15:03.869768+00', 1),
            ('Make the report', 'Do everything', '2024-12-15 20:37:17.940634+00', False, '2024-12-15 20:37:17.940653+00', 2),
            ('Eat shrimps', 'Yummy.', '2024-12-15 20:15:03.86957+00', False, '2024-12-15 20:15:03.869768+00', 2),
            ('Pet the cat', 'Yes', '2024-12-15 20:37:17.940634+00', False, '2024-12-15 20:37:17.940653+00', 3),
            ('Ride Bike', 'Vroom Vroom.', '2024-12-15 20:15:03.86957+00', False, '2024-12-15 20:15:03.869768+00', 3),
            ('Buy Flowers', 'All the Colors !!', '2024-12-15 20:37:17.940634+00', False, '2024-12-15 20:37:17.940653+00', 4),
            ('Sleep', 'You need it.', '2024-12-15 20:15:03.86957+00', True, '2024-12-15 20:15:03.869768+00', 4)
        ]

        # Create or update tasks
        for task_data in tasks_data:
            try:
                user = User.objects.get(id=task_data[5])
                task, created = Tasks.objects.get_or_create(
                    task=task_data[0],
                    defaults={
                        'description': task_data[1],
                        'timestamp': timezone_datetime.fromisoformat(task_data[2]),
                        'completed': task_data[3],
                        'updated': timezone_datetime.fromisoformat(task_data[4]),
                        'user': user
                    }
                )
                if created:
                    self.stdout.write(f"Task '{task_data[0]}' created.")
                else:
                    self.stdout.write(f"Task '{task_data[0]}' already exists.")
            except User.DoesNotExist:
                self.stdout.write(f"Error: User with ID {task_data[5]} does not exist.")
