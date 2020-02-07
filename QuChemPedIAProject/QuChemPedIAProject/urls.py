"""QuChemPedIAProject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/

Examples:
Function views:
1. Add an import: from my_app import views
2. Add a URL to urlpatterns: path('', views.home, name='home')

Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')

Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path(settings.MODE+'admin/', include('admin_qcpia.urls_admin_qcpia')),
    path(settings.MODE+'', include('common_qcpia.urls_common_qcpia')),
    path(settings.MODE+'accueil/', include('common_qcpia.urls_common_qcpia')),
    path(settings.MODE+'access/', include('query_qcpia.urls_query_qcpia')),
    path(settings.MODE+'import/', include('import_qcpia.urls_import_qcpia')),
    path(settings.MODE+'user/', include('user_qcpia.urls_user_qcpia')),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)+static(settings.DATA_DIR_URL, document_root=settings.DATA_DIR_ROOT)
