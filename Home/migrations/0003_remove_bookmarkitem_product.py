# Generated by Django 3.0.8 on 2020-07-10 22:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Home', '0002_bookmarkitem_product'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='bookmarkitem',
            name='product',
        ),
    ]
