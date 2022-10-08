from rest_framework import serializers
from rating.models import Rating
from menu.models import Menu
from django.db.models import Avg


class RatingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Rating
        fields = ("id", "rating", "user", "menu")