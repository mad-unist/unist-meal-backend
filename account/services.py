from account.models import User
from django.db.utils import IntegrityError
from rest_framework.exceptions import ValidationError

def fetch_users():
    conditions = {}
    users = User.objects.filter(**conditions).all()
    return users

def create_user(id, email):
    try:
        user = User.objects.create(
            id=id,
            email=email
        )
    except IntegrityError:
        raise ValidationError("Error for creating user")
    return user