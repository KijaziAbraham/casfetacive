# Generated by Django 4.2.5 on 2023-12-17 19:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('teachings_app', '0003_video_thumbnail_url'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='content',
            field=models.FileField(upload_to='books/pdfs/'),
        ),
    ]
