# Generated by Django 4.0 on 2022-01-22 15:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api_app', '0002_remove_cars__id'),
    ]

    operations = [
        migrations.AddField(
            model_name='cars',
            name='rating',
            field=models.IntegerField(blank=True, null=True, verbose_name='model'),
        ),
    ]
