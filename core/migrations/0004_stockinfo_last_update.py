# Generated by Django 4.1.5 on 2023-01-08 23:47

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_alter_stockinfo_ask_size_alter_stockinfo_market_cap_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='stockinfo',
            name='last_update',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]