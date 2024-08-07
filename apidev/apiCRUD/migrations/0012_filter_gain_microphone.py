# Generated by Django 3.2.8 on 2021-10-08 03:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('apiCRUD', '0011_alter_keys_table'),
    ]

    operations = [
        migrations.CreateModel(
            name='Filter',
            fields=[
                ('id_filter', models.SmallIntegerField(primary_key=True, serialize=False)),
                ('decription', models.CharField(max_length=100)),
            ],
            options={
                'db_table': 'filter',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Gain',
            fields=[
                ('id_gain', models.SmallIntegerField(primary_key=True, serialize=False)),
                ('description', models.CharField(max_length=100)),
            ],
            options={
                'db_table': 'gain',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Microphone',
            fields=[
                ('id_microphone', models.SmallIntegerField(primary_key=True, serialize=False)),
                ('description', models.CharField(blank=True, max_length=100, null=True)),
            ],
            options={
                'db_table': 'microphone',
                'managed': False,
            },
        ),
    ]
