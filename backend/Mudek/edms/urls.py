# Django
from django.urls import path
from django.contrib.auth.views import (
    LoginView, LogoutView, PasswordResetView, PasswordResetDoneView,
    PasswordResetConfirmView, PasswordResetCompleteView,
    PasswordChangeView, PasswordChangeDoneView
)

# Local
from edms.views import (
    HomeView, LessonListView, LessonDetailView, LessonUpdateView,
    ExamUpdateView, Other_DocumentUpdateView
)


app_name = 'edms'

urlpatterns = [
    # Home Page
    path('', HomeView.as_view(), name='home'),
    
    # Lesson Links
    path('lessons', LessonListView.as_view(), name='lesson-list'),
    path('lessons/<int:pk>', LessonDetailView.as_view(), name='lesson-detail'),
    path('lessons/<int:pk>/update', LessonUpdateView.as_view(), name='lesson-update'),

    # Exam Links
    path('exam/<int:pk>/update', ExamUpdateView.as_view(), name='exam-update'),

    # Other Document Links
    path('other_document/<int:pk>/update', Other_DocumentUpdateView.as_view(), name='other-document-update'),

    # User İnteraction
    path('login/', LoginView.as_view(), {
        'template_name': 'registration/login.html'},
        name='login'
    ),
    path('logout/', LogoutView.as_view(), {
        'template_name': 'registration/logout.html'},
        name='logout'
    ),
    path('reset-password/', PasswordResetView.as_view(), {
        'template_name': 'registration/reset_password.html',
        'post_reset_redirect': 'edms:password_reset_done',
        'email_template_name': 'registration/reset_password_email.html'
        }, name='reset_password'
    ),
    path('reset-password/done/', PasswordResetDoneView.as_view(), {
        'template_name': 'registration/reset_password_done.html'
        }, name='password_reset_done'
    ),
    path('reset-password/confirm/<uidb64>/<token>/', PasswordResetConfirmView.as_view(), {
            'template_name': 'registration/reset_password_confirm.html',
            'post_reset_redirect': 'edms:password_reset_complete'
            }, name='password_reset_confirm'
    ),
    path('reset-password/complete/', PasswordResetCompleteView.as_view(), {
        'template_name': 'registration/reset_password_complete.html'
        }, name='password_reset_complete'
    ),
    path('password_change/', PasswordChangeView.as_view(), name='password_change'),
    path('password_change/done/', PasswordChangeDoneView.as_view(), name='password_change_done'),
]