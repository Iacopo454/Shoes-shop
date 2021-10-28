from django.urls import path
from . import views

app_name = 'review'

urlpatterns = [
    path('', views.order_view, name='index'),
    path('submit_review/', views.submit_review, name='submit_review'),
    path('<str:order_number>/', views.order_details, name='order_details'),

]