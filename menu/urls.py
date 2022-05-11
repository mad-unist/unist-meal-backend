from django.urls import path, include
from menu import views

urlpatterns = [
    path("v1/menus", views.MenuList.as_view(), name="v1_menu_list"),
]
