from django.contrib import admin
from .models import *

@admin.register(Faculty)
class FacultyAdmin(admin.ModelAdmin):
    fields = ('f_code', 'f_name')
    list_display = ('f_code', 'f_name')
    list_filter = ('f_name',)
    search_fields = ('f_name',)


@admin.register(Department)
class DepartmentAdmin(admin.ModelAdmin):
    fields = ('faculty', 'd_code', 'd_name')
    list_display = ('faculty', 'd_code', 'd_name')
    list_filter = ('faculty', 'd_code', 'd_name')
    search_fields = ('faculty', 'd_code', 'd_name')


@admin.register(Output)
class OutputAdmin(admin.ModelAdmin):
    fields = ('o_no', 'o_comment', 'general_version', 'lower_version', 'side_version')
    list_display = ('o_no', 'o_comment', 'general_version', 'lower_version', 'side_version')
    list_filter = ('o_no',)
    search_fields = ('o_no',)


@admin.register(Lesson)
class LessonAdmin(admin.ModelAdmin):
    fields = ('output', 'l_code', 'l_name', 'l_academician', 'l_status', 'l_period', 'l_class', 'l_order', 'l_possitive', 'l_language', 'l_ects', 'l_akts', 'l_credit', 'l_theory', 'l_application', 'l_lab')
    list_display = ('l_code', 'l_name', 'l_academician', 'l_class', 'l_period', 'l_ects', 'l_akts')
    list_filter = ('l_period', 'l_status', 'l_academician')
    search_fields = ('l_code', 'l_name ', 'l_academician')

    def get_output(self, obj):
        output = '-'.join(
            [output.o_no for output in obj.output.all()]
        )
        return output