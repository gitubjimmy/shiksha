from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^menus/$', views.menus),
    url(r'^review/$', views.review),
    url(r'^restaurants/$', views.restaurants),
    url(r'^privacy_policy/', views.PrivacyPolicy.as_view()),
]