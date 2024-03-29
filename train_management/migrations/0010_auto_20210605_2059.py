# Generated by Django 3.1.6 on 2021-06-05 18:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('train_management', '0009_auto_20210604_1420'),
    ]

    operations = [
        migrations.AddField(
            model_name='reservation',
            name='comment',
            field=models.TextField(blank=True, null=True, verbose_name='reservation.comment'),
        ),
        migrations.AddField(
            model_name='reservation',
            name='end',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='end_reservation', to='train_management.station'),
        ),
        migrations.AddField(
            model_name='reservation',
            name='start',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='start_reservation', to='train_management.station'),
        ),
    ]
