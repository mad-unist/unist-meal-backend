from django.urls import path
from account import views

urlpatterns = [
    path("v1/users", views.UserList.as_view(), name="v1_user_list"),
    path("v1/user/<str:id>", views.UserDetail.as_view(), name="v1_user_detail"),
]