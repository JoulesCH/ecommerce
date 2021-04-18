# Generated by Django 3.2 on 2021-04-18 19:03

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Cart',
            fields=[
                ('ide', models.AutoField(primary_key=True, serialize=False)),
                ('promo', models.IntegerField(default=0)),
                ('subtotal', models.FloatField(default=0)),
                ('estado', models.CharField(default='waiting', max_length=20)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
