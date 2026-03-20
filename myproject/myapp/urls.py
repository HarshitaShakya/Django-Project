from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('member/add/', views.add_member, name='member_add'),
    path('member/<int:pk>/update/', views.update_member, name='member_update'),
    path('member/<int:pk>/delete/', views.delete_member, name='member_delete'),
]