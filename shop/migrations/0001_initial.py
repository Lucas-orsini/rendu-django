# Generated by Django 4.0.2 on 2022-03-01 09:29

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('prdocutname', models.CharField(max_length=500)),
                ('productprice', models.IntegerField()),
                ('productimage', models.CharField(max_length=500)),
                ('productdescription', models.CharField(max_length=800)),
                ('productquantity', models.IntegerField()),
            ],
        ),
    ]