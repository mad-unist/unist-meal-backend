from rest_framework.response import Response
from rest_framework.views import APIView

from restaurant.serializers import RestaurantSerializer
from restaurant.services import fetch_restaurants


class RestaurantList(APIView):
    def get(self, request):
        restaurants = fetch_restaurants()
        data = RestaurantSerializer(restaurants, many=True).data
        return Response({"data": data}, status=200)
