from rest_framework import serializers
from questions.models import Question#, Answer

class QuestionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Question
        fields = (
            'id',
            'question_text',
            'answer_a_text',
            'answer_b_text',
            'answer_c_text',
            'answer_corect_text',
        )
class LengthSerializer(serializers.ModelSerializer):
    model = Question
    fields = (
        'questionsLength',
    )
#class AnswerSerializer(serializers.ModelSerializer):
 #   class Meta:
  #      model = Answer
   #     fields = (
    #        'id',
     #       'question',
      #      'answer_text',
       #     'is_right',
        #)