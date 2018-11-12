# Generated by Django 2.1.3 on 2018-11-12 13:07

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('questions', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='question',
            name='right_a',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='question',
            name='right_b',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='question',
            name='right_c',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='question',
            name='right_d',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='question',
            name='pub_date',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]