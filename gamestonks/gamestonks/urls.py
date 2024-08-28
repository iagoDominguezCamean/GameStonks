from django.contrib import admin
from django.conf import settings
from django.urls import include, path
from django.conf.urls.static import static

urlpatterns = [
    path('', include('store.urls')),
    path('admin/', admin.site.urls),
]
