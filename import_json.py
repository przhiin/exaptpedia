import json
import os
import django

# If running outside Django manage.py
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "exaptpedia.settings")
django.setup()

from accounts.models import CustomUser  # import your model

# Load JSON file
with open('data.json', 'r') as f:
    data = json.load(f)

# Iterate and save
for item in data:
    CustomUser.objects.create(
        username=item.get('username'),
        occupation=item.get('occupation', ''),   
        email=item.get('email', ''),  
        first_name=item.get('first_name', ''),
        last_name=item.get('last_name', ''),
        phone=item.get('phone', ''),
        address=item.get('address', ''),
        age=item.get('age'),
        
    )

print("Data imported successfully!")
