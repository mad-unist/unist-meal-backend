# Generated by Django 3.2.13 on 2022-08-15 14:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='kakao_id',
        ),
        migrations.AlterField(
            model_name='user',
            name='id',
            field=models.IntegerField(primary_key=True, serialize=False, unique=True),
        ),
    ]
