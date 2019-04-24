# Django
from django.shortcuts import render, redirect
from django.urls import reverse
from django.views.generic import TemplateView, ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth import update_session_auth_hash

# Local
from edms.models import Lesson, Exam, Other_Document,Requested_Documents


class HomeView(TemplateView):
    template_name = 'edms/home.html'


class LessonListView(ListView):
    model = Lesson
    template_name = 'edms/lesson/list.html'

    def get(self, request):
        lessons = Lesson.objects.filter(user=request.user)
        return render(request, self.template_name, {'lessons': lessons})

class LessonDetailView(DetailView):
    model = Lesson
    template_name = 'edms/lesson/detail.html'


class LessonUpdateView(UpdateView):
    model = Lesson
    template_name = 'edms/lesson/update.html'
    fields = [
        'lesson_content', 'lesson_content_file',
        'lesson_notes', 'lesson_notes_file'
    ]
    success_url = "/edms/lessons"


class ExamUpdateView(UpdateView):
    model = Exam
    template_name = 'edms/exam/update.html'
    fields = ['exam_type', 'exam_information', 'exam_file', 'exam_answer_file']
    success_url = "/edms/lessons"


class Other_DocumentUpdateView(UpdateView):
    model = Other_Document
    template_name = 'edms/other/update.html'
    fields = [
        'course_evaluation_form', 'course_survey', 'exam_note_list_midterm',
        'exam_note_list_end_of_term', 'exam_note_list_Integrated'
    ]
    success_url = "/edms/lessons"
