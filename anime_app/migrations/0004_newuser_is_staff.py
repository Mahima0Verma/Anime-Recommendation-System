# Generated by Django 5.0.6 on 2024-12-04 13:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('anime_app', '0003_remove_newuser_is_staff'),
    ]

    operations = [
        migrations.AddField(
            model_name='newuser',
            name='is_staff',
            field=models.BooleanField(default=False),
        ),
    ]