# Third-Party
from rest_framework import viewsets, mixins

# Local Django
from edms.models import Lesson, Exam, Other_Document, Requested_Documents
from users.models import User
from edms.serializers import (
    LessonSerializer, LessonListSerializer, LessonRetrieveSerializer,
    LessonCreateSerializer, LessonUpdateSerializer, ExamSerializer,
    ExamListSerializer, ExamRetrieveSerializer, Other_DocumentListSerializer,
    ExamUpdateSerializer, Other_DocumentSerializer, ExamCreateSerializer,
    Other_DocumentRetrieveSerializer, Other_DocumentCreateSerializer,
    Other_DocumentUpdateSerializer, Requested_DocumentsSerializer,
    Requested_DocumentsListSerializer, Requested_DocumentsRetrieveSerializer,
    Requested_DocumentsCreateSerializer, Requested_DocumentsUpdateSerializer
)


class LessonViewSet(mixins.ListModelMixin,
                    mixins.CreateModelMixin,
                    mixins.RetrieveModelMixin,
                    mixins.UpdateModelMixin,
                    mixins.DestroyModelMixin,
                    viewsets.GenericViewSet):
    queryset = Lesson.objects.all()

    def get_queryset(self):
        if self.request.user.is_assistant_department_manager or self.request.user.is_department_manager or self.request.user.is_dean_manager:
            return self.queryset.all()
        elif self.request.user.is_academician:
            return self.queryset.filter(user=self.request.user)
        
        

    def get_serializer_class(self):
        if self.action == 'list':
            return LessonListSerializer
        elif self.action == 'create':
            return LessonCreateSerializer
        elif self.action == 'retrieve':
            return LessonRetrieveSerializer
        elif self.action == 'update':
            return LessonUpdateSerializer
        else:
            return LessonSerializer


class ExamViewSet(mixins.ListModelMixin,
                  mixins.CreateModelMixin,
                  mixins.RetrieveModelMixin,
                  mixins.UpdateModelMixin,
                  mixins.DestroyModelMixin,
                  viewsets.GenericViewSet):
    queryset = Exam.objects.all()

    def get_queryset(self):
        return self.queryset.filter(lesson__user=self.request.user)

    def get_serializer_class(self):
        if self.action == 'list':
            return ExamListSerializer
        elif self.action == 'create':
            return ExamCreateSerializer
        elif self.action == 'retrieve':
            return ExamRetrieveSerializer
        elif self.action == 'update':
            return ExamUpdateSerializer
        else:
            return ExamSerializer


class Other_DocumentViewSet(mixins.ListModelMixin,
                            mixins.CreateModelMixin,
                            mixins.RetrieveModelMixin,
                            mixins.UpdateModelMixin,
                            mixins.DestroyModelMixin,
                            viewsets.GenericViewSet):
    queryset = Other_Document.objects.all()

    def get_queryset(self):
        return self.queryset.filter(lesson__user=self.request.user)

    def get_serializer_class(self):
        if self.action == 'list':
            return Other_DocumentListSerializer
        elif self.action == 'create':
            return Other_DocumentCreateSerializer
        elif self.action == 'retrieve':
            return Other_DocumentRetrieveSerializer
        elif self.action == 'update':
            return Other_DocumentUpdateSerializer
        else:
            return Other_DocumentSerializer


class Requested_DocumentsViewSet(mixins.ListModelMixin,
                                 mixins.CreateModelMixin,
                                 mixins.RetrieveModelMixin,
                                 mixins.UpdateModelMixin,
                                 mixins.DestroyModelMixin,
                                 viewsets.GenericViewSet):
    queryset = Requested_Documents.objects.all()

    def get_queryset(self):
        return self.queryset.filter(lesson__user=self.request.user)

    def get_serializer_class(self):
        if self.action == 'list':
            return Requested_DocumentsListSerializer
        elif self.action == 'create':
            return Requested_DocumentsCreateSerializer
        elif self.action == 'retrieve':
            return Requested_DocumentsRetrieveSerializer
        elif self.action == 'update':
            return Requested_DocumentsUpdateSerializer
        else:
            return Requested_DocumentsSerializer
