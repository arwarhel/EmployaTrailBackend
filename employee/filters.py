from rest_framework import filters


class AuthUserFilterBackend(filters.BaseFilterBackend):
    def filter_queryset(self, request, queryset, view):
        return queryset.filter(created_by=request.user)
