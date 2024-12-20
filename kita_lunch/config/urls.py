"""config URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from django.contrib import admin
from django.urls import path
from app import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.TopView.as_view(), name="top"),
    path('Stores/', views.StoreListView.as_view(), name="list"),
    path('area/<int:area_id>/', views.area_store_list, name='area_detail'),
    path('area/<int:area_id>/stores/', views.area_store_list, name='area_store_list'),
    # path('area/<int:area_id>/stores/<int:store_id>/', views.store_detail, name='store_detail'),
    path('store/<int:area_id>/<int:store_id>/',views.store_detail,name='store_detail'),
    # path('stores/', views.area_store_list, name='area_store_list'),
    # path('area/<int:area_id>/', views.AreaStoreListView.as_view(), name='area_detail'),
]

from django.conf import settings
from django.conf.urls.static import static

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)