# Generated by Django 2.0.3 on 2018-04-03 12:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('albums', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='album',
            name='photo',
            field=models.ImageField(blank=True, upload_to='media/'),
        ),
    ]
