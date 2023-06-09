# Generated by Django 4.1.1 on 2023-04-28 14:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('invoice_generator', '0003_alter_invoice_quantity'),
    ]

    operations = [
        migrations.CreateModel(
            name='Items',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('item_name', models.CharField(max_length=100, null=True)),
                ('quantity', models.FloatField(null=True)),
                ('price', models.FloatField(null=True)),
                ('tax', models.FloatField(null=True)),
                ('amount', models.FloatField(null=True)),
            ],
        ),
        migrations.RemoveField(
            model_name='invoice',
            name='amount',
        ),
        migrations.RemoveField(
            model_name='invoice',
            name='item_name',
        ),
        migrations.RemoveField(
            model_name='invoice',
            name='price',
        ),
        migrations.RemoveField(
            model_name='invoice',
            name='quantity',
        ),
        migrations.RemoveField(
            model_name='invoice',
            name='tax',
        ),
    ]
