# Generated by Django 3.2.9 on 2021-12-30 16:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ideas', '0003_alter_idea_audio_file'),
    ]

    operations = [
        migrations.AlterField(
            model_name='idea',
            name='audio_file',
            field=models.FileField(blank=True, default='', upload_to='ideas/audio/'),
        ),
    ]