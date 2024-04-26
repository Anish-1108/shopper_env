# Generated by Django 4.2.10 on 2024-03-18 10:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shooper_app', '0028_product_color'),
    ]

    operations = [
        migrations.AddField(
            model_name='order1',
            name='order_id',
            field=models.CharField(blank=True, max_length=10, null=True),
        ),
        migrations.AlterField(
            model_name='product',
            name='color',
            field=models.CharField(blank=True, choices=[('Black', 'Black'), ('White', 'White'), ('Red', 'Red'), ('Blue', 'Blue'), ('Green', 'Green')], max_length=50, null=True),
        ),
    ]