#from rest_framework import viewsets
#from django.views import generic
from questions.models import Question#, Answer
from .serializers import QuestionSerializer, LengthSerializer#, AnswerSerializer

#from django.shortcuts import render, get_object_or_404
#from django.http import JsonResponse

from rest_framework.decorators import api_view
from rest_framework.response import Response

from rest_framework import generics#, mixins

class QuestionRudView(generics.RetrieveAPIView):
    resource_name       = 'questions'
    lookup_field        = 'id'
    serializer_class    = QuestionSerializer

    def get_queryset(self):
        return Question.objects.all()

class LengthDataView(generics.ListAPIView):
    resource_name       = 'questions'
    serializer_class    = LengthSerializer

    def get_queryset(self):
        questions = Question.objects.all()
        return len(questions)

@api_view()
def getQuestionsLength(request):
    questions = Question.objects.all()
    return Response({"questionsLength": len(questions)})
'''
class QuestionAPIView(viewsets.ModelViewSet):
    queryset = Question.objects.filter()
    serializer_class = QuestionSerializer
    
   
class AnswerAPIView(viewsets.ModelViewSet):
    queryset = Answer.objects.all()
    serializer_class = AnswerSerializer
@api_view()
def questions_detail(request, pk):#question_id):
    queryset = Question.objects.all()
    #question = Question.objects.filter(pk=pk)
    answers = Answer.objects.filter(question=pk)
    return render(request, question)
    #return Response(queryset.question_text)
    {
            'question':question.question_text,
            'answers':answers,
        }
    )

@api_view()#['GET', 'POST'])
def hello_world(request):
    if request.method == 'POST':
        return Response({"message": "Got some data!", "data": request.data})
    return Response({"message": "Hello, world!"})
    '''