# Generated by Django 4.2.5 on 2023-12-16 22:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home_app', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='category',
            old_name='home_model',
            new_name='malengo_content',
        ),
    ]
