# Generated by Django 4.0.2 on 2022-03-01 09:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0002_rename_prdocutname_product_productname'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='productimage',
            field=models.CharField(max_length=100000),
        ),
    ]