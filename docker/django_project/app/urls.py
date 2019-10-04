from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('exercise/<int:year>/<str:type>/<int:page_id>/',
         views.exercise,
         name='exercise'),
    path('answer/<int:year>/<str:type>/<int:page_id>/', views.answer, name='answer'),
    path('judge/', views.judge, name='judge'),
    path('top/', views.top, name='top'),
]
