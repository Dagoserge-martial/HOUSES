# Generated by Django 2.2.6 on 2019-10-17 04:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('house', '0007_info_house_article'),
    ]

    operations = [
        migrations.AlterField(
            model_name='info_house',
            name='article',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='article_info', to='blog.Article'),
        ),
    ]
