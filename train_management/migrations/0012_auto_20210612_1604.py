# Generated by Django 3.1.6 on 2021-06-12 14:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('train_management', '0011_auto_20210609_1311'),
    ]

    operations = [
        migrations.AlterField(
            model_name='personnel',
            name='category',
            field=models.ManyToManyField(blank=True, to='train_management.PersonnelCategory'),
        ),
    ]
