# Generated by Django 3.1.3 on 2020-11-30 22:14

import ckeditor_uploader.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('hotel', '0005_auto_20201126_1915'),
    ]

    operations = [
        migrations.AlterField(
            model_name='hotel',
            name='detail',
            field=ckeditor_uploader.fields.RichTextUploadingField(),
        ),
    ]