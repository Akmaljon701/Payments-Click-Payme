from django.contrib import admin
from django.urls import path
from payments.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('click_tolov/', ClickAPIView.as_view()),
    path('clickuz/', ClickView.as_view()),
]

