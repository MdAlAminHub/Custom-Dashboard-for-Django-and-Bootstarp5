# Generated by Django 3.2.8 on 2021-11-30 08:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0003_auto_20211129_1540'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='description_bangla',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='product',
            name='description_english',
            field=models.TextField(),
        ),
    ]
