from django.urls import path
from rating import views

app_name="rating"

urlpatterns = [
    path("v1/ratings", views.RatingList.as_view(), name="v1_rating_list"),
    path("v1/ratings/<str:user_id>", views.RatingListByUser.as_view(), name="v1_rating_list_by_user"),
    path("v1/today-ratings/<str:user_id>", views.TodayRatingListByUser.as_view(), name="v1_today_rating_list_by_user"),
]