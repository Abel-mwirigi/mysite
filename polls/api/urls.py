from django.urls import path
from polls.api import views

urlpatterns = [
    path('choice/', views.ChoiceList.as_view()),
    path('question/', views.QuestionDetail.as_view()),

]
