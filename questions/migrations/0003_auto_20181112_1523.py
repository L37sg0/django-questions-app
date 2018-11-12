# Generated by Django 2.1.3 on 2018-11-12 13:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('questions', '0002_auto_20181112_1507'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='question',
            name='right_a',
        ),
        migrations.RemoveField(
            model_name='question',
            name='right_b',
        ),
        migrations.RemoveField(
            model_name='question',
            name='right_c',
        ),
        migrations.RemoveField(
            model_name='question',
            name='right_d',
        ),
        migrations.AddField(
            model_name='question',
            name='a',
            field=models.CharField(default='aa', max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='question',
            name='b',
            field=models.CharField(default='aa', max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='question',
            name='c',
            field=models.CharField(default='aa', max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='question',
            name='d',
            field=models.CharField(default='aa', max_length=100),
            preserve_default=False,
        ),
    ]
