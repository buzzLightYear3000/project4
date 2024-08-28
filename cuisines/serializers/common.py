from rest_framework.serializers import ModelSerializer
from ..models import Cuisine

class CuisineSerializer(ModelSerializer):
    class Meta:
        model = Cuisine
        fields = '__all__'