from rest_framework.viewsets import ModelViewSet
from rest_framework.filters import OrderingFilter
from rest_framework.response import Response
from rest_framework import status

from .models import Advertisement
from .serializers import AdSerializer


class AdViewSet(ModelViewSet):
    serializer_class = AdSerializer
    queryset = Advertisement.objects.all()
    filter_backends = [OrderingFilter]
    ordering_fields = ['price', 'created']

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        return Response(
            f'Created object has an id {serializer.data["id"]}',
            status=status.HTTP_201_CREATED)
