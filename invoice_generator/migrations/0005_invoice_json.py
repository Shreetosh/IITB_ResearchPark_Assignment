# Generated by Django 4.1.1 on 2023-04-29 09:55

from django.db import migrations
import jsonfield.fields


class Migration(migrations.Migration):

    dependencies = [
        ('invoice_generator', '0004_items_remove_invoice_amount_remove_invoice_item_name_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='invoice',
            name='json',
            field=jsonfield.fields.JSONField(null=True),
        ),
    ]
