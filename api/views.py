from django.http import Http404
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status

#CLASS BASED VIEWS
from rest_framework.views import APIView
from rest_framework import generics


# Models
from django.contrib.auth.models import User
from student.models import Student


# Serializers
from . serializers import StudentSerializer, UserSerializer


# Authentication/Permissions 
from rest_framework import permissions



class UsersView(generics.ListAPIView):
    '''
        Working with multiple User instances,
        LIST ONLY
    
    '''
    queryset = User.objects.all()
    serializer_class = UserSerializer

class UserDetail(generics.RetrieveAPIView):
    

    '''
        Single/Detailed view of users
    '''
    queryset = User.objects.all()
    serializer_class = UserSerializer
        

class StudentsView(APIView):

    def get(self, request):
        student = Student.objects.all()
        print('FROM class based view')

        serializer = StudentSerializer(student, many=True)

        return Response(serializer.data)
    
    def post(self, request):
        print('from cbv post method')
        serializer = StudentSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save(creator=self.request.user)
        
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        else:
            error_response = {"errors": "request failed!", "details": serializer.errors}
            print(serializer.errors)
            return Response(error_response, status=status.HTTP_400_BAD_REQUEST)

    

class StudentDetailView(APIView):
    def get_object(self, pk):
        try:
            return Student.objects.get(id=pk)
        except Student.DoesNotExist:
            print('not found')
            raise Http404("Student not found")

    def get(self, request, pk):
        '''
            this method is for getting a single student from our db
            wherein pk is entered by the user.

            if the student or object does not exists,
            this will raise an http404      
        
        '''
        student = self.get_object(pk)

        serializer = StudentSerializer(student)

        return Response(serializer.data)
    
    def put(self, request, pk):
        # Updating of student
        student = self.get_object(pk)

        serializer = StudentSerializer(student, data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response({"message": "student updated"}, status=status.HTTP_202_ACCEPTED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    

    def delete(self, request, pk):
        student = self.get_object(pk)

        student.delete()

        return Response({"message": f"Student of {pk} was deleted."}, status=status.HTTP_204_NO_CONTENT)
    






