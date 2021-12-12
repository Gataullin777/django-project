from django_filters import rest_framework as filters

# date__lte
# created_at_before=2021-12-10
# creator=1

class AdvertisementFilter(filters.FilterSet):
    """Фильтры для объявлений."""
    creator = filters.NumberFilter(field_name='creator_id', lookup_expr='exact')
    created_at_before = filters.DateFromToRangeFilter(field_name='created_at', lookup_expr='lte')

