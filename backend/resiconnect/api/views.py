from rest_framework import generics
from .models import Apartment, Resident, Post
from rest_framework import viewsets
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import ApartmentSerializer, ResidentSerializer, PostSerializer, PostDetailSerializer


class PostListView(generics.ListCreateAPIView):
    def get_serializer_class(self):
        if self.request.method == 'GET':
            return PostDetailSerializer
        return PostSerializer

    def get_queryset(self):
        queryset = Post.objects.all().order_by('-created_at')
        resident_id = self.request.query_params.get('resident', None)
        apartment_id = self.request.query_params.get('apartment', None)
        if resident_id is not None:
            queryset = queryset.filter(resident__id=resident_id)
        elif apartment_id is not None:
            queryset = queryset.filter(resident__apartment__id=apartment_id)
        return queryset


# View for retrieving, updating, or deleting a post

class PostDetailView(generics.RetrieveUpdateDestroyAPIView):
    def get_serializer_class(self):
        if self.request.method == 'GET':
            return PostDetailSerializer
        return PostSerializer

    queryset = Post.objects.all()


class ApartmentViewSet(viewsets.ModelViewSet):
    queryset = Apartment.objects.all()
    serializer_class = ApartmentSerializer


class ResidentViewSet(viewsets.ModelViewSet):
    queryset = Resident.objects.all()
    serializer_class = ResidentSerializer

class ResidentByApartment(generics.ListAPIView):
    serializer_class = ResidentSerializer

    def get_queryset(self):
        apartment_id = self.kwargs['apartment_id']
        return Resident.objects.filter(apartment_id=apartment_id)