# Generated by Django 3.1.2 on 2020-10-31 21:53

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('barcode', models.PositiveIntegerField(primary_key=True, serialize=False, verbose_name='Código de Barras')),
                ('name', models.CharField(max_length=100, verbose_name='Produto')),
            ],
        ),
    ]
