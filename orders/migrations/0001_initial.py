# Generated by Django 5.0.4 on 2024-04-08 10:31

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=50)),
                ('last_name', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=254)),
                ('address', models.CharField(max_length=250)),
                ('postal_code', models.CharField(max_length=22)),
                ('status', models.CharField(choices=[('unfullfilled', 'Unfullfilled'), ('ready to pickup', 'READY TO PICKUP'), ('canceled', 'CANCELED'), ('shipped', 'SHIPPED'), ('partially fulfilled', 'PARTIALLY FULFILLED'), ('fullfilled', 'Fullfilled')], default='unfullfilled', max_length=20)),
                ('city', models.CharField(max_length=101)),
                ('delivery', models.CharField(choices=[('standart shipping', 'Standard shipping'), ('local pickup', 'Local pickup'), ('local delivery', 'Local delivery'), ('free shipping', 'Free shipping'), ('cash on delivery', 'Cash on delivery'), ('express', 'Express')], default=1, max_length=20)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('paid', models.BooleanField(default=False)),
            ],
            options={
                'ordering': ['-created'],
                'indexes': [models.Index(fields=['-created'], name='orders_orde_created_743fca_idx')],
            },
        ),
        migrations.CreateModel(
            name='OrderItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('quantity', models.PositiveIntegerField(default=1)),
                ('order', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='items', to='orders.order')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='order_items', to='app.course')),
            ],
        ),
    ]
