# Generated by Django 3.2 on 2021-05-08 20:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('insurance_register', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='insurancerecord',
            name='mobile',
            field=models.CharField(max_length=10),
        ),
    ]