# Generated by Django 4.1.5 on 2023-03-02 12:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0008_alter_category_slug_alter_post_slug_alter_tag_slug'),
    ]

    operations = [
        migrations.AddField(
            model_name='contact',
            name='site_map_url',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='Site Map'),
        ),
    ]
