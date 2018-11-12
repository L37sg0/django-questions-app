from rest_framework import generics, mixins
from questions.models import Question
from .serializers import QuestionSerializer

class QuestionAPIView(mixins.CreateModelMixin, generics.ListAPIView):
    resource_name = 'questions'
    serializer_class = QuestionSerializer

    def get_queryset(self):
        return Question.objects.all()

    #def post(self, request, *args, **kwargs):
       # return self.create(request, *args, **kwargs)

#class bookRudView(generics.RetrieveUpdateDestroyAPIView):
 #   resource_name       = 'books'
  #  lookup_field        = 'id'
   # serializer_class    = bookSerializer

    #def get_queryset(self):
     #   return Book.objects.all()