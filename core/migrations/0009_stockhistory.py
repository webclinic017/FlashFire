# Generated by Django 4.1.5 on 2023-01-12 02:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0008_delete_stockhistory'),
    ]

    operations = [
        migrations.CreateModel(
            name='StockHistory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('open', models.DecimalField(decimal_places=3, default=0.0, max_digits=15, null=True)),
                ('high', models.DecimalField(decimal_places=3, default=0.0, max_digits=15, null=True)),
                ('low', models.DecimalField(decimal_places=3, default=0.0, max_digits=15, null=True)),
                ('close', models.DecimalField(decimal_places=3, default=0.0, max_digits=15, null=True)),
                ('volume', models.BigIntegerField(null=True)),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('stock', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='history', to='core.stockinfo')),
            ],
        ),
    ]