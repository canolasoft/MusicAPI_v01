# Generated by Django 3.1.7 on 2021-05-05 16:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapi', '0006_datapp_titulomapp'),
    ]

    operations = [
        migrations.AlterField(
            model_name='datapp',
            name='keyapp',
            field=models.CharField(max_length=200),
        ),
    ]