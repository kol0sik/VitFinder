# Generated by Django 3.2.9 on 2021-11-13 12:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_product_search'),
    ]

    operations = [
        migrations.RenameField(
            model_name='search',
            old_name='name',
            new_name='search_text',
        ),
    ]
