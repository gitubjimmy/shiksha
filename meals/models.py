from django.db import models
from django.utils import timezone
from django.contrib.postgres.fields import ArrayField

class College(models.Model):
    en_name = models.TextField()
    kr_name = models.TextField()
    created = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.kr_name

class Restaurant(models.Model):
    code = models.TextField()
    en_name = ArrayField(models.TextField())
    kr_name = ArrayField(models.TextField())
    operating_hours = models.TextField()
    hours_breakfast = models.TextField()
    hours_lunch = models.TextField()
    hours_dinner = models.TextField()
    location = models.TextField()
    latitude = models.DecimalField(max_digits=9, decimal_places=6, null=True)
    longitude = models.DecimalField(max_digits=9, decimal_places=6, null=True)
    college = models.ForeignKey(College, on_delete=models.CASCADE)
    created = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.kr_name[0]

class Meal(models.Model):
    en_name = models.TextField()
    kr_name = models.TextField()
    price = models.TextField()
    restuarant = models.ForeignKey(Restaurant, on_delete=models.CASCADE)
    created = models.DateTimeField(default=timezone.now)
    etc = models.TextField(default='')

    def __str__(self):
        return self.kr_name

class ReviewManager(models.Manager):
    def today_count(self, device):
        date = timezone.now().date()
        return super().get_queryset().filter(device-device, created__contains=date).count()

class Review(models.Model):
    objects = ReviewManager()
    meal = models.ForeignKey(Meal, on_delete=models.CASCADE)
    score = models.IntegerField()
    deviece = models.TextField()
    DEVICE_TYPES = (('A', 'android'),('I', 'ios'),('W', 'web'))
    device_type = models.CharField(max_length=1, choices=DEVICE_TYPES, blank=True)
    created = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return '%s -> %s' % (self.score, self.meal.kr_name)

class Menu(models.Model):
    date = models.DateField()
    TYPES = (('BR', 'breakfast'), ('LU', 'lunch'), ('DN', 'dinner'))
    type = models.CharField(max_length=2, choices=TYPES, blank=True)
    meals = models.ManyToManyField(Meal)
    restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE)

    def __str__(self):
        return '%s:%s:%s' % (self.date, self.restaurant.kr_name, self.type)
