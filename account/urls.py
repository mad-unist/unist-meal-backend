from django.urls import path
from account import views

urlpatterns = [
    path("v1/users", views.UserList.as_view(), name="v1_user_list"),
    path("v1/delete-user", views.delete_user, name="v1_user_delete"),
]