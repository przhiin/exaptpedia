import json
import os
import django
import random
import string
from django.core.management.base import BaseCommand
from accounts.models import CustomUser 
# If running outside Django manage.py
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "exaptpedia.settings")
django.setup()

from accounts.models import CustomUser  # import your model

# Load JSON file
with open('data.json', 'r') as f:
    data = json.load(f)

# Iterate and save

class Command(BaseCommand):
    help = 'Import users from a JSON file'

    def add_arguments(self, parser):
        parser.add_argument('json_file', type=str, help='Path to the JSON file')

    def handle(self, *args, **kwargs):
        json_file = kwargs['json_file']
        with open(json_file, 'r') as f:
            data = json.load(f)

        for item in data:
            # Generate random username from first and last name
            name = item.get('name', '').lower()
            base_username = name if name.strip() else 'user'
            random_number = ''.join(random.choices(string.digits, k=4))
            username = f"{base_username}{random_number}"

            user = CustomUser(
                username=username,
                email=item.get('email', ''),
                name =item.get('name', ''),
                phone=item.get('phone', ''),
                occupation=item.get('occupation', '')
            )
            user.save()
print("Data imported successfully!")
