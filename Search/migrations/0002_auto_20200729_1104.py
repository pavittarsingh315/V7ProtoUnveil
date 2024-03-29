# Generated by Django 3.0.8 on 2020-07-29 18:04

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('Search', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='User_Search',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Search_value', models.CharField(max_length=100, null=True)),
                ('Search_User', models.CharField(blank=True, default=None, max_length=200, null=True)),
                ('Frequency', models.IntegerField(blank=True, null=True)),
                ('date_added', models.DateTimeField(default=django.utils.timezone.now)),
            ],
            options={
                'verbose_name_plural': 'Searches',
            },
        ),
        migrations.RemoveField(
            model_name='search',
            name='Search_User',
        ),
    ]
