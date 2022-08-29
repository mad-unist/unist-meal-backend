from rest_framework.response import Response
from rest_framework.views import APIView
from .models import User
from account.serializers import UserSerializer
from account.services import delete_user, fetch_users, create_user, get_user

class UserList(APIView):
    
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

class UserDetail(APIView):
    
    def get(self, request, id):
        user = get_user(id)
        data = UserSerializer(user).data
        return Response({"data": data}, status=200)
    
    def delete(self, request, id):
        delete_user(id)
        return Response({"message": "success"}, status=204)