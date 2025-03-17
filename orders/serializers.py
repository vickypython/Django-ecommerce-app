from django.contrib.auth.models import User,Group
from rest_framework import serializers
from .models import Notes
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model=Notes
        fields='__all__'

class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model=Group
        fields=['url','name']
    def validate_name(self,value):
        if value <0:
            raise serializers.ValidationError("name must be greater than 0")
data = {'name': 'Alice', 'age': 25}
serializer=UserSerializer(data=data)
if serializer.is_valid():
    serializer.save()
    print(serializer.data)