from api.serializers import EmployeeSerializer,TaskSerializer

from rest_framework import viewsets

from api.models import Employee


class EmployeeViewSet(viewsets.ModelViewSet):

    serializer_class=EmployeeSerializer

    queryset=Employee.objects.all()