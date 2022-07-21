from rest_framework.response import Response
from rest_framework.views import APIView

from photo.serializers import PhotoSerializer
from photo.services import fetch_photos


class PhotoList(APIView):
    def get(self, request):
        photos = fetch_photos()
        data = PhotoSerializer(photos, many=True).data
        return Response({"data": data}, status=200)
