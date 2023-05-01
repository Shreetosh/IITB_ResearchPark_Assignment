# Generated by Django 4.1.1 on 2023-05-01 04:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('invoice_generator', '0008_remove_invoice_price_alter_invoice_amount_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Add_Items',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('item_name', models.CharField(max_length=100, null=True)),
                ('price', models.FloatField(null=True)),
                ('tax', models.FloatField(null=True)),
                ('amount', models.FloatField(null=True)),
            ],
        ),
    ]