from rest_framework import serializers

from user.models import AuthUser
from user.serializers import AuthUserSerializer

from attendance.serializers import AttendanceSerializer

from .models import Employee


class EmployeeSerializer(serializers.ModelSerializer):
    id = serializers.CharField(source='user.pk', read_only=True)
    username = serializers.CharField(source='user.username')
    email = serializers.CharField(source='user.email')
    first_name = serializers.CharField(source='user.first_name')
    last_name = serializers.CharField(source='user.last_name')
    password = serializers.CharField(source='user.password', write_only=True)
    role = serializers.CharField(source='user.role', read_only=True)
    attendance = serializers.SerializerMethodField()

    def get_attendance(self, instance):
        attendance_qs = instance.user.attendance.all()[:3]
        serializer = AttendanceSerializer(
            attendance_qs, many=True, read_only=True, context={'user_dictionary': False})
        return serializer.data

    class Meta:
        model = Employee
        fields = ('id', 'username', 'email', 'first_name', 'last_name', 'role',
                  'phone', 'designation', 'mood', 'attendance', 'password')

    def create(self, validated_data):
        # Assign the currently logged-in user as created_by
        request = self.context.get('request')
        if request and hasattr(request, 'user') and request.user.is_authenticated:

            user_data = validated_data['user']

            user = AuthUser.objects.create(
                username=user_data['username'],
                email=user_data['email'],
                first_name=user_data['first_name'],
                last_name=user_data['last_name'],
                role='employee'
            )
            user.set_password(user_data['password'])
            user.save()

            created_by = request.user

            phone = validated_data.get('phone', None)
            designation = validated_data.get('designation', None)
            mood = validated_data.get('mood', None)

            employee = Employee.objects.create(
                user=user, created_by=created_by, phone=phone, designation=designation, mood=mood)

            return employee

        return super().create(validated_data)

    def update(self, instance, validated_data):
        user_data = validated_data.pop('user', None)
        if user_data:
            user_serializer = AuthUserSerializer(
                instance.user, data=user_data, partial=True)
            user_serializer.is_valid(raise_exception=True)
            user_serializer.save()

        for attr, value in validated_data.items():
            setattr(instance, attr, value)
        instance.save()

        return instance
