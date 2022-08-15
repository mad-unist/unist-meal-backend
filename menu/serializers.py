from rest_framework import serializers
from menu.models import Menu
from django.db.models import Avg


class MenuSerializer(serializers.ModelSerializer):
    rating = serializers.SerializerMethodField()
    class Meta:
        model = Menu
        fields = ("id", "place", "type", "time", "content", "calorie", "date", "rating")
        
    def get_rating(self, obj):
        rating = obj.ratings.all().aggregate(avg_rating=Avg("rating"))["avg_rating"]
        return rating if rating else 0.0