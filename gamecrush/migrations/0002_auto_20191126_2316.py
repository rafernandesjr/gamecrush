# Generated by Django 2.2.7 on 2019-11-26 23:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gamecrush', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='birthdate',
            field=models.DateField(blank=True, null=True, verbose_name='DOB'),
        ),
    ]