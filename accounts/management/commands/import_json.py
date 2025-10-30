import os
import json
import django
from django.core.management.base import BaseCommand
from accounts.models import Members, JobCategory

# Django setup (if running outside manage.py)
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "expatpedia.settings")
django.setup()


class Command(BaseCommand):
    help = 'Import members from a JSON file with position and occupation_category'

    def add_arguments(self, parser):
        parser.add_argument('json_file', type=str, help='Path to the JSON file')

    def handle(self, *args, **kwargs):
        json_file = kwargs['json_file']

        try:
            with open(json_file, 'r', encoding='utf-8') as f:
                data = json.load(f)
        except FileNotFoundError:
            self.stdout.write(self.style.ERROR(f"❌ File '{json_file}' not found!"))
            return
        except json.JSONDecodeError:
            self.stdout.write(self.style.ERROR(f"❌ Invalid JSON format in file '{json_file}'!"))
            return

        count = 0
        for item in data:
            try:
                # ✅ Extract both position and occupation_category
                occupation_value = item.get('position', '').strip()
                category_value = item.get('occupation_category', '').strip()

                # ✅ Create or get JobCategory if category_value exists
                occupation_category = None
                if category_value:
                    occupation_category, _ = JobCategory.objects.get_or_create(name=category_value)

                # ✅ Create member
                user = Members(
                    name=item.get('name', '').strip(),
                    email=item.get('email', '').strip(),
                    phone=item.get('phone', '').strip(),
                    position=occupation_value or None,
                    occupation_category=occupation_category
                )
                user.save()
                count += 1
            except Exception as e:
                self.stdout.write(self.style.WARNING(
                    f"⚠️ Failed to import {item.get('email', 'Unknown')}: {str(e)}"
                ))
                continue

        self.stdout.write(self.style.SUCCESS(f"✅ Successfully imported {count} members!"))
