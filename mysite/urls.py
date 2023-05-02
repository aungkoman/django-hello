
from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('tdl/', include('tdl.urls')),
    path('admin/', admin.site.urls),
]