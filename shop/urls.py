from django.conf.urls.static import static
from django.urls import path,include
from django.contrib import admin
from shop import settings


urlpatterns = [
                  path('', include('store.urls')),
                  path('', include('accounts.urls')),
                  path('admin/', admin.site.urls),
              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
