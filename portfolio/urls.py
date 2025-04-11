from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('stage_1/', views.stage_1, name='stage_1'),
    path('stage_2/', views.stage_2, name='stage_2'),
    path('portfolio/', views.portfolio_page, name='portfolio_page'),
]
