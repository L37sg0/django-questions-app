# Generated by Django 2.1.3 on 2018-11-14 18:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('questions', '0008_auto_20181112_1739'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='answer',
            name='question',
        ),
        migrations.AddField(
            model_name='question',
            name='answer_a_text',
            field=models.CharField(default='', max_length=100),
        ),
        migrations.AddField(
            model_name='question',
            name='answer_b_text',
            field=models.CharField(default='', max_length=100),
        ),
        migrations.AddField(
            model_name='question',
            name='answer_c_text',
            field=models.CharField(default='', max_length=100),
        ),
        migrations.AddField(
            model_name='question',
            name='answer_corect_text',
            field=models.CharField(default='', max_length=1),
        ),
        migrations.DeleteModel(
            name='Answer',
        ),
    ]
