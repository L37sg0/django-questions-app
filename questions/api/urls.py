from .views import QuestionAPIView
from django.conf.urls import url

app_name = 'questions'
urlpatterns = [
    url(r'^$', QuestionAPIView.as_view(), name='question-read'),
]