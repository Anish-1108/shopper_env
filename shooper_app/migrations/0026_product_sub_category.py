# Generated by Django 4.2.10 on 2024-03-07 09:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('shooper_app', '0025_alter_order1_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='sub_category',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='shooper_app.sub_category'),
        ),
    ]