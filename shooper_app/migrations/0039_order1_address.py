# Generated by Django 4.0.3 on 2024-04-15 09:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('shooper_app', '0038_coupon_discount'),
    ]

    operations = [
        migrations.AddField(
            model_name='order1',
            name='address',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='shooper_app.address'),
        ),
    ]
