# Generated by Django 5.0.7 on 2024-07-11 17:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0004_complain_rename_plant_productcart_equipment_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='sportcategory',
            name='Description',
        ),
    ]
