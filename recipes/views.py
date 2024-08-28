from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.exceptions import PermissionDenied
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly
from .models import Recipe
from .serializers.common import RecipeSerializer
from .serializers.populated import PopulatedRecipeSerializer
from utils.decorators import handle_exceptions
from utils.permissions import IsOwnerOrReadOnly

# Path for this view: /books/
class RecipeListCreateView(APIView):
    permission_classes = [IsAuthenticated]

    # Index Route
    @handle_exceptions
    def get(self, request):
        recipes = Recipe.objects.all() # Model.find() equivalent
        serialized_recipes = RecipeSerializer(recipes, many=True) # if we make a request that will return multiple results, remember to use many=True
        return Response(serialized_recipes.data)

    # Create Route
    @handle_exceptions
    def post(self, request):
        request.data['owner'] = request.user.id
        recipe_to_create = RecipeSerializer(data=request.data)

        if recipe_to_create.is_valid():
            # Data is valid
            recipe_to_create.save()
            return Response(recipe_to_create.data, 201)
        
        # An Error occurred during validation
        print('Validation error:', recipe_to_create.errors)
        return Response(recipe_to_create.errors, 400)
        


# Path for this view: /books/<int:id>/
class RecipeRetrieveUpdateDestroyView(APIView):
    permission_classes = [IsOwnerOrReadOnly]

    # Retrieve
    # Method: GET
    @handle_exceptions
    def get(self, request, pk):
        book = Recipe.objects.get(pk=pk)
        serialized_recipe = PopulatedRecipeSerializer(book)
        return Response(serialized_recipe.data)

    # Update
    # Method: PUT
    @handle_exceptions
    def put(self, request, pk):
        recipe_to_update = Recipe.objects.get(pk=pk)

        # After querying the book, we want to ensure the user making the request owns the book
        self.check_object_permissions(request, recipe_to_update)

        serialized_recipe = RecipeSerializer(recipe_to_update, data=request.data, partial=True)
        if serialized_recipe.is_valid():
            serialized_recipe.save()
            return Response(serialized_recipe.data)
        return Response(serialized_recipe.errors, 400)

    # Destroy
    # Method: DELETE
    @handle_exceptions
    def delete(self, request, pk):
        recipe_to_delete = Recipe.objects.get(pk=pk)

        # After querying the book, we want to ensure the user making the request owns the book
        self.check_object_permissions(request, recipe_to_delete)
            
        recipe_to_delete.delete()
        return Response(status=204)