# Generated by Django 4.2.6 on 2024-06-10 09:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('cart', '0011_alter_cartitem_cart_alter_cartitem_user'),
        ('orders', '0002_addresses_order_note'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='addresses',
            name='order_note',
        ),
        migrations.AddField(
            model_name='order',
            name='coupon',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='orders', to='cart.coupon'),
        ),
        migrations.AddField(
            model_name='order',
            name='discount',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=10),
        ),
    ]
