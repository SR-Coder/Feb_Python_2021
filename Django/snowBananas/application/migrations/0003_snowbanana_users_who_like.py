# Generated by Django 2.2.4 on 2021-02-22 18:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('application', '0002_snowbanana'),
    ]

    operations = [
        migrations.AddField(
            model_name='snowbanana',
            name='users_who_like',
            field=models.ManyToManyField(related_name='likedSnowBananas', to='application.User'),
        ),
    ]
