# Generated by Django 2.1.8 on 2019-04-21 12:48

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='from_user',
        ),
        migrations.AddField(
            model_name='user',
            name='from_user',
            field=models.ManyToManyField(related_name='followings', to=settings.AUTH_USER_MODEL),
        ),
        migrations.RemoveField(
            model_name='user',
            name='to_user',
        ),
        migrations.AddField(
            model_name='user',
            name='to_user',
            field=models.ManyToManyField(related_name='followers', to=settings.AUTH_USER_MODEL),
        ),
    ]
