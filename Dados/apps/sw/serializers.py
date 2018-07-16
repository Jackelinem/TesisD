from rest_framework import serializers
from rest_framework import User

class userSerializer(serializers.ModelField):
    class Meta:
        model = User
        fields= '__all__'