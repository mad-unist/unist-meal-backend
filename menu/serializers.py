from rest_framework import serializers
from menu.models import Menu
from django.db.models import Avg


class MenuSerializer(serializers.ModelSerializer):
    rating = serializers.SerializerMethodField()
    rating_count = serializers.SerializerMethodField()
    class Meta:
        model = Menu
        fields = ("id", "place", "type", "time", "content", "calorie", "date", "rating", "rating_count")
        
    def get_rating(self, obj):
        rating = obj.ratings.all().aggregate(avg_rating=Avg("rating"))["avg_rating"]
        return rating if rating else 0.0
    
    def get_rating_count(self, obj):
        return obj.ratings.all().count()

class MenuXRatingSerializer(serializers.ModelSerializer):
    rating = serializers.SerializerMethodField()
    rating_count = serializers.SerializerMethodField()
    date = serializers.SerializerMethodField()
    class Meta:
        model = Menu
        fields = ( "place", "time", "date", "rating", "rating_count")
        
    def get_rating(self, obj):
        rating = obj.ratings.all().aggregate(avg_rating=Avg("rating"))["avg_rating"]
        return rating if rating else 0.0
    
    def get_rating_count(self, obj):
        return obj.ratings.all().count()

    def get_date(self, obj):
        return obj.date.strftime("%Y-%m-%d")

    