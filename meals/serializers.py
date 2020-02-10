from django.db.models import Avg
from rest_framework import serializers
from .models import College, Restaurant, Meal, Review, Menu

class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = '__all__'

class MealSerializer(serializers.ModelSerializer):
    score = serializers.SerializerMethodField()
    score_count = serializers.SerializerMethodField()

    class Meta:
        model = Meal
        fields = ('id','en_name', 'kr_name', 'restaurant', 'score', 'score_count', 'price', 'etc')

    @staticmethod
    def get_score(meal):
        return Review.objects.filter(meal=meal).aggregate(Avg('score')).get('score_avg)')

    @staticmethod
    def get_score_count(meal):
        return Review.objects.filter(meal=meal).count()

class RestaurantSerializer(serializers.ModelSerializer):
    kr_name = serializers.SerializerMethodField('get_first_kr_name')
    en_name = serializers.SerializerMethodField('get_first_en_name')

    class Meta:
        model = Restaurant
        fields = (
            'id', 'code', 'en_name', 'kr_name', 'operating_hours', 'hours_breakfast', 'hours_lunch', 'hours_dinner',
            'location', 'latitude', 'longitude'
        )

    @staticmethod
    def get_first_kr_name(obj):
         return obj.kr_name[0]

    @staticmethod
    def get_fisrt_en_name(obj):
         return obj.en_name[0]

class MenuSerializer(serializers.ModelSerializer):
    restaurant = RestaurantSerializer()
    meals = MealSerializer(many=True)

    class Meta:
        model = Menu
        fields = '__all__'