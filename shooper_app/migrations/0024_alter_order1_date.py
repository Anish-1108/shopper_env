# Generated by Django 4.2.10 on 2024-03-06 10:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shooper_app', '0023_order1'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order1',
            name='date',
            field=models.DateTimeField(auto_created=True),
        ),
    ]
