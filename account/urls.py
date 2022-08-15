from django.urls import path
from account import views

urlpatterns = [
    path("v1/users", views.UserList.as_view(), name="v1_menu_list"),
]