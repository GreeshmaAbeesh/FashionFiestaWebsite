# Generated by Django 4.2.6 on 2024-04-30 12:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('wishlist', '0002_remove_wishlist_user_remove_wishlistitem_wishlist_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='wishlistitem',
            old_name='cart',
            new_name='wishlist',
        ),
        migrations.AlterField(
            model_name='wishlist',
            name='date_added',
            field=models.DateField(auto_now_add=True),
        ),
    ]