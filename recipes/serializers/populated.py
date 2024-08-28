from .common import RecipeSerializer
from cuisines.serializers.common import CuisineSerializer
from jwt_auth.serializers.common import UserSerializer

class PopulatedRecipeSerializer(RecipeSerializer):
    cuisines = CuisineSerializer(many=True)
    owner = UserSerializer()