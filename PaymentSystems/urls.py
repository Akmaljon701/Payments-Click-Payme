from django.contrib import admin
from django.urls import path
from payments.views import *

from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

schema_view = get_schema_view(
   openapi.Info(
      title="Click, Payme API",
      default_version='v1',
      description="Click, Payme to'lo'vlari uchun API",
      contact=openapi.Contact("Akmaljon Yoqubov <akmaljonyoqubov088@gmail.com>"),
   ),
   public=True,
   permission_classes=[permissions.AllowAny],
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('click_tolov/', ClickAPIView.as_view()),
    path('payme_tolov/', PaymeAPIView.as_view()),
    path('clickuz/', ClickView.as_view()),
    path('', PaycomView.as_view()),

    path('docs/', schema_view.with_ui('swagger', cache_timeout=0))
]

