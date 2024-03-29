# Generated by Django 4.1.5 on 2023-03-01 01:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0007_message_subscriber'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='slug',
            field=models.SlugField(editable=False, max_length=150, unique=True),
        ),
        migrations.AlterField(
            model_name='post',
            name='slug',
            field=models.SlugField(editable=False, unique=True),
        ),
        migrations.AlterField(
            model_name='tag',
            name='slug',
            field=models.SlugField(editable=False, max_length=100, unique=True),
        ),
    ]
