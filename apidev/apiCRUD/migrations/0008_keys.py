# Generated by Django 3.2.7 on 2021-09-16 21:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('apiCRUD', '0007_auto_20210815_2255'),
    ]

    operations = [
        migrations.CreateModel(
            name='Keys',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=200)),
                ('description', models.CharField(max_length=200)),
            ],
        ),
    ]