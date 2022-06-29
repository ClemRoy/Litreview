# Generated by Django 4.0.4 on 2022-06-22 07:55

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('review', '0005_rename_following_user_id_userfollows_following_user_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='userfollows',
            old_name='following_user',
            new_name='followed_user',
        ),
        migrations.AlterUniqueTogether(
            name='userfollows',
            unique_together={('user', 'followed_user')},
        ),
    ]
