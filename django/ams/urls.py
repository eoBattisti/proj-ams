from django.contrib import admin
from django.urls import path, include

from core.views import HomeRedirectView

urlpatterns = [
    path('', HomeRedirectView.as_view(), name='home'),
    path('admin/', admin.site.urls),
    path('accounts/', include('django.contrib.auth.urls')),
]
