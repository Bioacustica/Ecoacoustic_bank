# Generated by Django 3.2.6 on 2021-08-15 22:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('apiCRUD', '0006_auto_20210814_2301'),
    ]

    operations = [
        migrations.AlterModelTable(
            name='frequencydetail',
            table='frequency_detail',
        ),
        migrations.AlterModelTable(
            name='locality',
            table='locality',
        ),
    ]