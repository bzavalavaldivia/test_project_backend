# Generated by Django 3.1.4 on 2020-12-25 20:04

from django.db import migrations
import django_mysql.models


class Migration(migrations.Migration):

    dependencies = [
        ('surveys', '0002_auto_20201225_1458'),
    ]

    operations = [
        migrations.AlterField(
            model_name='question',
            name='type',
            field=django_mysql.models.EnumField(choices=[('t', 'Text'), ('a', 'Alternative'), ('o', 'Oorder')]),
        ),
    ]