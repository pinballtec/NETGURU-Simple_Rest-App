# Generated by Django 4.0 on 2022-01-23 17:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
        ('api_app', '0004_alter_cars_rating'),
    ]

    operations = [
        migrations.AddField(
            model_name='cars',
            name='user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='auth.user', verbose_name='User'),
        ),
    ]
