# Generated by Django 5.1.4 on 2024-12-06 07:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0003_alter_music_cover_alter_music_file'),
    ]

    operations = [
        migrations.AlterField(
            model_name='music',
            name='cover',
            field=models.FileField(null=True, upload_to=''),
        ),
        migrations.AlterField(
            model_name='music',
            name='file',
            field=models.FileField(null=True, upload_to=''),
        ),
    ]
