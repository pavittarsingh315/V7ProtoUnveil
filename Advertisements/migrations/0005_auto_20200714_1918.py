# Generated by Django 3.0.8 on 2020-07-15 02:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Advertisements', '0004_auto_20200714_1909'),
    ]

    operations = [
        migrations.AlterField(
            model_name='searchpageads',
            name='Keywords',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='tier2',
            name='Keywords',
            field=models.TextField(blank=True, null=True),
        ),
    ]
