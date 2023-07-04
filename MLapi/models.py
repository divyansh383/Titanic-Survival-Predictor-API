from django.db import models

# Create your models here.
class Titanic(models.Model):
    GENDER=[
        ("male","male"),
        ("female","female")
    ]
    EMBARKED=[
        ("S","S"),
        ("C","C"),
        ("Q","Q")
    ]
    Pid=[
        ("1","1"),
        ("2","2"),
        ("3","3")
    ]

    PassengerId=models.CharField(max_length=50)
    Pclass=models.IntegerField(default=0,choices=Pid)
    Name=models.CharField(max_length=50)
    Sex=models.CharField(max_length=50,choices=GENDER)
    Age=models.IntegerField()
    Sibsp=models.IntegerField()
    Parch=models.IntegerField()
    Ticket=models.CharField(max_length=50)
    Fare=models.FloatField()
    Cabin=models.CharField(max_length=50,null=True,blank=True)
    Embarked=models.CharField(max_length=50,choices=EMBARKED)
    Survived=models.IntegerField(null=True,blank=True)

    def to_dict(self):
        return {
            'PassengerId':self.PassengerId,
            'Survived':self.Survived,
            'Pclass':self.Pclass,
            'Name':self.Name,
            'Sex':self.Sex,
            'Age':self.Age,
            'SibSp':self.Sibsp,
            'Parch':self.Parch,
            'Ticket':self.Ticket,
            'Fare':self.Fare,
            'Cabin':self.Cabin,
            'Embarked':self.Embarked
        }
    
    def __str__(self):
        return self.Name