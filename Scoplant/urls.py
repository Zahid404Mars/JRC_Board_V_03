"""Scoplant URL Configuration

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
from django.conf import settings
from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.contrib.auth.views import LogoutView


urlpatterns = [
    path('', include('ScoplantUserPanel.urls')),
    path('', include('ScoplantAccounts.urls')),
    path('admin/', admin.site.urls),
    path("logout/", LogoutView.as_view(), name="logout"),
]
admin.site.index_title = "JRC_Board_V-03"
admin.site.site_header = "JRC_Board_V-03 Admin"
admin.site.site_title  = " Site Title JRC_Board_V-03"


# 404 Error Handler Custom Setting
handler404 = 'ScoplantUserPanel.views.error_404_view'

# 500 Error Handler Custom Setting
handler500 = 'ScoplantUserPanel.views.error_500_view'

if settings.DEBUG:
    # add root static files
    urlpatterns = urlpatterns + \
        static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    # add media static files
    urlpatterns = urlpatterns + \
        static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
