# Generated by Django 4.0.4 on 2022-05-12 15:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('raterapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='game',
            name='estimated_time_to_play',
            field=models.CharField(max_length=99),
        ),
    ]