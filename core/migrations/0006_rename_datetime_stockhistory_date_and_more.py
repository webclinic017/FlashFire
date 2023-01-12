# Generated by Django 4.1.5 on 2023-01-11 14:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0005_alter_stockinfo_last_update'),
    ]

    operations = [
        migrations.RenameField(
            model_name='stockhistory',
            old_name='datetime',
            new_name='date',
        ),
        migrations.RenameField(
            model_name='stockhistory',
            old_name='stock_id',
            new_name='symbol',
        ),
        migrations.RemoveField(
            model_name='stockhistory',
            name='open_price',
        ),
        migrations.AddField(
            model_name='stockhistory',
            name='open',
            field=models.DecimalField(decimal_places=3, default=0.0, max_digits=15, null=True),
        ),
        migrations.AlterField(
            model_name='stockhistory',
            name='close',
            field=models.DecimalField(decimal_places=3, default=0.0, max_digits=15, null=True),
        ),
        migrations.AlterField(
            model_name='stockhistory',
            name='high',
            field=models.DecimalField(decimal_places=3, default=0.0, max_digits=15, null=True),
        ),
        migrations.AlterField(
            model_name='stockhistory',
            name='low',
            field=models.DecimalField(decimal_places=3, default=0.0, max_digits=15, null=True),
        ),
        migrations.AlterField(
            model_name='stockhistory',
            name='volume',
            field=models.BigIntegerField(null=True),
        ),
    ]