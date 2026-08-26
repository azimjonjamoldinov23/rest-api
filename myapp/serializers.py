from rest_framework.serializers import ModelSerializer
from myapp.models import Students

class Studentsserializers(ModelSerializer):
    class Meta:
        model = Students
        fields = ['id','name', 'fam','yosh',]

class addStudentsserializers(ModelSerializer):
    class Meta:
        model = Students
        fields = ['id','name', 'fam','yosh','kurs','yonalish',]