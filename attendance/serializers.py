from rest_framework import serializers

from .models import Attendance, Location
from user.models import AuthUser
from user.serializers import AuthUserSerializer


class LocationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Location
        fields = ('place', 'lat', 'lng')


class AttendanceSerializer(serializers.ModelSerializer):

    user = serializers.SerializerMethodField()
    location = LocationSerializer()

    def get_user(self, instance):
        user_dictionary = self.context.get('user_dictionary', True)

        if user_dictionary:
            return {
                "id": instance.user.id,
                "username": instance.user.username,
                "email": instance.user.email,
                "first_name": instance.user.first_name,
                "last_name": instance.user.last_name,
            }
        else:
            return instance.user.id

    class Meta:
        model = Attendance
        # fields = '__all__'
        fields = ('user', 'location', 'type', 'datetime')

    def create(self, validated_data):
        # Extract location data from validated_data
        location_data = validated_data.pop('location')

        # Create the location object
        location = Location.objects.create(**location_data)

        # Add the location object to validated_data
        validated_data['location'] = location

        # Create the Attendance object
        attendance = Attendance.objects.create(**validated_data)

        return attendance

    def to_internal_value(self, data):
        user_id = data.pop('user_id')  # Extract user_id from request data

        # retrieve user if already exists
        user = AuthUser.objects.get(id=user_id)

        # Update the data dictionary with the user
        data['user'] = user

        # Return the updated data dictionary
        return data
