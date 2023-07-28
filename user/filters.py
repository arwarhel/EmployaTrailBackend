from rest_framework import filters


class AttendanceUserFilterBackend(filters.BaseFilterBackend):
    def filter_queryset(self, request, queryset, view):
        user = request.user
        return queryset.filter(user=user)
