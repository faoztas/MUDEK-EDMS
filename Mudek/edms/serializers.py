# Standart Library
import datetime

# Third-Party
from rest_framework import serializers

# Django
from django.utils.translation import ugettext_lazy as _

# Local Django
from edms.models import(
    Lesson, Exam, Other_Document, Requested_Documents
)


class LessonSerializer(serializers.ModelSerializer):

    class Meta:
        model = Lesson
        fields = (
            'id',
            'user',
            'lesson_name',
            'lesson_content',
            'lesson_content_file',
            'lesson_notes',
            'lesson_notes_file'
        )


class LessonListSerializer(LessonSerializer):

    class Meta:
        model = Lesson
        fields = (
            'id',
            'user',
            'lesson_name',
            'lesson_content',
            'lesson_content_file',
            'lesson_notes',
            'lesson_notes_file'
        )


class LessonCreateSerializer(LessonSerializer):

    class Meta:
        model = Lesson
        fields = (
            'id',
            'user',
            'lesson_name',
            'lesson_content',
            'lesson_content_file',
            'lesson_notes',
            'lesson_notes_file'
        )


class LessonRetrieveSerializer(LessonSerializer):
    pass


class LessonUpdateSerializer(LessonSerializer):

    class Meta:
        model = Lesson
        fields = (
            'id',
            'user',
            'lesson_name',
            'lesson_content',
            'lesson_content_file',
            'lesson_notes',
            'lesson_notes_file'
        )


class ExamSerializer(serializers.ModelSerializer):

    class Meta:
        model = Exam
        fields = (
            'id',
            'lesson',
            'exam_type',
            'exam_information',
            'exam_file',
            'exam_answer_file'
        )


class ExamListSerializer(ExamSerializer):

    class Meta:
        model = Exam
        fields = (
            'id',
            'lesson',
            'exam_type',
            'exam_information',
            'exam_file',
            'exam_answer_file'
        )


class ExamCreateSerializer(ExamSerializer):

    class Meta:
        model = Exam
        fields = (
            'id',
            'lesson',
            'exam_type',
            'exam_information',
            'exam_file',
            'exam_answer_file'
        )


class ExamRetrieveSerializer(ExamSerializer):
    pass


class ExamUpdateSerializer(ExamSerializer):

    class Meta:
        model = Exam
        fields = (
            'id',
            'lesson',
            'exam_type',
            'exam_information',
            'exam_file',
            'exam_answer_file'
        )


class Other_DocumentSerializer(serializers.ModelSerializer):

    class Meta:
        model = Other_Document
        fields = (
            'id',
            'lesson',
            'name',
            'document'
        )


class Other_DocumentListSerializer(Other_DocumentSerializer):

    class Meta:
        model = Other_Document
        fields = (
            'id',
            'lesson',
            'name',
            'document'
        )


class Other_DocumentCreateSerializer(Other_DocumentSerializer):

    class Meta:
        model = Other_Document
        fields = (
            'id',
            'lesson',
            'name',
            'document'
        )


class Other_DocumentRetrieveSerializer(Other_DocumentSerializer):
    pass


class Other_DocumentUpdateSerializer(Other_DocumentSerializer):

    class Meta:
        model = Other_Document
        fields = (
            'id',
            'lesson',
            'name',
            'document'
        )


class Requested_DocumentsSerializer(serializers.ModelSerializer):

    class Meta:
        model = Requested_Documents
        fields = ('id', 'lesson', 'd_name', 'd_bool')


class Requested_DocumentsListSerializer(Requested_DocumentsSerializer):

    class Meta:
        model = Requested_Documents
        fields = ('id', 'lesson', 'd_name', 'd_bool')


class Requested_DocumentsCreateSerializer(Requested_DocumentsSerializer):

    class Meta:
        model = Requested_Documents
        fields = ('id', 'lesson', 'd_name', 'd_bool')


class Requested_DocumentsRetrieveSerializer(Requested_DocumentsSerializer):
    pass


class Requested_DocumentsUpdateSerializer(Requested_DocumentsSerializer):

    class Meta:
        model = Requested_Documents
        fields = ('id', 'lesson', 'd_name', 'd_bool')
