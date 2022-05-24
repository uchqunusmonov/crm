from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('accounts.urls')),
    path('', include('dashboard.urls')),
    path('', include('tasks.urls')),
    path('', include('email_crm.urls')),
    #email Urls
    path('chat/', include('chat.urls')),
    #email API Urls
    path('api/email/', include('email_crm.api.urls')),

    
    # api

    path('api/chat/', include('chat.api.urls')),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
