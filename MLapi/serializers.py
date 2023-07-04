from rest_framework import serializers
from .models import *

class TitanicSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model=Titanic
        fields=['PassengerId','Pclass','Name','Sex','Age','Sibsp','Parch','Ticket','Fare','Cabin','Embarked']