# Django
from django.urls import path, include

# Third-Party
from rest_framework import routers

# Local Django
from users.api_views import UserViewSet
from edms.api_views import (
    LessonViewSet, ExamViewSet, Other_DocumentViewSet,
    Requested_DocumentsViewSet
)
from core.api_views import ContactViewSet


router_L = routers.DefaultRouter()

LIST_LINKS = [
    (r'contacts', ContactViewSet, 'contacts'),
    (r'users', UserViewSet, 'users'),
    (r'lessons', LessonViewSet, 'lessons'),
    (r'exams', ExamViewSet, 'exams'),
    (r'other-documents', Other_DocumentViewSet, 'other-documents'),
    (r'request-documents', Requested_DocumentsViewSet, 'request-documents'),
]

for router in LIST_LINKS:
    router_L.register(router[0], router[1], base_name=router[2])


urlpatterns = [
    path('api/', include(router_L.urls)),
]
