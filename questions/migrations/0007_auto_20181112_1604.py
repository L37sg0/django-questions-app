# Generated by Django 2.1.3 on 2018-11-12 14:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('questions', '0006_remove_question_right_answer'),
    ]

    operations = [
        migrations.CreateModel(
            name='Answer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('answer_text', models.CharField(max_length=100)),
                ('is_right', models.BooleanField(default=False)),
            ],
        ),
        migrations.RenameField(
            model_name='question',
            old_name='text',
            new_name='question_text',
        ),
        migrations.RemoveField(
            model_name='question',
            name='A',
        ),
        migrations.RemoveField(
            model_name='question',
            name='B',
        ),
        migrations.RemoveField(
            model_name='question',
            name='C',
        ),
        migrations.RemoveField(
            model_name='question',
            name='D',
        ),
        migrations.AddField(
            model_name='answer',
            name='question',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='questions.Question'),
        ),
    ]
