# Generated by Django 4.1.1 on 2023-04-27 05:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('invoice_generator', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='invoice',
            name='amount',
            field=models.FloatField(null=True),
        ),
        migrations.AlterField(
            model_name='invoice',
            name='price',
            field=models.FloatField(null=True),
        ),
        migrations.AlterField(
            model_name='invoice',
            name='quantity',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='invoice',
            name='tax',
            field=models.FloatField(null=True),
        ),
    ]
