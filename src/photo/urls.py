from django.urls import path

from photo import views


urlpatterns = [
    path("v1/photos", views.PhotoList.as_view(), name="v1_photo_list"),
]
