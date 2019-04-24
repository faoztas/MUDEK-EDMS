# Django
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

# Local
from Mudek.views import login_redirect

urlpatterns = [
    # Admin Panel
    path('admin/', admin.site.urls),

    # Login Screeen
    path('', login_redirect, name='login_redirect'),

    # Edms App urls include
    path('edms/', include('edms.urls'))

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
