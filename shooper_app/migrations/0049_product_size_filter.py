# Generated by Django 4.0.3 on 2024-04-24 04:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shooper_app', '0048_size_filter'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='size_filter',
            field=models.ManyToManyField(blank=True, null=True, to='shooper_app.size_filter'),
        ),
    ]