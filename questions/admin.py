from django.contrib import admin
from .models import Question#, Answer

# Register your models here.
#class AnswerInLine(admin.TabularInline):
 #   model = Answer
  #  extra = 4
    

class QuestionAdmin(admin.ModelAdmin):
    fieldsets = [
        ('Въпрос:',               {'fields':['question_text']}),
        ('Дата на публикуване:', {'fields':['pub_date']}),
        ('Публикуван от:', {'fields':['pub_by']}),
        ('Oтговори:', {'fields':['answer_a_text','answer_b_text','answer_c_text',]}),
        ('Правилен отговор:', {'fields':['answer_corect_text']}),
    ]
    #inlines = [AnswerInLine]
    list_display = ('question_text', 'pub_date', 'pub_by')
    list_filter = ['pub_date']
    search_fields = ['question_text']

admin.site.register(Question, QuestionAdmin)
   