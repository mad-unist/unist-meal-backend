from rest_framework.response import Response
from rest_framework.views import APIView
from .models import User
from account.serializers import UserSerializer
from account.services import fetch_users, create_user, get_user
from rest_framework.permissions import IsAdminUser


class UserList(APIView):
    
    # permission_classes = [IsAdminUser]
    
    def get(self, request):
        users = fetch_users()
        data = UserSerializer(users, many=True).data
        return Response({"data": data}, status=200)
    
    def post(self, request):
        id = request.data["user_id"]
        email = request.data["email"] if "email" in request.data else None
        if User.objects.filter(id=id).exists():
            user = get_user(id)
        else:
            user = create_user(id, email)
        data = UserSerializer(user).data
        return Response({"data": data}, status=200)
