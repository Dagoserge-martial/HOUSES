# Generated by Django 2.2.6 on 2019-10-15 18:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('house', '0002_auto_20191015_1722'),
    ]

    operations = [
        migrations.AlterField(
            model_name='info_house',
            name='noumbre',
            field=models.CharField(max_length=255),
        ),
    ]
