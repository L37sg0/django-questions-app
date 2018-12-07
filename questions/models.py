from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

# Create your models here.

class Question(models.Model):
    question_text = models.CharField(max_length=100)
    pub_date = models.DateTimeField(default=timezone.now)
    pub_by = models.ForeignKey(User, on_delete=models.PROTECT)
    answer_a_text = models.CharField(max_length=100, default='')
    answer_b_text = models.CharField(max_length=100, default='')
    answer_c_text = models.CharField(max_length=100, default='')
    answer_corect_text = models.CharField(max_length=1, default='')

    def __str__(self):
        return str(self.question_text+self.answer_a_text+self.answer_b_text+self.answer_c_text+self.answer_corect_text)

    class Meta:
        verbose_name_plural = 'въпроси'

#class Answer(models.Model):
 #   question = models.ForeignKey(Question, on_delete=models.CASCADE)
  #  answer_text = models.CharField(max_length=100)
   # is_right = models.BooleanField(default=False)

    #def __str__(self):
     #   return self.answer_text

#    class Meta:
 #       verbose_name_plural = 'отговори'