from restaurant.models import Restaurant


def fetch_restaurants():
    conditions = {}
    restaurants = Restaurant.objects.filter(**conditions).all()
    return restaurants
