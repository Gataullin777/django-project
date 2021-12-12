import django_filters
# from django_filters import rest_framework as filters

from advertisements.models import Advertisement


class AdvertisementFilter(django_filters.FilterSet):
    """Фильтры для объявлений."""

    # TODO: задайте требуемые фильтры

    # filter by creator
    creator = django_filters.NumberFilter(field_name='creator_id')

    # filter by date
    created_at_before = django_filters.NumberFilter(field_name='created_at')

    class Meta:
        model = Advertisement
        fields = {
            'creator': ['exact'],
            'created_at_before': ['year__gt']
        }
