# Generated by Django 4.1.5 on 2023-01-05 12:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0013_alter_stockinfo_currentratio'),
    ]

    operations = [
        migrations.AlterField(
            model_name='stockinfo',
            name='quickRatio',
            field=models.DecimalField(decimal_places=3, max_digits=8, null=True),
        ),
    ]