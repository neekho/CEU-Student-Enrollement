from typing import Any
from django.forms.models import BaseModelForm
from django.http import HttpRequest, HttpResponse, HttpResponseRedirect, JsonResponse
from django.shortcuts import redirect, render


# for login and logout
from django.contrib.auth.views import LoginView, LogoutView


# for views that require authentication
from django.contrib.auth.mixins import LoginRequiredMixin


# url redirection
from django.urls import reverse_lazy

# models
from .models import Student


# views 
from django.views import View
from django.views.generic import DetailView, DeleteView, CreateView, UpdateView



# making requests
import requests
import json


# forms
from . forms import StudentSearch, StudentForm


class MyLoginView(LoginView):
    template_name = 'student/login.html'

    def form_valid(self, form):
        response = super().form_valid(form)
    
        return response


class MyLogoutView(LogoutView):
    template_name = 'student/logout.html'


def get_student(request, student_id):

    url = f'http://localhost:8000/api/cbv/student/{student_id}'

    response = requests.get(url)


    if response.status_code == 200:

        print(response.url, response.status_code)
        print(json.dumps(response.json(), indent=5))

        return response.json()


    else:
        return JsonResponse({'message': 'Not found or ID is non existing'})


class HomeView(LoginRequiredMixin, View):
    template_name ='student/home.html'


    def get(self, request, *args, **kwargs):
        '''
            Get all students from DB
        
        '''
        # Your logic for handling GET requests (e.g., rendering the home page)

        url = f'http://localhost:8000/api/cbv/students/'

        response = requests.get(url)

        if response.status_code == 200:
            data = response.json()
            print(data)
            print(response.url)
            print(response.status_code)
        
            return render(request, self.template_name, context={'students': data})
        
        else:
            print('ERROR' * 10)
            print(f"Error: {response.status_code}, {response.text}")
            return render(request, self.template_name, context={'error': response.text})
        

    def post(self, request, *args, **kwargs):
        

        search = StudentSearch(request.POST)
        print('post...')

        if search.is_valid():
            print('search valid')
            student_id = search.cleaned_data['student_id']
            student_search = get_student(request, student_id)

            print(student_search)

            return render(request, self.template_name, context={'student_search': student_search, 'student_search_form': search})
        
        else:
            search = StudentSearch()
            print('not val')
            return render(request, self.template_name, context={'student_search_form': search})



class StudentCreateView(LoginRequiredMixin, CreateView):
    
    model = Student
    form_class = StudentForm
    template_name = 'student/create_student.html'
    success_url = reverse_lazy('home')  # Set the URL to redirect to after successful creation

    def form_valid(self, form):

        form.instance.creator = self.request.user
        response = super().form_valid(form)

        # For example, if your DRF API endpoint is '/api/cbv/students/'z
        api_url = 'http://localhost:8000/api/cbv/students/'
        print(form.cleaned_data)
        response_api = requests.post(api_url, data=form.cleaned_data)

        if response_api.status_code == 201:  # Successful creation status code
            return response  # Redirect to the success URL
        else:

            # Handle error, for example, by displaying an error message
            return render(self.request, 'student/error_page.html', {'error_message': 'Failed to create student'})


    


class StudentDetailView(LoginRequiredMixin, DetailView):
   
    template_name = 'student/detail.html'  # Create this template in your templates directory
    context_object_name = 'student'  # This is the variable name available in the template


    def get_object(self, queryset=None):
        # Fetch student data from DRF API using the student ID from the URL
        student_id = self.kwargs.get('pk')
        print(student_id)
        api_url = f'http://localhost:8000/api/cbv/student/{student_id}/'
        response = requests.get(api_url)

        if response.status_code == 200:
                
            return response.json()
        else:
            pass




class StudentDeleteView(LoginRequiredMixin, DeleteView):


    template_name = 'student/confirm_delete.html'
    context_object_name = 'student'
    success_url = reverse_lazy('home')  # Provide the URL to redirect to after deletion

    
    def get_object(self, queryset=None):
        # Instead of using queryset, fetch the student data from DRF API using the student ID from the URL
        student_id = self.kwargs.get('pk')
        api_url = f'http://localhost:8000/api/cbv/student/{student_id}/'
        response = requests.get(api_url)

        if response.status_code == 200:
            student_data = response.json()
            return student_data
        else:
            # Handle error, for example, redirect to a custom error page
            pass

    def get_context_data(self, **kwargs):
        # Properly structure the context data as a dictionary
        context = super().get_context_data(**kwargs)
        context[self.context_object_name] = self.get_object()
        return context
    

    def form_valid(self, form):

        student = self.get_object()  # Fetch student data using the overridden get_object method

        api_url = f'http://localhost:8000/api/cbv/student/{student["id"]}/'
        response = requests.delete(api_url)

        if response.status_code == 204:  # Successful deletion status code
            return HttpResponseRedirect(self.success_url)
        else:
            # Handle error, for example, redirect to a custom error page
            pass




class StudentUpdateView(UpdateView):

    model = Student
    form_class = StudentForm
    template_name = 'student/update.html'


    # no code provided with update feature