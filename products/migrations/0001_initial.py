# Generated by Django 3.2 on 2021-04-15 05:21

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('ide', models.IntegerField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=50)),
                ('descripcion', models.CharField(max_length=200)),
                ('price', models.FloatField()),
                ('stock', models.IntegerField()),
                ('sizes', models.CharField(max_length=5)),
                ('colors', models.CharField(max_length=20)),
                ('discount', models.FloatField()),
                ('image1', models.ImageField(upload_to='static/images/')),
                ('image2', models.ImageField(upload_to='static/images/')),
                ('image3', models.ImageField(upload_to='static/images/')),
                ('image4', models.ImageField(upload_to='static/images/')),
            ],
        ),
    ]
