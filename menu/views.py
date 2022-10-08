from rest_framework.response import Response
from rest_framework.views import APIView
from menu.serializers import MenuSerializer, MenuXRatingSerializer
from menu.services import fetch_menus, fetch_today_menus, fetch_menus_with_ratings


class MenuList(APIView):
    def get(self, request):
        menus = fetch_menus()
        data = MenuSerializer(menus, many=True).data
        return Response({"data": data}, status=200)

class TodayMenuList(APIView):
    def get(self, request):
        menus = fetch_today_menus()
        data = MenuSerializer(menus, many=True).data
        return Response({"data": data}, status=200)

class MenuRatingList(APIView):
    def get(self, request):
        menus = fetch_menus_with_ratings()
        data = MenuXRatingSerializer(menus, many=True).data
        return Response(data, status=200)