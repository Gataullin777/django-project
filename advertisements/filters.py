from django_filters import rest_framework as filters


# created_at_before=2021-12-10
# creator=1
from advertisements.models import Advertisement


class AdvertisementFilter(filters.FilterSet):
    """Фильтры для объявлений."""
    creator = filters.NumberFilter(field_name='creator_id', lookup_expr='exact')
    created_at = filters.DateFromToRangeFilter()
    class Meta:
        model = Advertisement
        fields = ['creator_id', 'created_at']

