# Generated by Django 5.0.1 on 2024-01-23 08:04

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=50)),
                ('author', models.CharField(max_length=50)),
                ('year', models.IntegerField()),
            ],
        ),
    ]
