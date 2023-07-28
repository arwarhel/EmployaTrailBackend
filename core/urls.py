from django.contrib import admin
from django.urls import path, include
from django.views.generic.base import TemplateView
from drf_spectacular.views import SpectacularAPIView, SpectacularSwaggerView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', TemplateView.as_view(template_name="core/index.html")),
    # apis
    path('api-auth/', include('rest_framework.urls')),
    path('api/v1/', include('user.urls', namespace='user')),
    path('api/v1/', include('employee.urls', namespace='employee')),
    path('api/v1/', include('attendance.urls', namespace='attendance')),
    # docs
    path('api/v1/schema/', SpectacularAPIView.as_view(), name='schema'),
    path('api/v1/docs/', SpectacularSwaggerView.as_view(url_name='schema'),
         name='swagger-ui'),
]
