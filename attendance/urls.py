from rest_framework.routers import DefaultRouter

from .views import AttendanceViewSet

router = DefaultRouter()
router.register('attendance', AttendanceViewSet, basename='attendance')

app_name = "attendance"

urlpatterns = router.urls
