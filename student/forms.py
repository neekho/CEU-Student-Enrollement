from django import forms


# import student models
from . models import Student

class StudentSearch(forms.Form):
    student_id = forms.CharField(label='enter student id..', widget=forms.Textarea)
    



class StudentForm(forms.ModelForm):

    '''
        For creation of a student, to be pass on to our POST API end point
    '''

    class Meta:
        model = Student
        fields = ['first_name', 'last_name','birth_date', 'course']  # Specify the fields you need in the form

    widgets = {
        'birth_date': forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}),
        'first_name': forms.TextInput(attrs={'class': 'form-control'}),
        'last_name': forms.TextInput(attrs={'class': 'form-control'}),
        'course': forms.TextInput(attrs={'class': 'form-control'}),
    }