# Generated by Django 3.1.3 on 2020-11-25 18:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('hotel', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='category',
            old_name='create_ate',
            new_name='create_at',
        ),
        migrations.RenameField(
            model_name='category',
            old_name='update_ate',
            new_name='update_at',
        ),
    ]
