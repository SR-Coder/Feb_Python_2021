# Generated by Django 2.2.4 on 2021-02-22 17:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('application', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='email',
            field=models.CharField(default='j@r.com', max_length=255),
            preserve_default=False,
        ),
    ]
