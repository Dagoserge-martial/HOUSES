# Generated by Django 2.2.6 on 2019-10-15 17:34

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_auto_20191015_1722'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='lien_video',
            field=models.CharField(default=django.utils.timezone.now, max_length=255),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='article',
            name='prix',
            field=models.CharField(blank=True, max_length=255),
        ),
    ]
