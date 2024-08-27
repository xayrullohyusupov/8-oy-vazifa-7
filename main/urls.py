from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('quiz-list/', views.quizList, name='quizList'),
    path('quiz-detail/<int:id>/', views.quizDetail, name='quizDetail'),
    path('create-quiz', views.createQuiz, name='createQuiz'),
    path('create-question/<int:id>/', views.questionCreate, name='questionCreate'),
    path('question-detail/<int:id>/', views.questionDetail, name='questionDetail'),  # Qo'shildi
    path('delete-question/<int:id>/', views.questionDelete, name='questionDelete'),  # Qo'shildi
    path('create-option/<int:question_id>/', views.optionCreate, name='optionCreate'),  # Qo'shildi
    path('delete-option/<int:id>/', views.optionDelete, name='optionDelete'),  # Qo'shildi
    
]
