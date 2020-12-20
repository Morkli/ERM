import django_filters
from .models import Members


class MembersFilter(django_filters.FilterSet):
    Full_name = django_filters.CharFilter(lookup_expr='icontains')

    class Meta:
        model = Members
        fields = ['Full_name', 'Gender', 'Dues_Payment', 'Operation_Mode']
