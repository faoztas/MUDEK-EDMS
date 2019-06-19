# Django
from django.shortcuts import render, redirect
from django.urls import reverse
from django.views.generic import ListView, DetailView
from django.views.generic.edit import UpdateView, FormView
from django.db.models import Q
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout

# Local
from edms.models import Lesson, Exam, Other_Document, Requested_Documents
from users.models import User
from .forms import LessonForm, OtherDocumentForm, LoginForm


class LoginView(FormView):
    template_name = 'registration/login.html'
    form_class = LoginForm
    success_url = '/lessons'

    def form_valid(self, form):
        form = LoginForm(self.request.POST or None)
        if form.is_valid():
            email = self.request.POST.get('email')
            password = self.request.POST.get('password')
            user = authenticate(email=email, password=password)
            login(self.request, user)
            return redirect('edms:lesson-list')
        return render(self.request, self.template_name , {'form':form})


class LessonListView(ListView):
    model = Lesson
    template_name = 'edms/lesson/list.html'
    success_url = '/lessons'
    
    def get(self, request):
        if request.user.is_authenticated:
            user = request.user
            if user.is_department_manager or user.is_assistant_department_manager or user.is_dean_manager:
                documnets = Requested_Documents.objects.filter(
                    lesson__user=user
                ).order_by("lesson")
                lessons = {}
                all_lessons = Lesson.objects.all()            
                for lesson in all_lessons:
                    lesson_id = str(lesson.id)
                    lessons[lesson_id] = {
                            'lesson': lesson,
                            'docs': []
                        }

                for doc in documnets:
                    lesson_id = str(doc.lesson.id)
                    lessons[lesson_id]['docs'].append(doc)
                return render(request, self.template_name, {
                    'lessons': lessons
                })
            elif user.is_academician:
                documnets = Requested_Documents.objects.filter(
                    lesson__user=user
                ).order_by("lesson")

                lessons = {}
                for lesson in Lesson.objects.filter(user=user):
                    lesson_id = str(lesson.id)
                    lessons[lesson_id] = {
                            'lesson': lesson,
                            'docs': []
                        }

                for doc in documnets:
                    lesson_id = str(doc.lesson.id)
                    lessons[lesson_id]['docs'].append(doc)

                return render(request, self.template_name, {
                    'lessons': lessons,
                })
        else:
            return redirect(reverse('edms:login'))


class LessonDetailView(DetailView):
    model = Lesson
    template_name = 'edms/lesson/detail.html'


class LessonUpdateView(SuccessMessageMixin, UpdateView):
    model = Lesson
    template_name = 'edms/lesson/update.html'
    form_class = LessonForm
    
    success_url = "/lessons"
    success_message = 'Lesson successfully saved!!!!'

    def update(self, request, *args, **kwargs):
        messages.success(self.request, self.success_message)
        return super(LessonUpdateView, self).update(request, *args, **kwargs)


class ExamUpdateView(SuccessMessageMixin, UpdateView):
    model = Exam
    template_name = 'edms/exam/update.html'
    fields = ['exam_information', 'exam_file', 'exam_answer_file']
    success_url = "/lessons"
    success_message = 'Exam successfully saved!!!!'

    def update(self, request, *args, **kwargs):
        messages.success(self.request, self.success_message)
        return super(ExamUpdateView, self).update(request, *args, **kwargs)


class OtherDocumentUpdateView(SuccessMessageMixin, UpdateView):
    model = Other_Document
    template_name = 'edms/other/update.html'
    form_class = OtherDocumentForm
    success_url = "/lessons"
    success_message = 'Other Document successfully saved!!!!'

    def update(self, request, *args, **kwargs):
        messages.success(self.request, self.success_message)
        return super(OtherDocumentUpdateView, self).update(request, *args, **kwargs)


class RequstedDocumentsUpdateView(SuccessMessageMixin, UpdateView):
    model = Requested_Documents
    template_name = 'edms/requested/update.html'
    fields = ['d_bool', ]
    success_url = "/lessons"
    success_message = 'Requsted Document successfully saved!!!!'

    def update(self, request, *args, **kwargs):
        messages.success(self.request, self.success_message)
        return super(RequstedDocumentsUpdateView, self).update(request, *args, **kwargs)
