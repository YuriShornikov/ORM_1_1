# Generated by Django 4.1.7 on 2023-04-04 18:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('phones', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='phone',
            name='image',
            field=models.CharField(max_length=200),
        ),
    ]
