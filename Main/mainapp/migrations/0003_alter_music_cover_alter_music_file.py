# Generated by Django 5.1.4 on 2024-12-06 07:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0002_remove_music_music_remove_music_name_music_cover_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='music',
            name='cover',
            field=models.FileField(upload_to=''),
        ),
        migrations.AlterField(
            model_name='music',
            name='file',
            field=models.FileField(upload_to=''),
        ),
    ]
