# Generated by Django 2.2.7 on 2019-11-28 01:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chat', '0004_auto_20191128_0128'),
    ]

    operations = [
        migrations.AlterField(
            model_name='message',
            name='id_auth',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='message',
            name='room',
            field=models.TextField(),
        ),
    ]