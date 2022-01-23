# Generated by Django 4.0.1 on 2022-01-21 20:16

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cars',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('_id', models.CharField(db_index=True, max_length=64, verbose_name='id')),
                ('make', models.CharField(max_length=64, verbose_name='make')),
                ('model', models.CharField(max_length=64, verbose_name='model')),
            ],
        ),
    ]
