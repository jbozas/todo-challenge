import django_filters
from .models import Task


class TaskFilter(django_filters.FilterSet):
    created_at__gte = django_filters.DateTimeFilter(
        field_name="created_at", lookup_expr="gte", label="Created After"
    )
    created_at__lte = django_filters.DateTimeFilter(
        field_name="created_at", lookup_expr="lte", label="Created Before"
    )
    content = django_filters.CharFilter(
        field_name="content", lookup_expr="icontains", label="Content Contains"
    )

    class Meta:
        model = Task
        fields = [
            "completed",
            "created_at__gte",
            "created_at__lte",
            "content",
        ]
