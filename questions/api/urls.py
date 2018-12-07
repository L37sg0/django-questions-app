from .views import QuestionRudView, getQuestionsLength #LengthDataView#QuestionAPIView, AnswerAPIView, questions_detail, bookRudView#, hello_world
from django.urls import path
from django.conf.urls import url

app_name = 'questions'
urlpatterns = [
    #url(r'^a', AnswerAPIView.as_view({'get': 'list'}), name='answer-read'),#({'get': 'list'}), name='question-read'),
    #path('q/<int:pk>', questions_detail, name='question_detail'),
    #url(r'^q', QuestionAPIView.as_view({'get': 'list'}), name='questions-read'),
    #url(r'^hello', hello_world, name='hello'),

    url(r'^(?P<id>\d+)', QuestionRudView.as_view(), name='question-rud'),
    url(r'', getQuestionsLength, name='questions-length'),
]