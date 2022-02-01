
from django.forms.models import ModelForm
from .models import Student

 
class registerform(ModelForm):
  class Meta:
    model = Student
    fields = ['Fullname','Photo','Course','Grade','Gender']

