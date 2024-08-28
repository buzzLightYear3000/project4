from .common import CuisineSerializer
from recipes.serializers.common import RecipeSerializer

class PopulatedCuisineSerializer(CuisineSerializer):
    recipes = RecipeSerializer(many=True)