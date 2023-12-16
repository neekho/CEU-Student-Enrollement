from django.urls import path

from . views import (MyLoginView, MyLogoutView, HomeView, StudentDetailView, StudentDeleteView, StudentCreateView, StudentUpdateView)


urlpatterns = [

    path('home/', HomeView.as_view(), name='home'),

    path('add/', StudentCreateView.as_view(), name='add_student'),

    path('student/<str:pk>/', StudentDetailView.as_view(), name='student_detail'),

    path('update/<str:pk>/', StudentUpdateView.as_view(), name='student_update'),


    path('delete/<str:pk>/', StudentDeleteView.as_view(), name='student_delete'),


    path('login/', MyLoginView.as_view(), name='login'),

    path('logout/', MyLogoutView.as_view(next_page='/login/'), name='logout'),



]