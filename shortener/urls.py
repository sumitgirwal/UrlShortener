from django.urls import path
from . import views

urlpatterns = [
    path('', views.index,name='home'),
    path('<str:short_code>/', views.redirect_to_original, name='redirect'),
]
