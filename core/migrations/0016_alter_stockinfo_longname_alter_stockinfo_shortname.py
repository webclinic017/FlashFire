# Generated by Django 4.1.5 on 2023-01-05 13:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0015_alter_stockinfo_debttoequity'),
    ]

    operations = [
        migrations.AlterField(
            model_name='stockinfo',
            name='longName',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='stockinfo',
            name='shortName',
            field=models.CharField(max_length=50, null=True),
        ),
    ]