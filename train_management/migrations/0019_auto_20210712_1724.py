# Generated by Django 3.1.6 on 2021-07-12 15:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('train_management', '0018_merge_20210711_1708'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='dayplanning',
            name='paid',
        ),
        migrations.RemoveField(
            model_name='dayplanning',
            name='slot_ordered',
        ),
        migrations.AddField(
            model_name='dayplanning',
            name='billed',
            field=models.TextField(choices=[('yes', 'dayplanning.billed.yes'), ('no', 'dayplanning.billed.no'), ('not_applicable', 'dayplanning.billed.not_applicable')], default='not_applicable', max_length=80, verbose_name='dayplanning.billed'),
        ),
        migrations.AddField(
            model_name='dayplanning',
            name='railway_company',
            field=models.CharField(choices=[('tr', 'dayplanning.railway_company.tr'), ('sbb', 'dayplanning.railway_company.sbb'), ('other', 'dayplanning.railway_company.other')], default='tr', max_length=80, verbose_name='dayplanning.railway_company'),
        ),
        migrations.AddField(
            model_name='dayplanning',
            name='slot_ordered_sbb',
            field=models.CharField(choices=[('open', 'dayplanning.slot.open'), ('ordered', 'dayplanning.slot.ordered'), ('reserved', 'dayplanning.slot.reserved'), ('received', 'dayplanning.slot.received'), ('not_applicable', 'dayplanning.slot.not_applicable')], default='not_applicable', max_length=80, verbose_name='dayplanning.slot_ordered_sbb'),
        ),
        migrations.AddField(
            model_name='dayplanning',
            name='slot_ordered_st',
            field=models.CharField(choices=[('open', 'dayplanning.slot.open'), ('ordered', 'dayplanning.slot.ordered'), ('reserved', 'dayplanning.slot.reserved'), ('received', 'dayplanning.slot.received'), ('not_applicable', 'dayplanning.slot.not_applicable')], default='not_applicable', max_length=80, verbose_name='dayplanning.slot_ordered_st'),
        ),
        migrations.AddField(
            model_name='vehicle',
            name='added_weight',
            field=models.FloatField(blank=True, null=True, verbose_name='vehicle.added_weight'),
        ),
        migrations.AddField(
            model_name='vehicle',
            name='empty_weight',
            field=models.FloatField(blank=True, null=True, verbose_name='vehicle.empty_weight'),
        ),
    ]