from django.urls import path

from api import views

from rest_framework.routers import DefaultRouter

router=DefaultRouter()  #object

router.register("employee",views.EmployeeViewSet,basename="employee")

urlpatterns=[

]+router.urls