from lunch.models import Student, Plan
from rest_framework.serializers import ModelSerializer, Serializer

class StudentSerializer(ModelSerializer):
    class Meta:
        model = Student
        fields = "__all__"

class PlanSerializer(ModelSerializer):
    class Meta:
        model = Plan
        fields = "__all__"

