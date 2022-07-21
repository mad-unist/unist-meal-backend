from django.urls import path

from restaurant import views


urlpatterns = [
    path("v1/restaurants", views.RestaurantList.as_view(), name="v1_restaurant_list"),
]
