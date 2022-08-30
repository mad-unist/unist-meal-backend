from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.decorators import api_view
from .models import User
from account.serializers import UserSerializer
import account.services as services

class UserList(APIView):
    def post(self, request):
        id = request.data["user_id"]
        email = request.data["email"] if "email" in request.data else None
        if User.objects.filter(id=id).exists():
            user = services.get_user(id)
        else:
            user = services.create_user(id, email)
        data = UserSerializer(user).data
        return Response({"data": data}, status=200)
        
@api_view(["POST"])
def delete_user(request):
    id = request.data["user_id"]
    services.delete_user(id)
    return Response({"data": "success"}, status=200)