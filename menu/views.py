from rest_framework.response import Response
from rest_framework.views import APIView
from menu.serializers import MenuSerializer
from menu.services import fetch_menus


class MenuList(APIView):
    def get(self, request):
        menus = fetch_menus()
        data = MenuSerializer(menus, many=True).data
        return Response({"data": data}, status=200)
