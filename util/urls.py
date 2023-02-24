from django.urls import path
from util import views

app_name="util"

urlpatterns = [
    path("v1/upload-file", views.UploadFile.as_view(), name="v1_upload_file"),
    path("v1/process-menus-dormitory", views.ProcessExcelMenuDormitory.as_view(), name="v1_process_menus_dormitory"),
    path("v1/process-menus-dormitory2", views.ProcessExcelMenuDormitory2.as_view(), name="v1_process_menus_dormitory2"),
    path("v1/process-menus-dormitory-vacation", views.ProcessExcelMenuDormitoryVacation.as_view(), name="v1_process_menus_dormitory_vacation"),
    path("v1/process-menus-student", views.ProcessExcelMenuStudent.as_view(), name="v1_process_menus_student"),
    path("v1/process-menus-professor", views.ProcessExcelMenuProfessor.as_view(), name="v1_process_menus_professor"),
]
