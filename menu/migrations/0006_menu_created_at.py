# Generated by Django 3.2.13 on 2022-11-24 18:35

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('menu', '0005_alter_menu_options'),
    ]

    operations = [
        migrations.AddField(
            model_name='menu',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
