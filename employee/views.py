from rest_framework import viewsets
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from .models import Employee
from .serializers import EmployeeSerializer
from .filters import AuthUserFilterBackend


class EmployeeViewSet(viewsets.ModelViewSet):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer
    filter_backends = [AuthUserFilterBackend]
    lookup_field = 'id'

    def get_object(self):
        """Return the object for this view."""
        return get_object_or_404(self.queryset, user__id=self.kwargs["id"])

    def partial_update(self, request, *args, **kwargs):
        kwargs['partial'] = True
        instance = self.get_object()
        serializer = self.get_serializer(
            instance, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)

        return Response(serializer.data)
