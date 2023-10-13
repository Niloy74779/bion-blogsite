# Generated by Django 4.2.3 on 2023-09-06 15:04

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('blogs', '0015_alter_blogpost_author'),
    ]

    operations = [
        migrations.AddField(
            model_name='blogpost',
            name='favourites',
            field=models.ManyToManyField(blank=True, null=True, related_name='favourite', to=settings.AUTH_USER_MODEL),
        ),
    ]
