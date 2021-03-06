"""server URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls.conf import re_path
from django.views.generic.base import RedirectView
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

from rest_framework.authtoken import views
from rest_framework import routers

from sensor_data.views import (
    HelloView,
    RecordViewSet,
    SensorDataViewSet,
    MeasurementTypeViewSet,
)

from users.views import login_request, logout_request, register_request

router = routers.SimpleRouter()
router.register("sensor-data", SensorDataViewSet)
router.register("measurements", MeasurementTypeViewSet)
router.register("records", RecordViewSet)

# For customizing admin panel
admin.site.site_header = "Patient Monitor System"
admin.site.index_title = "Database"
admin.site.site_title = "Admin Panel"

favicon_view = RedirectView.as_view(
    url="/static/assets/img/favicon.ico", permanent=True
)

urlpatterns = [
    re_path(r"^favicon\.ico$", favicon_view),
    path("admin/", admin.site.urls),
    path("hello/", HelloView.as_view(), name="hello"),
    path("api-token/", views.obtain_auth_token),
    path("api/", include(router.urls)),
    path("login/", login_request, name="login"),
    path("register/", register_request, name="register"),
    path("logout/", logout_request, name="logout"),
]
