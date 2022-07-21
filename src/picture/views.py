from rest_framework.response import Response
from rest_framework.views import APIView

from picture.serializers import PictureSerializer
from picture.services import fetch_pictures


class PictureList(APIView):
    def get(self, request):
        pictures = fetch_pictures()
        data = PictureSerializer(pictures, many=True).data
        return Response({"data": data}, status=200)
