# Generated by Django 4.2.6 on 2024-06-10 18:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0005_salesreportnew_discount_salesreportnew_ip_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='salesreportnew',
            name='discount',
        ),
        migrations.RemoveField(
            model_name='salesreportnew',
            name='ip',
        ),
        migrations.RemoveField(
            model_name='salesreportnew',
            name='is_ordered',
        ),
        migrations.RemoveField(
            model_name='salesreportnew',
            name='order',
        ),
        migrations.RemoveField(
            model_name='salesreportnew',
            name='order_total',
        ),
        migrations.RemoveField(
            model_name='salesreportnew',
            name='status',
        ),
        migrations.RemoveField(
            model_name='salesreportnew',
            name='tax',
        ),
        migrations.RemoveField(
            model_name='salesreportnew',
            name='user',
        ),
    ]
