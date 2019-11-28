# Generated by Django 2.2.7 on 2019-11-27 06:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gamecrush', '0002_auto_20191126_2316'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='describe',
            field=models.CharField(default='Descrição', max_length=300),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='user',
            name='birthdate',
            field=models.DateField(blank=True, null=True),
        ),
    ]
