# Generated by Django 2.0.7 on 2022-08-03 05:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0003_auto_20220803_0451'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='Isavailable',
            field=models.BooleanField(default=True),
            preserve_default=False,
        ),
    ]
