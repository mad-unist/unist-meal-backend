from django.urls import path

from picture import views


urlpatterns = [
    path("v1/pictures", views.PictureList.as_view(), name="v1_pictures_list"),
]
