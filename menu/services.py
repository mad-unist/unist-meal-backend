from datetime import datetime, timedelta, time
from menu.models import Menu
from rest_framework.exceptions import ValidationError
from django.db.utils import IntegrityError

def fetch_menus():
    conditions = {}
    menus = Menu.objects.filter(**conditions).all()
    return menus


def fetch_today_menus():
    today = datetime.now().date()
    tomorrow = today + timedelta(1)
    today_start = datetime.combine(today, time())
    today_end = datetime.combine(tomorrow, time())
    conditions = {"date__lt": today_end, "date__gte": today_start}
    menus = Menu.objects.filter(**conditions).all()
    return menus

def get_menu(menu_id):
    try:
        menu = Menu.objects.get(id=menu_id)
    except Menu.DoesNotExist:
        raise ValidationError("Error for getting menu")
    return menu