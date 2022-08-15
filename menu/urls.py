from django.urls import path
from menu import views

urlpatterns = [
    path("v1/menus", views.MenuList.as_view(), name="v1_menu_list"),
    path("v1/today-menus", views.TodayMenuList.as_view(), name="v1_today_menu_list"),
]
