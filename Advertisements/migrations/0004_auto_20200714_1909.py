# Generated by Django 3.0.8 on 2020-07-15 02:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Advertisements', '0003_auto_20200713_0006'),
    ]

    operations = [
        migrations.AddField(
            model_name='searchpageads',
            name='Keywords',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='tier2',
            name='Keywords',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]