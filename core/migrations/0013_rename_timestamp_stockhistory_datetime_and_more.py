# Generated by Django 4.1.5 on 2023-01-14 07:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0012_rename_date_stockhistory_timestamp'),
    ]

    operations = [
        migrations.RenameField(
            model_name='stockhistory',
            old_name='timestamp',
            new_name='datetime',
        ),
        migrations.AddField(
            model_name='stockhistory',
            name='openinterest',
            field=models.IntegerField(default=0),
        ),
    ]