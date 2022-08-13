from rest_framework.response import Response
from rest_framework.views import APIView
from notice.serializers import NoticeSerializer
from notice.services import fetch_notices, get_notice


class NoticeList(APIView):
    def get(self, request):
        menus = fetch_notices()
        data = NoticeSerializer(menus, many=True).data
        return Response({"data": data}, status=200)
    
class NoticeDetail(APIView):
    def get(self, request, notice_id):
        notice = get_notice(notice_id)
        data = NoticeSerializer(notice).data
        return Response({"data": data})