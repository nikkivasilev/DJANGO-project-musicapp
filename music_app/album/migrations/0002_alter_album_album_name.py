# Generated by Django 4.1.2 on 2022-10-25 14:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('album', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='album',
            name='album_name',
            field=models.CharField(max_length=30, unique=True, verbose_name='Album Name'),
        ),
    ]