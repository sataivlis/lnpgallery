from django.urls import path, include
from django.conf.urls import url
from . import views

urlpatterns = [
  path('', views.gallery, name='gallery'),
  path('character/<int:pk>', views.chara_card, name='chara_card'),
]
