# Django
from django.urls import path

# Local Django
from .views import ContactView
app_name='core'

urlpatterns = [
   path('', ContactView.as_view(), name='contact'),
]
