from account.models import User
from django.db.utils import IntegrityError
from rest_framework.exceptions import ValidationError

def fetch_users():
    conditions = {}
    users = User.objects.filter(**conditions).all()
    return users

def get_user(id):
    try:
        user = User.objects.get(id=id)
    except User.DoesNotExist:
        raise ValidationError("Error for getting user")
    return user

def create_user(id, email):
    try:
        user = User.objects.create(
            id=id,
            email=email
        )
    except IntegrityError:
        raise ValidationError("Error for creating user")
    return user

def delete_user(id):
    try:
        user = get_user(id)
        user.delete()
    except User.DoesNotExist:
        raise ValidationError("Error for deleting user")