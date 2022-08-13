from django.urls import path
from notice import views

urlpatterns = [
    path("v1/notices", views.NoticeList.as_view(), name="v1_notice_list"),
    path("v1/notice/<int:notice_id>", views.NoticeDetail.as_view(), name="v1_notice_detail")
]
