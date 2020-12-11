from rest_framework import serializers
from.models import RestModel

class RestModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = RestModel
        fields = '__all__'