from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Cuisine
from .serializers.common import CuisineSerializer
from .serializers.populated import PopulatedCuisineSerializer
from utils.decorators import handle_exceptions

# Index View
class CuisineListView(APIView):

    @handle_exceptions
    def get(self, request):
        cuisines = Cuisine.objects.all()
        serialized_cuisines = PopulatedCuisineSerializer(cuisines, many=True)
        return Response(serialized_cuisines.data)