# Generated by Django 4.0.4 on 2022-05-12 07:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('instagram', '0002_rename_content_post_message_remove_post_title'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='is_public',
            field=models.BooleanField(default=False, verbose_name='공개여부'),
        ),
    ]