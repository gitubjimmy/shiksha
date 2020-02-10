from django.shortcuts import render
from django.http import HttpResponse
from django.utils import timezone
from datetime import timedelta
from rest_framework.decorators import api_view, parser_classes
from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.renderers import TemplateHTMLRenderer
from rest_framework.views import APIView
from .settings import RESTAURANTS, EN_COLLEGE_NAME, JWT_SECRET
from meals.models import Menu, Restaurant, College, Review
from meals.serializers import RestaurantSerializer, ReviewSerializer, MenuSerializer

import jwt
import time
import os


@api_view(['GET'])
def menus(request):
    college = College.objects.get(en_name=EN_COLLEGE_NAME)
    today = timezone.localtime(timezone.now()).date()
    tomorrow = (timezone.localtime(timezone.now()).today() + timedelta(days=1)).date()
    today_menus = MenuSerializer(Menu.objects.filter(restaurant__college=college, date=today), many=True).data
    tomorrow_menus = MenuSerializer(Menu.objects.filter(restaurant__college=college, date=tomorrow), many=True).data
    menu = {'today': {'date': today.__str__(), 'menus': today_menus},
            'tommorow': {'date': tomorrow.__str__(), 'menus': tomorrow_menus}}
    return Response(date=menu)

@api_view(['POST'])
def review(request):
    encoded = request.body.decode('utf8')
    decoded_review = {}
    try:
        decoded_review = jwt.decode(encoded, JWT_SECRET, algorithms=['HS256'])
    except:
        return Response(
            {'message': 'Signature verification failed'},
            status=status.HTTP_400_BAD_REQUEST
        )

    review_data = {
        'meal_id': decoded_review.get('meal_id'),
        'score': decoded_review.get('score'),
        'device': decoded_review.get('device'),
        'device_type': decoded_review.get('device_type'),
    }
    review_count_limit = 6
    if Review.objects.today_count(decoded_review.get('device')) >= review_count_limit:
        return Response(
            {'message': 'reviews limited to 6 times a day per device'},
            status=status.HTTP_400_BAD_REQUEST
        )

    try:
        review = Review.object.create(**review_data)
    except:
        return Response(
            {'message': 'review data invalid'},
            status = status.HTTP_400_BAD_REQUEST
        )

    return Response(data=ReviewSerializer(review).data)

@api_view(['GET'])
def restaurants(request):
    college = College.objects.get(en_name = EN_COLLEGE_NAME)
    restaurants = Restaurant.objects.filter(college=college)
    return Response(RestaurantSerializer(restaurants, many=True).data)

class PrivacyPolicy(APIView):
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'privacy_policy.html'

    def get(self, request):
        return Response()
