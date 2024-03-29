# Generated by Django 3.1.6 on 2021-05-13 07:20

from django.db import migrations, models
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    dependencies = [
        ('train_management', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='personnel',
            name='mobile_phone',
            field=phonenumber_field.modelfields.PhoneNumberField(blank=True, max_length=128, region=None, verbose_name='mobile phone'),
        ),
        migrations.AlterField(
            model_name='station',
            name='neighbours',
            field=models.ManyToManyField(blank=True, related_name='_station_neighbours_+', to='train_management.Station'),
        ),
    ]
