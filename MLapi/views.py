from django.shortcuts import render

from rest_framework.response import Response
from rest_framework.views import APIView

from rest_framework import generics
from rest_framework import viewsets

from .models import *
from .serializers import *

from MLapi import ML
# Create your views here.

class index(APIView):
    def get(self,request):
        endpoints={
            "Home":"ML api"
        }
        return Response(endpoints)

class TitanicView(viewsets.ModelViewSet):
    queryset = Titanic.objects.all()
    serializer_class = TitanicSerializer

    def create(self,request,*args,**kwargs):
        viewsets.ModelViewSet.create(self,request,*args,**kwargs)
        obj=Titanic.objects.latest('id')
        survived=ML.pred(obj)
        return Response({'status':'Success','Survived':survived})
