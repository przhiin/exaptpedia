import os, django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'expatpedia.settings')
django.setup()

from accounts.models import CustomUser

# List of users you want to add
users_to_add = [
    {"username": "meee1", "email": "meee1@example.com"},
    {"username": "mooo2", "email": "mooo2@example.com"},
    {"username": "user3", "email": "user3@example.com"},
]

# Get all existing usernames in the DB
existing_usernames = set(CustomUser.objects.values_list("username", flat=True))

# Create only new users
new_users = [
    CustomUser(username=u["username"], email=u["email"])
    for u in users_to_add
    if u["username"] not in existing_usernames
]

if new_users:
    CustomUser.objects.bulk_create(new_users)
    print(f"✅ Added {len(new_users)} new users.")
else:
    print("⚠️ All users already exist — no new users added.")
