# Generated by Django 4.2.8 on 2024-03-26 13:30

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='MyData',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('busy_po_no', models.IntegerField()),
                ('party_name', models.CharField(max_length=100)),
                ('product_name', models.CharField(max_length=100)),
                ('qty_main', models.IntegerField()),
            ],
        ),
    ]