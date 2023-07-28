from django.db import models
from user.models import AuthUser


class AuthUserOwnedEmployee(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(user=self.request.user)


class Employee(models.Model):
    user = models.OneToOneField(
        AuthUser, related_name='employee', on_delete=models.CASCADE)
    created_by = models.ForeignKey(
        AuthUser, on_delete=models.CASCADE, related_name='owner')
    phone = models.IntegerField(null=True, blank=True)
    designation = models.CharField(max_length=255, null=True, blank=True)
    mood = models.CharField(max_length=255, null=True, blank=True)

    objects = models.Manager()
    # employees = AuthUserOwnedEmployee()

    def __str__(self):
        return self.user.username
