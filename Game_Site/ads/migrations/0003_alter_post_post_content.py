# Generated by Django 4.0.6 on 2022-08-27 05:39

import ckeditor_uploader.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ads', '0002_rename_author_post_post_author_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='post_content',
            field=ckeditor_uploader.fields.RichTextUploadingField(blank=True, null=True),
        ),
    ]