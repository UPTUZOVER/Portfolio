# Generated by Django 5.0.4 on 2024-04-21 15:28

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portifolya', '0004_rename_services_service_alter_link_options_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('location', models.CharField(blank=True, max_length=100, null=True, verbose_name='Manzilingizni kiriting: ')),
                ('phone_number', models.CharField(blank=True, max_length=20, null=True, validators=[django.core.validators.RegexValidator(message="To'g'ri telefon raqamini kiriting.", regex='^\\+?998\\d{9}$')], verbose_name='Telefon raqamingizni keriting')),
                ('email', models.EmailField(blank=True, max_length=70, null=True, verbose_name='Email manzilingizni kiriting')),
                ('website', models.URLField(blank=True, null=True, verbose_name='Website manzilingizni kiriting')),
            ],
            options={
                'verbose_name': 'Manzil keritildi',
                'verbose_name_plural': 'Manzillari keritildi',
            },
        ),
        migrations.AlterModelOptions(
            name='service',
            options={},
        ),
    ]
