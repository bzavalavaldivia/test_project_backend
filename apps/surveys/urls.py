from django.urls import path, include
from apps.surveys import views

urlpatterns = [
    path('surveys/', views.SurveyAPIView.as_view()),
    path('surveys/<int:pk>/', views.SurveyDetailAPIView.as_view()),
    path('questions/', views.QuestionAPIView.as_view()),
    path('answers/', views.AnswerAPIView.as_view()),
    path('answers/?<int:pk>', views.AnswerAPIView.as_view()),
]