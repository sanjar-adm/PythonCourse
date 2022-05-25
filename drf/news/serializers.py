
from rest_framework import serializers
from .models import *

class NewsDetailSerializers(serializers.ModelSerializer):
    author = serializers.HiddenField(default=serializers.CurrentUserDefault())
    class Meta:
        model = News
        fields = '__all__'


class CargoSerializers(serializers.ModelSerializer):
    class Meta:
        model = Cargo
        fields = '__all__'