from django.db import models
import uuid
from user.models import AuthUser


class Location(models.Model):
    id = models.UUIDField(
        primary_key=True, default=uuid.uuid4, editable=False)
    place = models.CharField(max_length=255, blank=True, null=True)
    lat = models.FloatField()
    lng = models.FloatField()

    def __str__(self):
        return self.place + "_" + str(self.lat) + "_" + str(self.lng)


class Attendance(models.Model):

    class AttendanceTypeChoices(models.IntegerChoices):
        CheckIn = 1
        CheckOut = 2

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    user = models.ForeignKey(
        AuthUser, on_delete=models.CASCADE, related_name='attendance')
    type = models.IntegerField(choices=AttendanceTypeChoices.choices)
    datetime = models.DateTimeField()
    location = models.ForeignKey(
        Location, on_delete=models.CASCADE, related_name='location')

    def __str__(self):
        return self.user.username + " ON " + str(self.datetime) + " AT " + self.location.__str__()
