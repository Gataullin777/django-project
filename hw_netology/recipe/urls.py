from recipe import views
from django.urls import path

urlpatterns = [
    path('<dish>/', views.repice, name='recipe'),
    path('', views.main_menu, name='menu')

]