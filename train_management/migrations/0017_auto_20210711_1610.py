# Generated by Django 3.1.6 on 2021-07-11 14:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('train_management', '0016_auto_20210624_1712'),
    ]

    operations = [
        migrations.DeleteModel(
            name='TrainTimetableTemplate',
        ),
        migrations.CreateModel(
            name='TrainTimetableTemplate',
            fields=[
                ('traintimetable_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='train_management.traintimetable')),
                ('template_name', models.CharField(max_length=200, verbose_name='train_timetable_template.template_name')),
                ('active', models.CharField(choices=[('yes', 'train_timetable_template.active.yes'), ('no', 'train_timetable_template.active.no')], default='yes', max_length=50, verbose_name='train_timetable_template.active')),
            ],
            options={
                'verbose_name': 'train_timetable_template.singular',
                'verbose_name_plural': 'train_timetable_template.plural',
            },
            bases=('train_management.traintimetable',),
        ),
    ]
