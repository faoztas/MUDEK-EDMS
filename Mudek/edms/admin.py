# Django
from django.contrib import admin
from django.utils.translation import ugettext_lazy as _

# Local Django
from edms.models import Lesson, Exam, Other_Document, Requested_Documents


@admin.register(Lesson)
class LessonAdmin(admin.ModelAdmin):

    fields = (
        'user', 'lesson_name', 'lesson_content',
        'lesson_content_file', 'lesson_notes', 'lesson_notes_file'
    )

    list_display = ('user', 'lesson_name')
    list_filter = ('user', 'lesson_name')
    search_fields = ('user', 'lesson_name')


@admin.register(Exam)
class ExamAdmin(admin.ModelAdmin):

    fields = (
        'lesson', 'exam_type', 'exam_information',
        'exam_file', 'exam_answer_file'
    )

    list_display = ('lesson', 'exam_type', 'exam_information')
    list_filter = ('lesson', 'exam_type')
    search_fields = ('lesson',)


@admin.register(Requested_Documents)
class Requested_DocumentsAdmin(admin.ModelAdmin):

    fields = ('lesson', 'd_name', 'd_bool')

    list_display = ('lesson', 'd_name', 'd_bool')
    list_filter = ('lesson', 'd_name', 'd_bool')
    search_fields = ('lesson', 'd_name', 'd_bool')


@admin.register(Other_Document)
class Other_DocumentAdmin(admin.ModelAdmin):

    fields = (
        'lesson',
        'name',
        'document'
    )

    list_display = ('lesson', 'name')
    list_filter = ('lesson',)
    search_fields = ('lesson',)
