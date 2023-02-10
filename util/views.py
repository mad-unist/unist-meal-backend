from xml.dom import ValidationErr
from django.shortcuts import render
from menu.serializers import MenuSerializer
from util.services import get_excel_sheet, make_7dates, make_menu
from rest_framework.views import APIView
from rest_framework.permissions import IsAdminUser
from rest_framework.response import Response

from django.db import transaction


places = ["기숙사식당", "학생식당", "교직원식당"]

class UploadFile(APIView):
    permission_classes = [IsAdminUser]
    def get(self, requset):
        return render(self.request, 'util/index.html')


class ProcessExcelMenuDormitory(APIView):
    permission_classes = [IsAdminUser]

    @transaction.atomic(using='default')
    def process_menu(self, worksheet, place):
        try:
            with transaction.atomic():
                day_idx = ["E", "G", "I", "K", "M", "O", "Q"]
                date_idx = 6
                moring_idx = [7, 13, "아침"]
                week_lunch_idx = [[14, 21, "점심", "한식"], [22, 28, "점심", "할랄"]]
                # evening_idx = [[35, 42, "저녁"], [43, 49, "저녁", "할랄"]]
                evening_idx = [[29, 36, "저녁", "한식"], [37, 43, "저녁", "할랄"]]
                
                datas = []
                date = worksheet["E"][date_idx].value
                dates= make_7dates(date)
                for i in range(7):  
                    datas.append(make_menu(worksheet, place, day_idx[i], dates[i], moring_idx[0], moring_idx[1], moring_idx[2])) # 아침
                    datas.append(make_menu(worksheet, place, day_idx[i], dates[i], week_lunch_idx[0][0], week_lunch_idx[0][1], week_lunch_idx[0][2], week_lunch_idx[0][3])) # 점심 (한식)
                    datas.append(make_menu(worksheet, place, day_idx[i], dates[i], week_lunch_idx[1][0], week_lunch_idx[1][1], week_lunch_idx[1][2], week_lunch_idx[1][3])) # 점심 (할랄)
                    datas.append(make_menu(worksheet, place, day_idx[i], dates[i], evening_idx[0][0], evening_idx[0][1], evening_idx[0][2], evening_idx[0][3])) # 저녁 (한식)
                    datas.append(make_menu(worksheet, place, day_idx[i], dates[i], evening_idx[1][0], evening_idx[1][1], evening_idx[1][2], evening_idx[1][3])) # 저녁 (할랄)
                datas = list(filter(lambda item: item is not None, datas))
        except:
            raise ValidationErr("식단표 업로드에 실패했습니다.")

        return datas
        
    def post(self, requset):
        worksheet = get_excel_sheet(self.request.FILES["excel_file"])
        datas = self.process_menu(worksheet, places[0])        
        return Response({"count": len(datas), "data": MenuSerializer(datas, many=True).data}, status=200)
    
class ProcessExcelMenuDormitoryVacation(APIView):
    permission_classes = [IsAdminUser]

    @transaction.atomic(using='default')
    def process_menu(self, worksheet, place):
        try:
            with transaction.atomic():
                day_idx = ["E", "G", "I", "K", "M", "O", "Q"]
                date_idx = 6
                moring_idx = [7, 13, "아침"]
                week_lunch_idx = [14, 21, "점심", "한식"]
                evening_idx = [22, 29, "저녁", "한식"]
                
                datas = []
                date = worksheet["E"][date_idx].value
                dates= make_7dates(date)
                for i in range(7):  
                    datas.append(make_menu(worksheet, place, day_idx[i], dates[i], moring_idx[0], moring_idx[1], moring_idx[2])) # 아침
                    datas.append(make_menu(worksheet, place, day_idx[i], dates[i], week_lunch_idx[0], week_lunch_idx[1], week_lunch_idx[2], week_lunch_idx[3])) # 점심 (한식)
                    datas.append(make_menu(worksheet, place, day_idx[i], dates[i], evening_idx[0], evening_idx[1], evening_idx[2], evening_idx[3])) # 저녁 (한식)
                datas = list(filter(lambda item: item is not None, datas))
        except:
            raise ValidationErr("식단표 업로드에 실패했습니다.")

        return datas
        
    def post(self, requset):
        worksheet = get_excel_sheet(self.request.FILES["excel_file"])
        datas = self.process_menu(worksheet, places[0])        
        return Response({"count": len(datas), "data": MenuSerializer(datas, many=True).data}, status=200)
    
class ProcessExcelMenuStudent(APIView):
    permission_classes = [IsAdminUser]

    @transaction.atomic(using='default')
    def process_menu(self, worksheet, place):
        try:
            with transaction.atomic():
                day_idx = ["E", "G", "I", "K", "M"]
                date_idx = 5
                week_lunch_idx = [6, 12, "점심"]
                evening_idx = [16, 22, "저녁"]
                
                datas = []
                date = worksheet["E"][date_idx].value
                dates= make_7dates(date)
                for i in range(5):  
                    datas.append(make_menu(worksheet, place, day_idx[i], dates[i], week_lunch_idx[0], week_lunch_idx[1], week_lunch_idx[2])) # 점심
                    datas.append(make_menu(worksheet, place, day_idx[i], dates[i], evening_idx[0], evening_idx[1], evening_idx[2])) # 저녁
                datas = list(filter(lambda item: item is not None, datas))
        except:
            raise ValidationErr("식단표 업로드에 실패했습니다.")
        return datas
    
    def post(self, requset):
        worksheet = get_excel_sheet(self.request.FILES["excel_file"])
        datas = self.process_menu(worksheet, places[1])        
        return Response({"count": len(datas), "data": MenuSerializer(datas, many=True).data}, status=200)
    
    
class ProcessExcelMenuProfessor(APIView):
    permission_classes = [IsAdminUser]

    @transaction.atomic(using='default')
    def process_menu(self, worksheet, place):
        try:
            with transaction.atomic():
                day_idx = ["E", "G", "I", "K", "M"]
                date_idx = 5
                week_lunch_idx = [6, 14, "점심"]
                evening_idx = [19, 26, "저녁"]
                
                datas = []
                date = worksheet["E"][date_idx].value
                dates= make_7dates(date)
                for i in range(5):  
                    datas.append(make_menu(worksheet, place, day_idx[i], dates[i], week_lunch_idx[0], week_lunch_idx[1], week_lunch_idx[2])) # 점심
                    datas.append(make_menu(worksheet, place, day_idx[i], dates[i], evening_idx[0], evening_idx[1], evening_idx[2])) # 저녁
                datas = list(filter(lambda item: item is not None, datas))
        except:
            raise ValidationErr("식단표 업로드에 실패했습니다.")
        return datas
        
    def post(self, requset):
        worksheet = get_excel_sheet(self.request.FILES["excel_file"])
        datas = self.process_menu(worksheet, places[2])        
        return Response({"count": len(datas), "data": MenuSerializer(datas, many=True).data}, status=200)