# Generated by Django 4.1.5 on 2023-03-02 12:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0011_contact_company_name_alter_contact_iframe'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contact',
            name='phone',
            field=models.CharField(blank=True, max_length=20, null=True, verbose_name='Phone'),
        ),
    ]