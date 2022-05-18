from django.urls import path
from menu import views

urlpatterns = [
    path("v1/menus", views.MenuList.as_view(), name="v1_menu_list"),
]
