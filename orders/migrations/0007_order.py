# Generated by Django 2.1.5 on 2020-07-06 20:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0006_auto_20200625_0331'),
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('total_price', models.IntegerField()),
                ('cart', models.ManyToManyField(to='orders.Product')),
            ],
        ),
    ]
