# Generated by Django 3.2.2 on 2021-05-08 20:45

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='DayPlanning',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('label', models.CharField(max_length=200, verbose_name='label')),
                ('day_planning_type', models.CharField(choices=[('sunday', 'Sunday'), ('extra', 'Extra'), ('other', 'Other')], max_length=80, verbose_name='day_planning_type')),
                ('date', models.DateField(verbose_name='date')),
                ('status', models.CharField(choices=[('draft', 'Draft'), ('confirmed', 'Confirmed'), ('executed', 'Executed')], max_length=80, verbose_name='status')),
                ('paid', models.TextField(choices=[('yes', 'Yes'), ('no', 'No'), ('not_applicable', 'Not applicable')], default='not_applicable', max_length=80, verbose_name='paid')),
                ('text', models.TextField(blank=True, max_length=5000, verbose_name='Text')),
                ('slot_ordered', models.CharField(choices=[('open', 'Open'), ('ordered', 'Ordered'), ('received', 'Received'), ('not_applicable', 'Not applicable')], default='not_applicable', max_length=80, verbose_name='slot ordered')),
                ('personnel_disposition', models.CharField(choices=[('open', 'Open'), ('disposed', 'Disposed'), ('not_applicable', 'Not applicable')], default='open', max_length=80, verbose_name='Personnel disposition')),
                ('customers', models.IntegerField(blank=True, null=True, verbose_name='Number of customers')),
                ('price', models.DecimalField(blank=True, decimal_places=2, max_digits=8, null=True, verbose_name='Price')),
                ('booking_status', models.CharField(choices=[('proposal', 'Proposal'), ('reservation', 'Reservation'), ('booked', 'Booked'), ('cancelled_dvzo', 'Cancelled DVZO'), ('cancelled_customer', 'Cancelled customer'), ('not_applicable', 'Not applicable')], default='not_applicable', max_length=80, verbose_name='Booking status')),
                ('comment', models.TextField(blank=True, verbose_name='Comment')),
            ],
            options={
                'verbose_name': 'Day planning',
                'verbose_name_plural': 'Day plannings',
            },
        ),
        migrations.CreateModel(
            name='DvzoFunction',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('label', models.CharField(max_length=200, verbose_name='label')),
                ('label_short', models.CharField(max_length=80, verbose_name='label short')),
                ('sorting', models.IntegerField(blank=True, null=True)),
                ('function_type', models.CharField(choices=[('train', 'Train'), ('bauma', 'Bauma'), ('neuthal', 'Neuthal'), ('baeretswil', 'Bäretswil'), ('hinwil', 'Hinwil')], max_length=80, verbose_name='function_type')),
            ],
            options={
                'verbose_name': 'Function',
                'verbose_name_plural': 'Functions',
            },
        ),
        migrations.CreateModel(
            name='FunctionPersons',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dvzo_function', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='train_management.dvzofunction')),
            ],
        ),
        migrations.CreateModel(
            name='PhoneNumber',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('label', models.CharField(max_length=200, verbose_name='label')),
                ('phone_number', phonenumber_field.modelfields.PhoneNumberField(max_length=128, region=None, verbose_name='Phone number')),
                ('phone_number_type', models.CharField(choices=[('sbb', 'SBB'), ('emergency', 'Emergency'), ('dvzo', 'DVZO'), ('other', 'Other')], max_length=80, verbose_name='Phone number type')),
            ],
            options={
                'verbose_name': 'Phone number',
                'verbose_name_plural': 'Phone numbers',
            },
        ),
        migrations.CreateModel(
            name='Station',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('didok_nr', models.CharField(blank=True, max_length=200, verbose_name='DIDOK Nr.')),
                ('label_short', models.CharField(max_length=5, verbose_name='label short')),
                ('label', models.CharField(max_length=200, verbose_name='label')),
                ('neighbours', models.ManyToManyField(related_name='_train_management_station_neighbours_+', to='train_management.Station')),
            ],
            options={
                'verbose_name': 'Betriebspunkt',
                'verbose_name_plural': 'Betriebspunkte',
            },
        ),
        migrations.CreateModel(
            name='Train',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('label', models.CharField(max_length=200, verbose_name='label')),
                ('km', models.IntegerField(blank=True, verbose_name='km')),
                ('day_planning', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='train_management.dayplanning')),
                ('function_persons', models.ManyToManyField(related_name='train', to='train_management.FunctionPersons')),
            ],
            options={
                'verbose_name': 'Train tour',
                'verbose_name_plural': 'Train tours',
            },
        ),
        migrations.CreateModel(
            name='Vehicle',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('label', models.CharField(max_length=200, verbose_name='label')),
                ('historic_name', models.CharField(blank=True, max_length=200, verbose_name='historic_name')),
                ('description', models.TextField(blank=True, verbose_name='description')),
                ('uic', models.CharField(blank=True, max_length=200, verbose_name='UIC')),
                ('image', models.ImageField(blank=True, null=True, upload_to='', verbose_name='image')),
                ('gross_weight', models.FloatField(blank=True, null=True, verbose_name='gross_weight')),
                ('seats', models.IntegerField(blank=True, null=True, verbose_name='seats')),
                ('vehicle_type', models.CharField(choices=[('engine', 'Engine'), ('carriage', 'Carriage')], max_length=80, verbose_name='vehicle type')),
                ('status', models.CharField(choices=[('available', 'Available'), ('servicing', 'In Servicing'), ('ask', 'Ask')], default='available', max_length=80, verbose_name='status')),
                ('carriage_type', models.CharField(blank=True, choices=[('seat', 'Seating Car'), ('gastro', 'Waggon Restaurant'), ('luggage', 'Luggage'), ('cargo', 'Cargo')], max_length=80, verbose_name='carriage_type')),
                ('home', models.CharField(choices=[('bauma', 'Bauma'), ('uster', 'Uster'), ('wald', 'Wald ZH')], max_length=80, verbose_name='home')),
                ('start_year', models.IntegerField(blank=True, null=True, verbose_name='start year')),
                ('last_revision', models.DateField(blank=True, null=True, verbose_name='last revision')),
                ('next_revision', models.DateField(blank=True, null=True, verbose_name='next revision')),
                ('axles_distance', models.FloatField(blank=True, null=True, verbose_name='axles distance')),
                ('length', models.FloatField(blank=True, null=True, verbose_name='length')),
                ('manufacturer', models.CharField(blank=True, max_length=200, verbose_name='manufacturer')),
                ('traction_25', models.IntegerField(blank=True, null=True, verbose_name='traction 25 permille')),
                ('traction_30', models.IntegerField(blank=True, null=True, verbose_name='traction 30 permille')),
                ('power_unit', models.CharField(choices=[('steam', 'Steam'), ('diesel', 'Diesel'), ('electric', 'Electric'), ('dieselelectric', 'Diesel/Electric')], max_length=80, verbose_name='power_unit')),
                ('steam_heating', models.CharField(choices=[('no', 'No'), ('front', 'Front'), ('back', 'Back'), ('both', 'Front and Back')], max_length=80, verbose_name='steam_heating')),
                ('max_speed', models.IntegerField(blank=True, null=True, verbose_name='maximum speed')),
            ],
            options={
                'verbose_name': 'Vehicle',
                'verbose_name_plural': 'Vehicles',
            },
        ),
        migrations.CreateModel(
            name='TrainTimetableTemplate',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('template_name', models.CharField(max_length=200, verbose_name='template name')),
                ('label', models.CharField(max_length=200, verbose_name='label')),
                ('start_time', models.TimeField(blank=True, null=True, verbose_name='start time')),
                ('destination_time', models.TimeField(blank=True, null=True, verbose_name='destination time')),
                ('comment', models.TextField(blank=True, verbose_name='description')),
                ('active', models.CharField(choices=[('yes', 'Yes'), ('no', 'No')], default='yes', max_length=50, verbose_name='active')),
                ('destination_station', models.ForeignKey(null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='destination_station_template', to='train_management.station')),
                ('start_station', models.ForeignKey(null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='start_station_template', to='train_management.station')),
                ('train', models.ForeignKey(null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='train_management.train')),
            ],
            options={
                'verbose_name': 'Train timetable template',
                'verbose_name_plural': 'Train timetable templates',
            },
        ),
        migrations.CreateModel(
            name='TrainTimetable',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('label', models.CharField(max_length=200, verbose_name='train_timetable.label')),
                ('start_time', models.TimeField(blank=True, null=True, verbose_name='train_timetable.start time')),
                ('destination_time', models.TimeField(blank=True, null=True, verbose_name='train_timetable.destination time')),
                ('comment', models.TextField(blank=True, verbose_name='train_timetable.description')),
                ('reservation_internal', models.CharField(choices=[('not_possible', 'train_timetable.reservation_possible.not_possible'), ('possible', 'train_timetable.reservation_possible.possible')], default='not_possible', max_length=80, verbose_name='train_timetable.reservation_internal')),
                ('reservation_external', models.CharField(choices=[('not_possible', 'train_timetable.reservation_possible.not_possible'), ('possible', 'train_timetable.reservation_possible.possible')], default='not_possible', max_length=80, verbose_name='train_timetable.reservation_external')),
                ('destination_station', models.ForeignKey(null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='destination_station', to='train_management.station')),
                ('start_station', models.ForeignKey(null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='start_station', to='train_management.station')),
                ('train', models.ForeignKey(null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='train_management.train')),
            ],
            options={
                'verbose_name': 'train_timetable.single',
                'verbose_name_plural': 'train_timetable.plural',
            },
        ),
        migrations.CreateModel(
            name='TrainConfiguration',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sorting', models.IntegerField(blank=True, null=True, verbose_name='sorting')),
                ('train', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='train_management.train')),
                ('vehicle', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='train_management.vehicle')),
            ],
            options={
                'verbose_name': 'Train configuration',
                'verbose_name_plural': 'Train configurations',
            },
        ),
        migrations.CreateModel(
            name='Route',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('arrival', models.TimeField(blank=True, null=True, verbose_name='route.arrival')),
                ('departure', models.TimeField(blank=True, null=True, verbose_name='route.departure')),
                ('reason', models.CharField(choices=[('no_stop', 'route.reason.no_stop'), ('no_stop_diff', 'route.reason.no_stop_diff'), ('start', 'route.reason.start'), ('end', 'route.reason.end'), ('stop', 'route.reason.stop')], max_length=80, verbose_name='route.reason')),
                ('ordering', models.IntegerField(verbose_name='route.ordering')),
                ('station', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='train_management.station')),
                ('traintimetable', models.ForeignKey(null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='train_management.traintimetable')),
            ],
            options={
                'verbose_name': 'Route',
                'verbose_name_plural': 'Routes',
            },
        ),
        migrations.CreateModel(
            name='Reservation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('label', models.CharField(max_length=200, verbose_name='label')),
                ('phone', phonenumber_field.modelfields.PhoneNumberField(blank=True, max_length=128, region=None, verbose_name='phone')),
                ('email', models.EmailField(blank=True, max_length=254, verbose_name='email')),
                ('amount', models.IntegerField(verbose_name='number of people')),
                ('reservation_type', models.CharField(choices=[('gastro', 'Gastro'), ('seating', 'Seating')], max_length=80, verbose_name='reservation type')),
                ('reservation_status', models.CharField(choices=[('proposal', 'Proposal'), ('confirmed', 'Confirmed')], default='confirmed', max_length=80, verbose_name='reservation status')),
                ('train_timetable', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='train_management.traintimetable')),
            ],
            options={
                'verbose_name': 'Reservation',
                'verbose_name_plural': 'Reservations',
            },
        ),
        migrations.CreateModel(
            name='Personnel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('mobile_phone', phonenumber_field.modelfields.PhoneNumberField(max_length=128, region=None, verbose_name='mobile phone')),
                ('status', models.CharField(choices=[('active', 'Active'), ('inactive', 'Inactive')], max_length=80, verbose_name='status')),
                ('mobile_phone_public', models.CharField(choices=[('yes', 'Yes'), ('no', 'No'), ('unknown', 'Unknown')], default='unknown', max_length=80, verbose_name='mobile phone publicly available')),
                ('date_of_birth', models.DateField(blank=True, null=True, verbose_name='date of birth')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Personnel',
                'verbose_name_plural': 'Personnel',
            },
        ),
        migrations.CreateModel(
            name='Mileage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(verbose_name='date')),
                ('label', models.CharField(blank=True, max_length=200, verbose_name='label')),
                ('train', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='train_management.train')),
            ],
            options={
                'verbose_name': 'Mileage',
                'verbose_name_plural': 'Mileages',
            },
        ),
        migrations.AddField(
            model_name='functionpersons',
            name='person',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='train_management.personnel'),
        ),
        migrations.AddField(
            model_name='dayplanning',
            name='function_persons',
            field=models.ManyToManyField(related_name='dayplanning', to='train_management.FunctionPersons'),
        ),
        migrations.CreateModel(
            name='Availability',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('start', models.DateField(verbose_name='availability.start')),
                ('end', models.DateField(verbose_name='availability.end')),
                ('availability_status', models.CharField(choices=[('in_use', 'availability.availability_status.in_use'), ('ask', 'availability.availability_status.ask'), ('servicing', 'availability.availability_status.servicing'), ('locked', 'availability.availability_status.locked')], default='servicing', max_length=80, verbose_name='Status')),
                ('dayplanning', models.ForeignKey(null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='train_management.dayplanning')),
                ('vehicle', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='train_management.vehicle')),
            ],
            options={
                'verbose_name': 'Availability',
                'verbose_name_plural': 'Availabilities',
            },
        ),
    ]
