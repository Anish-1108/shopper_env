# Generated by Django 4.0.3 on 2024-04-18 09:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shooper_app', '0043_alter_order1_product'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order1',
            name='product',
        ),
    ]