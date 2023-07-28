from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.decorators import action
from django.utils import timezone
from datetime import datetime
from django.db.models import Q

from user.permissions import IsAuthenticatedOrUserCreatedBy

from .models import Attendance
from .serializers import AttendanceSerializer

# Create a dictionary to map sorting options to field names
SORT_FIELD_MAPPING = {
    'datetime': 'datetime',
    # Add more options here if needed in the future
}


class AttendanceViewSet(viewsets.ModelViewSet):
    queryset = Attendance.objects.all()
    serializer_class = AttendanceSerializer
    permission_classes = [IsAuthenticatedOrUserCreatedBy]

    def get_queryset(self):
        queryset = super().get_queryset()

        if self.action == 'list' or self.action == 'list_search_attendance':
            if (self.request.user.is_superuser):
                queryset = queryset.filter(
                    Q(user__employee__created_by=self.request.user) | Q(user=self.request.user))
                # queryset = queryset.filter(
                #     user__employee__created_by=self.request.user)

            else:
                queryset = queryset.filter(user=self.request.user)

        return queryset

    def list(self, request, *args, **kwargs):
        queryset = self.get_queryset()

        user_id = request.data.get('user')
        if user_id:
            queryset = queryset.filter(user__id=user_id)

        # print("queryset : ", queryset)

        # checkin_location = request.data.get('checkin_location')
        # if checkin_location:
        #     queryset = queryset.filter(checkin_location=checkin_location)

        date_str = request.data.get('date')
        if date_str:
            try:
                # Parse the ISOString date to a datetime object
                date = datetime.strptime(date_str, "%Y-%m-%dT%H:%M:%SZ")
                # Filter the queryset to get all attendance records for the specified date
                queryset = queryset.filter(datetime__date=date.date())
            except ValueError:
                # Handle the case where the provided date is invalid
                return Response({"detail": "Invalid date format. Please provide a valid ISOString date."},
                                status=status.HTTP_400_BAD_REQUEST)

        # sorting options
        # Get the sort field and descending flag from the request data
        sortby = request.data.get('sortby')
        descending = request.data.get('descending')

        # Determine the field name for sorting using the SORT_FIELD_MAPPING dictionary
        sort_field = SORT_FIELD_MAPPING.get(sortby)

        # Perform sorting if a valid sort_field is found
        if sort_field:
            # Prepend '-' to the field name if descending is True
            sort_field = f'-{sort_field}' if descending else sort_field
            # Use the sort_field to order the queryset
            queryset = queryset.order_by(sort_field)

        serializer = self.get_serializer(queryset, many=True)
        # print(serializer.data)
        return Response(serializer.data)

    @action(methods=["get"], detail=False, url_path="user/(?P<user_id>[^/.]+)", url_name="list_user_attendance")
    def list_user_attendance(self, request, pk=None, user_id=None):
        queryset = self.get_queryset()
        if user_id:
            queryset = queryset.filter(user__id=user_id)
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)

    @action(methods=["post"], detail=False, url_path="search", url_name="list_search_attendance")
    def list_search_attendance(self, request, *args, **kwargs):
        print(request)
        return self.list(request, *args, **kwargs)
