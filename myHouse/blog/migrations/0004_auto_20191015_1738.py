# Generated by Django 2.2.6 on 2019-10-15 17:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_auto_20191015_1734'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='lien_video',
            field=models.CharField(blank=True, max_length=255),
        ),
    ]