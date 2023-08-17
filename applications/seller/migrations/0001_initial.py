# Generated by Django 4.2.4 on 2023-08-14 15:34

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Seller',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('NIT_seller', models.CharField(max_length=20, verbose_name='NIT')),
                ('name_company_seller', models.CharField(max_length=50, verbose_name='name_company')),
                ('email_seller', models.CharField(max_length=70, verbose_name='email')),
                ('password_seller', models.CharField(max_length=50, verbose_name='password')),
                ('phone_number_seller', models.CharField(max_length=20, verbose_name='phone_number')),
                ('address', models.CharField(max_length=60, verbose_name='address')),
                ('local_number_seller', models.CharField(blank=True, max_length=8, verbose_name='local_number_seller')),
            ],
        ),
    ]