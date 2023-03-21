# Generated by Django 4.1.5 on 2023-03-21 00:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0013_category_caption_category_heading'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contact',
            name='mobile_phone',
            field=models.CharField(default=1234567888, max_length=20, verbose_name='Mobile Phone'),
        ),
        migrations.AlterField(
            model_name='post',
            name='picture',
            field=models.ImageField(default='/media/about/project-1.jpg', upload_to='uploads/%Y/%m/%d', verbose_name='Picture'),
            preserve_default=False,
        ),
    ]
