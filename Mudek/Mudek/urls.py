# Django
from django.contrib import admin
from django.conf import settings
from django.views.static import serve
from django.urls import path, include
from django.conf.urls.static import static

# Local Django
from Mudek.views import ActivationView, ResetPasswordView
from users.api_views import TokenCreateView

urlpatterns = [
    # Admin
    path('admin/', admin.site.urls),

    # Api
    path('', include('Mudek.api_urls')),

    # Token
    path('auth/login/', TokenCreateView.as_view(), name='login'),
    path('auth/', include('djoser.urls.authtoken')),

    # Activation and Password Operations
    path('activation/(<key>)/', ActivationView.as_view(), name='activation'),
    path(
        'reset-password/(<key>)/',
        ResetPasswordView.as_view(),
        name='reset-password'
    ),

    # Web
    path('', include('edms.urls'))
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
