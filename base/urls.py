from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('doctorlist/<int:pk>/',views.doctorList,name='doclist'),
    path('doctordetails/<int:pk>/',views.docDetails,name='docDetails'),
    path('select-date/',views.selectdate,name='selectdate'),
]
