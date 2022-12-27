from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('chat/', include('app1.urls')),
    path('admin/', admin.site.urls),
]
