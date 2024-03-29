# Generated by Django 3.0.8 on 2020-07-29 17:52

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='SearchPageAds',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('company', models.CharField(max_length=100)),
                ('payment', models.DecimalField(decimal_places=2, default=None, max_digits=20)),
                ('Name', models.CharField(max_length=100)),
                ('Keywords', models.TextField(blank=True, null=True)),
                ('Seller', models.CharField(max_length=100)),
                ('Link', models.CharField(default=None, max_length=200)),
                ('Image', models.CharField(default=None, max_length=200)),
                ('Price', models.DecimalField(decimal_places=2, default=None, max_digits=20)),
                ('Description', models.TextField()),
                ('date_created', models.DateTimeField(default=django.utils.timezone.now)),
            ],
            options={
                'verbose_name_plural': 'Loaded Search Page Ads',
            },
        ),
        migrations.CreateModel(
            name='Tier1',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('company', models.CharField(max_length=100)),
                ('payment', models.DecimalField(decimal_places=2, default=None, max_digits=20)),
                ('header', models.CharField(max_length=100)),
                ('redirect_url', models.CharField(default=None, max_length=200)),
                ('image_url', models.CharField(default=None, max_length=200)),
                ('front_content', models.TextField()),
                ('hidden_content', models.TextField()),
                ('date_created', models.DateTimeField(default=django.utils.timezone.now)),
            ],
            options={
                'verbose_name_plural': 'Homepage Ads',
            },
        ),
        migrations.CreateModel(
            name='Tier2',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('company', models.CharField(max_length=100)),
                ('payment', models.DecimalField(decimal_places=2, default=None, max_digits=20)),
                ('header', models.CharField(max_length=100)),
                ('Keywords', models.TextField(blank=True, null=True)),
                ('symbol', models.CharField(max_length=100)),
                ('symbol_hex_color', models.CharField(default=None, max_length=20)),
                ('content', models.TextField()),
                ('date_created', models.DateTimeField(default=django.utils.timezone.now)),
            ],
            options={
                'verbose_name_plural': 'Tier2',
            },
        ),
    ]
