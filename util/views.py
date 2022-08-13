from django.shortcuts import render
from menu.serializers import MenuSerializer
from util.services import get_excel_sheet, make_7dates, make_menu
from rest_framework.views import APIView
from rest_framework.permissions import IsAdminUser
from rest_framework.response import Response


places = ["기숙사식당", "학생식당", "교직원식당"]

class UploadFile(APIView):
    permission_classes = [IsAdminUser]
    def get(self, requset):
        return render(self.request, 'util/index.html')

class ProcessExcelMenuDormitory(APIView):
    permission_classes = [IsAdminUser]
    
    def process_menu(self, worksheet, place):
        day_idx = ["E", "G", "I", "K", "M", "O", "Q"]
        date_idx = 6
        moring_idx = [7, 13, "아침"]
        week_lunch_idx = [[14, 21, "점심", "한식"], [22, 28, "점심", "일품"]]
        weekend_lunch_idx = [14, 27, "점심"]
        evening_idx = [34, 41, "저녁"]
        
        datas = []
        date = worksheet["E"][date_idx].value
        dates= make_7dates(date)
        for i in range(7):  
            datas.append(make_menu(worksheet, place, day_idx[i], dates[i], moring_idx[0], moring_idx[1], moring_idx[2])) # 아침
            if day_idx[i] in ["O", "Q"]: # 주말
                datas.append(make_menu(worksheet, place, day_idx[i], dates[i],weekend_lunch_idx[0], weekend_lunch_idx[1], weekend_lunch_idx[2])) # 점심 (한식)
            else:
                datas.append(make_menu(worksheet, place, day_idx[i], dates[i], week_lunch_idx[0][0], week_lunch_idx[0][1], week_lunch_idx[0][2], week_lunch_idx[0][3])) # 점심 (한식)
                datas.append(make_menu(worksheet, place, day_idx[i], dates[i], week_lunch_idx[1][0], week_lunch_idx[1][1], week_lunch_idx[1][2], week_lunch_idx[1][3])) # 점심 (일품)
            datas.append(make_menu(worksheet, place, day_idx[i], dates[i], evening_idx[0], evening_idx[1], evening_idx[2])) # 저녁
        return datas
        
    def post(self, requset):
        worksheet = get_excel_sheet(self.request.FILES["excel_file"])
        datas = self.process_menu(worksheet, places[0])        
        return Response({"count": len(datas), "data": MenuSerializer(datas, many=True).data}, status=200)
    
class ProcessExcelMenuStudent(APIView):
    pass
    
    
class ProcessExcelMenuProfessor(APIView):
    permission_classes = [IsAdminUser]
    def process_menu(self, worksheet, place):
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
        return datas
        
    def post(self, requset):
        worksheet = get_excel_sheet(self.request.FILES["excel_file"])
        datas = self.process_menu(worksheet, places[2])        
        return Response({"count": len(datas), "data": MenuSerializer(datas, many=True).data}, status=200)