from rest_framework.response import Response
from rest_framework.views import APIView
from rating.models import Rating
from rating.serializers import RatingSerializer
from rating.services import check_other_menu_rated_in_same_time, check_today_menu_rated, fetch_ratings, create_rating, fetch_today_ratings_by_user, update_rating, delete_rating, fetch_ratings_by_user


class RatingList(APIView):
    def get(self, request):
        ratings = fetch_ratings()
        data = RatingSerializer(ratings, many=True).data
        return Response({"data": data}, status=200)
    
    def post(self, request):
        user_id = request.data.get("user_id")
        menu_id = request.data.get("menu_id")
        rating = request.data.get("rating")
        
        if Rating.objects.filter(user_id=user_id, menu_id=menu_id).exists():
            rating = update_rating(user_id, menu_id, rating)
        else:
            check_today_menu_rated(menu_id)
            check_other_menu_rated_in_same_time(user_id, menu_id)
            rating = create_rating(user_id, menu_id, rating)
            
        data = RatingSerializer(rating).data
        return Response({"data": data}, status=201)
    
    def delete(self, request):
        user_id = request.data.get("user_id")
        menu_id = request.data.get("menu_id")
        delete_rating(user_id, menu_id)
        return Response({"message": "success"}, status=200)
    
class RatingListByUser(APIView):
    def get(self, request, user_id):
        ratings = fetch_ratings_by_user(user_id)
        data = RatingSerializer(ratings, many=True).data
        return Response({"data": data}, status=200)
    
class TodayRatingListByUser(APIView):
    def get(self, request, user_id):
        ratings = fetch_today_ratings_by_user(user_id)
        data = RatingSerializer(ratings, many=True).data
        return Response({"data": data}, status=200)