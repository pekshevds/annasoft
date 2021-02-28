
from django.contrib import admin
from django.urls import path
from django.urls import include


from django.conf.urls.static import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf import settings

urlpatterns = [    
    path('', include('baseapp.urls')),
    path('crm/', include('crmapp.urls')),
    path('admin/', admin.site.urls),
    path('auth/', include('authapp.urls')),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += staticfiles_urlpatterns()