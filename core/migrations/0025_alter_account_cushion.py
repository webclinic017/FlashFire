# Generated by Django 4.1.5 on 2023-02-10 05:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0024_remove_position_transaction_id_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='account',
            name='Cushion',
            field=models.FloatField(),
        ),
    ]
