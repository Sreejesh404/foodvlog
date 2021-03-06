# Generated by Django 4.0.1 on 2022-01-25 17:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0003_alter_categ_options'),
        ('cart', '0002_items'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cart',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cart_id', models.CharField(max_length=250, unique=True)),
                ('date_added', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'db_table': 'Cart',
                'ordering': ['date_added'],
            },
        ),
        migrations.CreateModel(
            name='CartItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.IntegerField()),
                ('active', models.BooleanField(default=True)),
                ('cart', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cart.cart')),
                ('products', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='shop.products')),
            ],
            options={
                'db_table': 'CartItem',
            },
        ),
        migrations.RemoveField(
            model_name='items',
            name='cart',
        ),
        migrations.RemoveField(
            model_name='items',
            name='prodt',
        ),
        migrations.DeleteModel(
            name='cartlist',
        ),
        migrations.DeleteModel(
            name='items',
        ),
    ]
