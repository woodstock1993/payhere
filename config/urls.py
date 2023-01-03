from config import settings

from django.urls import path, include

from rest_framework import permissions

from drf_yasg import openapi
from drf_yasg.views import get_schema_view


urlpatterns = [
    path("api/", include("apps.member.urls")),
    path("api/", include("apps.post.urls")),
]

if settings.DEBUG:
    schemal_url_patterns = [
        path("api/", include("apps.member.urls")),
        path("api/", include("apps.post.urls")),
    ]

    schema_view = get_schema_view(
        openapi.Info(
            title="payhere API",
            default_version="v1",
            description="payhere assignment",
        ),
        public=True,
        permission_classes=[permissions.AllowAny],
        patterns=schemal_url_patterns
    )

    urlpatterns += [
        path(
            'swagger<str:format>',
            schema_view.without_ui(cache_timeout=0),
            name='schema-json',
        ),
        path(
            'swagger/',
            schema_view.with_ui("swagger", cache_timeout=0),
            name='schema-swagger-ui',
        ),
        path(
            "docs/",
            schema_view.with_ui('redoc', cache_timeout=0),
            name='schema-redoc',
        )
    ]
    