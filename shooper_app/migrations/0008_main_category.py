# Generated by Django 4.2.10 on 2024-02-20 07:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shooper_app', '0007_login_user_otp'),
    ]

    operations = [
        migrations.CreateModel(
            name='main_category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
            ],
        ),
    ]