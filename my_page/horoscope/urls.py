from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='horoscope-index'),
    path('<int:znak_zodiac>', views.get_info_about_sing_zodiac_by_now),
    path('<str:znak_zodiac>', views.get_info_about_sing_zodiac, name='horoscope-name'),

]
