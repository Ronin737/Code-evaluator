from django.urls import path
from .views import QuestionAnswerAPI,QuestionsListAPI,QuestionsUpdateAPI,QuestionExpandAPI


urlpattern=[path('questions/<str:pk>/answer',QuestionAnswerAPI.as_view(),name='question-answer'),
            path('questions/',QuestionsListAPI.as_view(),name='question-list-create'),
            path('questions/<str:pk>/',QuestionExpandAPI.as_view(),name='question-expand'),
            path('questions/<str:pk>/edit/',QuestionsUpdateAPI.as_view(),name='question-update')]