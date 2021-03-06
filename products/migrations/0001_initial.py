# Generated by Django 3.2 on 2021-04-24 16:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('shoppingcarts', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Color',
            fields=[
                ('ide', models.AutoField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=30)),
                ('codigo', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('ide', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=50)),
                ('descripcion', models.TextField()),
                ('price', models.FloatField()),
                ('stock', models.IntegerField()),
                ('categories', models.CharField(default='temporada,', max_length=300)),
                ('discount', models.FloatField()),
                ('image1', models.ImageField(upload_to='static/images/')),
                ('image2', models.ImageField(null=True, upload_to='static/images/')),
                ('image3', models.ImageField(null=True, upload_to='static/images/')),
                ('image4', models.ImageField(null=True, upload_to='static/images/')),
            ],
        ),
        migrations.CreateModel(
            name='Size',
            fields=[
                ('ide', models.AutoField(primary_key=True, serialize=False)),
                ('valor', models.CharField(max_length=5)),
            ],
        ),
        migrations.CreateModel(
            name='ProductSpec',
            fields=[
                ('ide', models.AutoField(primary_key=True, serialize=False)),
                ('stock', models.IntegerField(default=1)),
                ('color', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='products.color')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='products.product')),
                ('size', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='products.size')),
            ],
        ),
        migrations.CreateModel(
            name='CartProduct',
            fields=[
                ('ide', models.AutoField(primary_key=True, serialize=False)),
                ('quantity', models.IntegerField(default=1)),
                ('talla', models.CharField(default='Unico', max_length=5)),
                ('color', models.CharField(default='Unico', max_length=20)),
                ('cart', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='shoppingcarts.cart')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='products.product')),
            ],
        ),
    ]
