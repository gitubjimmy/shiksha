from django.contrib import admin
from .models import Restaurant, Review, Menu, Meal, College

admin.site.register(Restaurant)
admin.site.register(Review)
admin.site.register(Menu)
admin.site.register(Meal)
admin.site.register(College)

# Register your models here.
