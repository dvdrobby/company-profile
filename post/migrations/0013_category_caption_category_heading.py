# Generated by Django 4.1.5 on 2023-03-03 12:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0012_alter_contact_phone'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='caption',
            field=models.TextField(default='None', verbose_name='Caption'),
        ),
        migrations.AddField(
            model_name='category',
            name='heading',
            field=models.CharField(default='None', max_length=50, verbose_name='Heading'),
        ),
    ]
