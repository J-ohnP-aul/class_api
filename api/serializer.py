from rest_framework import serializers
from .models import Student

class StudentSerializer(serializers.ModelSerializer):
  class Meta:
    model = Student
    fields = ['id', 'name', 'reg_no', 'phone', 'email', 'portfolio_link']