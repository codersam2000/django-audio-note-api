# Generated by Django 4.1.7 on 2023-06-27 18:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('note', '0010_audio_note_user_id'),
    ]

    operations = [
        migrations.RenameField(
            model_name='audio_note',
            old_name='user_id',
            new_name='user',
        ),
    ]
