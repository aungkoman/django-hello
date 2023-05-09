
from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('', include('tdl.urls')),
    path('admin/', admin.site.urls),
    path('news/', include('news.urls')),
]