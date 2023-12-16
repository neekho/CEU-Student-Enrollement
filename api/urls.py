from django.urls import path

from . import views


urlpatterns = [

  

    path('cbv/students/', views.StudentsView.as_view()),

    path('cbv/student/<str:pk>/', views.StudentDetailView.as_view()),

    path('users/', views.UsersView.as_view()),

    
    path('user/<int:pk>/', views.UserDetail.as_view())



]


