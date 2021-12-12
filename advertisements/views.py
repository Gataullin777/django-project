from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet

from advertisements.filters import AdvertisementFilter
from advertisements.models import Advertisement
from advertisements.serializers import AdvertisementSerializer
from django_filters.rest_framework import DjangoFilterBackend



class AdvertisementViewSet(ModelViewSet):
    """ViewSet для объявлений."""

    # TODO: настройте ViewSet, укажите атрибуты для кверисета,
    #   сериализаторов и фильтров

    queryset = Advertisement.objects.all()
    serializer_class = AdvertisementSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_class = AdvertisementFilter



    def get_permissions(self):
        """Получение прав для действий."""

        if self.action in ["create", "update", "partial_update", "destroy"]:
            return [IsAuthenticated()]
        return []

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        request_user = request.user
        print()
        if request_user == instance.creator:
            instance.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST)






