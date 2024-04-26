# Generated by Django 4.2.10 on 2024-03-07 10:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shooper_app', '0026_product_sub_category'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='address',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='user',
            name='img1',
            field=models.ImageField(default='C:\\Users\\Dell\\Desktop\\shopper_env\\shopper_project\\shooper_app\\static\\img\\avatar6.png', upload_to='image'),
        ),
        migrations.AddField(
            model_name='user',
            name='phone',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]