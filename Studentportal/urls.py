from django.contrib import admin
from django.urls import include, path
from rest_framework.schemas import get_schema_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/', include('data.urls')),
    path('api-auth/', include('rest_framework.urls')), # new url route
    path('api/v1/dj-rest-auth/', include('dj_rest_auth.urls')),
    path('api/v1/dj-rest-auth/registration/', include('dj_rest_auth.registration.urls')), # rest framework registration urls
    path('openapi', get_schema_view(
        title='Student portal API',
        description='An API for a student portal website',
        version='1.0.0'
    ), name='openapi-schema'),
]