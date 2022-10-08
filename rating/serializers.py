from rest_framework import serializers
from rating.models import Rating
from menu.models import Menu
from django.db.models import Avg


class RatingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Rating
        fields = ("id", "rating", "user", "menu")

class MenuXRatingSerializer(serializers.ModelSerializer):
    date = serializers.SerializerMethodField()
    class Meta:
        model = Menu
        fields = ("place", "time", "date")

    def get_date(self, obj):
        return obj.date.strftime("%Y-%m-%d")
    
class RatingXMenuSerializer(serializers.ModelSerializer):
    menu = MenuXRatingSerializer()
    class Meta:
        model = Rating
        fields = ("id", "menu", "rating")