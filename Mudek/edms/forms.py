from django.forms import ModelForm
from edms.models import *

class LessonForm(ModelForm):
    class Meta :
        model = Lesson
        fields = [
            'lesson_name',
            'lesson_content',
            'lesson_content_file',
            'lesson_notes',
            'lesson_notes_file'
        ]


class ExamForm(ModelForm):
    class Meta :
        model = Exam
        fields = [
            'exam_type',
            'exam_information',
            'exam_file',
            'exam_answer_file'
        ]


class Other_DocumentForm(ModelForm):
    model = Other_Document
    fields = [
            'course_evaluation_form',
            'course_survey',
            'exam_note_list_midterm',
            'exam_note_list_end_of_term',
            'exam_note_list_Integrated'
        ]

class Requested_DocumentsForm(ModelForm):

    class Meta:
        model = Requested_Documents
        fields = ['d_bool',]
