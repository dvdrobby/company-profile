# Generated by Django 4.1.5 on 2023-03-24 10:35

import ckeditor_uploader.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0020_alter_about_picture'),
    ]

    operations = [
        migrations.AlterField(
            model_name='about',
            name='content',
            field=ckeditor_uploader.fields.RichTextUploadingField(blank=True, null=True, verbose_name='About'),
        ),
    ]
