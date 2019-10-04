from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('exercise/<int:year>/<int:e_type>/<int:page_id>/',
         views.exercise,
         name='exercise'),
    path('answer/<int:year>/<int:e_type>/<int:page_id>/', views.answer, name='answer'),
    path('judge/<int:year>/<int:e_type>/', views.judge, name='judge'),
    path('top/', views.top, name='top'),
]
