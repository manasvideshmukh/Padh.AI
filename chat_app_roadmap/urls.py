from django.urls import path
from . import views

urlpatterns = [
    path("", views.chat, name="chat"),
    path("quiz", views.quiz, name="quiz"),
    path("ask_question/", views.ask_question, name="ask_question"),
    path("take_quiz/", views.take_quiz, name="take_quiz"),
]