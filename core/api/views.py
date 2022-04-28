from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticatedOrReadOnly,IsAuthenticated
from rest_framework.authentication import TokenAuthentication
from rest_framework import status
from rest_framework import generics

from django_filters.rest_framework import DjangoFilterBackend

from core.models import Categories, Equipements
from core.api.serializers import CategoriesSerializer,EquipementsSerializer, EquipementsDetailSerializer
from core.api.paginations import CustomPagination


class CategoriesList(generics.ListCreateAPIView):
  authentication_classes = (TokenAuthentication,)
  permission_classes = (IsAuthenticated,)
  queryset = Categories.objects.all()
  serializer_class = CategoriesSerializer
  pagination_class = CustomPagination
  filter_backends = [DjangoFilterBackend]
  filterset_fields = ['parent__id']

class CategoriesDetails(APIView):
  authentication_classes = (TokenAuthentication,)
  permission_classes = (IsAuthenticated,)


  def get(self, request, pk):
    try: 
      category = Categories.objects.get(pk=pk)
    except Categories.DoesNotExist:
      return Response({'error':'Category not found'}, status=status.HTTP_404_NOT_FOUND)

    serializer = CategoriesSerializer(category)
    return Response(serializer.data)
  
  def put(self, request, pk):
    try: 
      category = Categories.objects.get(pk=pk)
    except Categories.DoesNotExist:
      return Response({'error':'Category not found'}, status=status.HTTP_404_NOT_FOUND)

    serializer = CategoriesSerializer(category, data=request.data)
    if serializer.is_valid():
      serializer.save()
      return Response(serializer.data)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

  def delete(self, request, pk):
    category = Categories.objects.get(pk=pk)
    category.delete()
    return Response(status=status.HTTP_204_NO_CONTENT)


class EquipementsList(generics.ListCreateAPIView):
  authentication_classes = (TokenAuthentication,)
  permission_classes = (IsAuthenticated,)

  serializer_class = EquipementsSerializer
  pagination_class = CustomPagination

  """Customise query set for filtering data by range of quantity"""
  filter_backends = (DjangoFilterBackend, )
  filter_fields = ('quantity',)
  
  def get_queryset(self):
      queryset = Equipements.objects.all()
      quantity_min = self.request.query_params.get('quantity_min', '')
      quantity_max = self.request.query_params.get('quantity_max', '')

      if( quantity_max and quantity_min):
          queryset = queryset.filter(quantity__gt=quantity_min,
                                      quantity__lt=quantity_max)
      return queryset


class EquipementsDetails(APIView):
  authentication_classes = (TokenAuthentication,)
  permission_classes = (IsAuthenticated,)
  
  def get(self, request, pk):
    try: 
      category = Equipements.objects.get(pk=pk)
    except Equipements.DoesNotExist:
      return Response({'error':'Category not found'}, status=status.HTTP_404_NOT_FOUND)

    serializer = EquipementsDetailSerializer(category)
    return Response(serializer.data)
  
  def put(self, request, pk):
    try: 
      category = Equipements.objects.get(pk=pk)
    except Equipements.DoesNotExist:
      return Response({'error':'Category not found'}, status=status.HTTP_404_NOT_FOUND)

    serializer = EquipementsSerializer(category, data=request.data)
    if serializer.is_valid():
      serializer.save()
      return Response(serializer.data)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

  def delete(self, request, pk):
    category = Equipements.objects.get(pk=pk)
    category.delete()
    return Response(status=status.HTTP_204_NO_CONTENT)