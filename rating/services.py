from menu.services import get_menu
from rating.models import Rating
from django.db.utils import IntegrityError
from rest_framework.exceptions import ValidationError
from datetime import datetime

def fetch_ratings():
    conditions = {}
    ratings = Rating.objects.filter(**conditions).all()
    return ratings

def check_today_menu_rated(menu_id):
    menu = get_menu(menu_id)
    menu_date = menu.date.strftime("%Y-%m-%d")
    today = datetime.today().strftime("%Y-%m-%d")
    if menu_date != today:
        raise ValidationError("Only today's menu can be rated")
    
def check_other_menu_rated_in_same_time(user_id, menu_id):
    menu = get_menu(menu_id)
    ratings = Rating.objects.filter(user_id=user_id).all()
    for rating in ratings:
        
        if rating.menu.time == menu.time and rating.menu.date.strftime("%Y-%m-%d") == menu.date.strftime("%Y-%m-%d"): # 같은 시간이고 날짜가 같다면
            raise ValidationError("You have already rated other menu in same time")

def get_rating(user_id, menu_id):
    try:
        rating = Rating.objects.get(user_id=user_id, menu_id=menu_id)
    except Rating.DoesNotExist:
        raise ValidationError("Error for getting rating")
    return rating

def create_rating(user_id, menu_id, rating):
    try:
        rating = Rating.objects.create(user_id=user_id, menu_id=menu_id, rating=rating)
    except IntegrityError:
        raise ValidationError("Error for creating rating")
    return rating

def update_rating(user_id, menu_id, rating: int):
    try:
        rating_obj = get_rating(user_id, menu_id)
        rating_obj.rating = rating
        rating_obj.save()
    except Rating.DoesNotExist:
        raise ValidationError("Error for updating rating")
    return rating_obj

def delete_rating(user_id, menu_id):
    try:
        rating = get_rating(user_id, menu_id)
        rating.delete()
    except Rating.DoesNotExist:
        raise ValidationError("Error for deleting rating")
    return rating