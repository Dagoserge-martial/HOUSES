# Generated by Django 2.2.6 on 2019-10-15 18:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('house', '0003_auto_20191015_1807'),
    ]

    operations = [
        migrations.AddField(
            model_name='location',
            name='image_vue',
            field=models.ImageField(blank=True, upload_to='img'),
        ),
    ]
