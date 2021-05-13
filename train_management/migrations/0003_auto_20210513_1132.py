# Generated by Django 3.1.6 on 2021-05-13 09:32

from django.db import migrations, models
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    dependencies = [
        ('train_management', '0002_auto_20210513_0920'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='availability',
            options={'verbose_name': 'availability.singular', 'verbose_name_plural': 'availability.plural'},
        ),
        migrations.AlterModelOptions(
            name='dayplanning',
            options={'verbose_name': 'dayplanning.singular', 'verbose_name_plural': 'dayplanning.plural'},
        ),
        migrations.AlterModelOptions(
            name='dvzofunction',
            options={'verbose_name': 'dvzo_function.singular', 'verbose_name_plural': 'dvzo_function.plural'},
        ),
        migrations.AlterModelOptions(
            name='mileage',
            options={'verbose_name': 'mileage.singular', 'verbose_name_plural': 'mileage.plural'},
        ),
        migrations.AlterModelOptions(
            name='personnel',
            options={'verbose_name': 'personnel.singular', 'verbose_name_plural': 'personnel.plural'},
        ),
        migrations.AlterModelOptions(
            name='phonenumber',
            options={'verbose_name': 'phone_number.singular', 'verbose_name_plural': 'phone_number.plural'},
        ),
        migrations.AlterModelOptions(
            name='reservation',
            options={'verbose_name': 'reservation.singular', 'verbose_name_plural': 'reservation.plural'},
        ),
        migrations.AlterModelOptions(
            name='route',
            options={'verbose_name': 'route.singular', 'verbose_name_plural': 'route.plural'},
        ),
        migrations.AlterModelOptions(
            name='station',
            options={'verbose_name': 'station.singular', 'verbose_name_plural': 'station.plural'},
        ),
        migrations.AlterModelOptions(
            name='train',
            options={'verbose_name': 'train.singular', 'verbose_name_plural': 'train.plural'},
        ),
        migrations.AlterModelOptions(
            name='trainconfiguration',
            options={'verbose_name': 'train_configuration.singular', 'verbose_name_plural': 'train_configuration.plural'},
        ),
        migrations.AlterModelOptions(
            name='traintimetable',
            options={'verbose_name': 'train_timetable.singular', 'verbose_name_plural': 'train_timetable.plural'},
        ),
        migrations.AlterModelOptions(
            name='traintimetabletemplate',
            options={'verbose_name': 'train_timetable_template.singular', 'verbose_name_plural': 'train_timetable_template.plural'},
        ),
        migrations.AlterModelOptions(
            name='vehicle',
            options={'verbose_name': 'vehicle.singular', 'verbose_name_plural': 'vehicle.plural'},
        ),
        migrations.AlterField(
            model_name='availability',
            name='availability_status',
            field=models.CharField(choices=[('in_use', 'availability.availability_status.in_use'), ('ask', 'availability.availability_status.ask'), ('servicing', 'availability.availability_status.servicing'), ('locked', 'availability.availability_status.locked')], default='servicing', max_length=80, verbose_name='availability.status'),
        ),
        migrations.AlterField(
            model_name='dayplanning',
            name='booking_status',
            field=models.CharField(choices=[('proposal', 'dayplanning.booking_status.proposal'), ('reservation', 'dayplanning.booking_status.reservation'), ('booked', 'dayplanning.booking_status.booked'), ('cancelled_dvzo', 'dayplanning.booking_status.cancelled_dvzo'), ('cancelled_customer', 'dayplanning.booking_status.cancelled_customer'), ('not_applicable', 'dayplanning.booking_status.not_applicable')], default='not_applicable', max_length=80, verbose_name='dayplanning.booking_status'),
        ),
        migrations.AlterField(
            model_name='dayplanning',
            name='comment',
            field=models.TextField(blank=True, verbose_name='dayplanning.comment'),
        ),
        migrations.AlterField(
            model_name='dayplanning',
            name='customers',
            field=models.IntegerField(blank=True, null=True, verbose_name='dayplanning.customers'),
        ),
        migrations.AlterField(
            model_name='dayplanning',
            name='date',
            field=models.DateField(verbose_name='dayplanning.date'),
        ),
        migrations.AlterField(
            model_name='dayplanning',
            name='day_planning_type',
            field=models.CharField(choices=[('sunday', 'dayplanning.type.sunday'), ('extra', 'dayplanning.type.extra'), ('other', 'dayplanning.type.other')], max_length=80, verbose_name='dayplanning.day_planning_type'),
        ),
        migrations.AlterField(
            model_name='dayplanning',
            name='label',
            field=models.CharField(max_length=200, verbose_name='dayplanning.label'),
        ),
        migrations.AlterField(
            model_name='dayplanning',
            name='paid',
            field=models.TextField(choices=[('yes', 'dayplanning.paid.yes'), ('no', 'dayplanning.paid.no'), ('not_applicable', 'dayplanning.paid.not_applicable')], default='not_applicable', max_length=80, verbose_name='dayplanning.paid'),
        ),
        migrations.AlterField(
            model_name='dayplanning',
            name='personnel_disposition',
            field=models.CharField(choices=[('open', 'dayplanning.personnel_disposition.open'), ('disposed', 'dayplanning.personnel_disposition.disposed'), ('not_applicable', 'dayplanning.personnel_disposition.not_applicable')], default='open', max_length=80, verbose_name='dayplanning.personnel_disposition'),
        ),
        migrations.AlterField(
            model_name='dayplanning',
            name='price',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=8, null=True, verbose_name='dayplanning.price'),
        ),
        migrations.AlterField(
            model_name='dayplanning',
            name='slot_ordered',
            field=models.CharField(choices=[('open', 'dayplanning.slot.open'), ('ordered', 'dayplanning.slot.ordered'), ('received', 'dayplanning.slot.received'), ('not_applicable', 'dayplanning.slot.received')], default='not_applicable', max_length=80, verbose_name='slot ordered'),
        ),
        migrations.AlterField(
            model_name='dayplanning',
            name='status',
            field=models.CharField(choices=[('draft', 'dayplanning.status.draft'), ('confirmed', 'dayplanning.status.confirmed'), ('executed', 'dayplanning.status.executed')], max_length=80, verbose_name='dayplanning.status'),
        ),
        migrations.AlterField(
            model_name='dayplanning',
            name='text',
            field=models.TextField(blank=True, max_length=5000, verbose_name='dayplanning.text'),
        ),
        migrations.AlterField(
            model_name='dvzofunction',
            name='function_type',
            field=models.CharField(choices=[('train', 'dvzo_function.function_type.train'), ('bauma', 'dvzo_function.function_type.bauma'), ('neuthal', 'dvzo_function.function_type.neuthal'), ('baeretswil', 'dvzo_function.function_type.baeretswil'), ('hinwil', 'dvzo_function.function_type.hinwil')], max_length=80, verbose_name='dvzo_function.function_type'),
        ),
        migrations.AlterField(
            model_name='dvzofunction',
            name='label',
            field=models.CharField(max_length=200, verbose_name='dvzo_function.label'),
        ),
        migrations.AlterField(
            model_name='dvzofunction',
            name='label_short',
            field=models.CharField(max_length=80, verbose_name='dvzo_function.label_short'),
        ),
        migrations.AlterField(
            model_name='dvzofunction',
            name='sorting',
            field=models.IntegerField(blank=True, null=True, verbose_name='dvzo_function.sorting'),
        ),
        migrations.AlterField(
            model_name='mileage',
            name='date',
            field=models.DateField(verbose_name='mileage.date'),
        ),
        migrations.AlterField(
            model_name='mileage',
            name='label',
            field=models.CharField(blank=True, max_length=200, verbose_name='mileage.label'),
        ),
        migrations.AlterField(
            model_name='personnel',
            name='date_of_birth',
            field=models.DateField(blank=True, null=True, verbose_name='personnel.date_of_birth'),
        ),
        migrations.AlterField(
            model_name='personnel',
            name='mobile_phone',
            field=phonenumber_field.modelfields.PhoneNumberField(blank=True, max_length=128, region=None, verbose_name='personnel.mobile_phone'),
        ),
        migrations.AlterField(
            model_name='personnel',
            name='mobile_phone_public',
            field=models.CharField(choices=[('yes', 'personnel.personnel_mobile_public.yes'), ('no', 'personnel.personnel_mobile_public.no'), ('unknown', 'personnel.personnel_mobile_public.unknown')], default='unknown', max_length=80, verbose_name='personnel.personnel_mobile_public'),
        ),
        migrations.AlterField(
            model_name='personnel',
            name='status',
            field=models.CharField(choices=[('active', 'personnel.personnel_status.active'), ('inactive', 'personnel.personnel_status.inactive')], max_length=80, verbose_name='personnel.status'),
        ),
        migrations.AlterField(
            model_name='phonenumber',
            name='label',
            field=models.CharField(max_length=200, verbose_name='phone_number.label'),
        ),
        migrations.AlterField(
            model_name='phonenumber',
            name='phone_number',
            field=phonenumber_field.modelfields.PhoneNumberField(max_length=128, region=None, verbose_name='phone_number.phone_number'),
        ),
        migrations.AlterField(
            model_name='phonenumber',
            name='phone_number_type',
            field=models.CharField(choices=[('sbb', 'phone_number.type.sbb'), ('emergency', 'phone_number.type.emergency'), ('dvzo', 'phone_number.type.dvzo'), ('other', 'phone_number.type.other')], max_length=80, verbose_name='phone_number.type'),
        ),
        migrations.AlterField(
            model_name='reservation',
            name='amount',
            field=models.IntegerField(verbose_name='reservation.amount'),
        ),
        migrations.AlterField(
            model_name='reservation',
            name='email',
            field=models.EmailField(blank=True, max_length=254, verbose_name='reservation.email'),
        ),
        migrations.AlterField(
            model_name='reservation',
            name='label',
            field=models.CharField(max_length=200, verbose_name='reservation.label'),
        ),
        migrations.AlterField(
            model_name='reservation',
            name='phone',
            field=phonenumber_field.modelfields.PhoneNumberField(blank=True, max_length=128, region=None, verbose_name='reservation.phone'),
        ),
        migrations.AlterField(
            model_name='reservation',
            name='reservation_status',
            field=models.CharField(choices=[('proposal', 'reservation.status.proposal'), ('confirmed', 'reservation.status.confirmed')], default='confirmed', max_length=80, verbose_name='reservation.status'),
        ),
        migrations.AlterField(
            model_name='reservation',
            name='reservation_type',
            field=models.CharField(choices=[('gastro', 'reservation.type.gastro'), ('seating', 'reservation.type.seating')], max_length=80, verbose_name='reservation.type'),
        ),
        migrations.AlterField(
            model_name='station',
            name='didok_nr',
            field=models.CharField(blank=True, max_length=200, verbose_name='station.didok_nr'),
        ),
        migrations.AlterField(
            model_name='station',
            name='label',
            field=models.CharField(max_length=200, verbose_name='station.label'),
        ),
        migrations.AlterField(
            model_name='station',
            name='label_short',
            field=models.CharField(max_length=5, verbose_name='station.label_short'),
        ),
        migrations.AlterField(
            model_name='train',
            name='km',
            field=models.IntegerField(blank=True, verbose_name='train.km'),
        ),
        migrations.AlterField(
            model_name='train',
            name='label',
            field=models.CharField(max_length=200, verbose_name='train.label'),
        ),
        migrations.AlterField(
            model_name='trainconfiguration',
            name='sorting',
            field=models.IntegerField(blank=True, null=True, verbose_name='train_configuration.sorting'),
        ),
        migrations.AlterField(
            model_name='traintimetabletemplate',
            name='active',
            field=models.CharField(choices=[('yes', 'train_timetable_template.active.yes'), ('no', 'train_timetable_template.active.no')], default='yes', max_length=50, verbose_name='train_timetable_template.active'),
        ),
        migrations.AlterField(
            model_name='traintimetabletemplate',
            name='comment',
            field=models.TextField(blank=True, verbose_name='train_timetable_template.description'),
        ),
        migrations.AlterField(
            model_name='traintimetabletemplate',
            name='destination_time',
            field=models.TimeField(blank=True, null=True, verbose_name='train_timetable_template.destination_time'),
        ),
        migrations.AlterField(
            model_name='traintimetabletemplate',
            name='label',
            field=models.CharField(max_length=200, verbose_name='train_timetable_template.label'),
        ),
        migrations.AlterField(
            model_name='traintimetabletemplate',
            name='start_time',
            field=models.TimeField(blank=True, null=True, verbose_name='train_timetable_template.start_time'),
        ),
        migrations.AlterField(
            model_name='traintimetabletemplate',
            name='template_name',
            field=models.CharField(max_length=200, verbose_name='train_timetable_template.template_name'),
        ),
        migrations.AlterField(
            model_name='vehicle',
            name='axles_distance',
            field=models.FloatField(blank=True, null=True, verbose_name='vehicles.axles_distance'),
        ),
        migrations.AlterField(
            model_name='vehicle',
            name='carriage_type',
            field=models.CharField(blank=True, choices=[('seat', 'vehicle.carriage_type.seat'), ('gastro', 'vehicle.carriage_type.gastro'), ('luggage', 'vehicle.carriage_type.luggage'), ('cargo', 'vehicle.carriage_type.cargo')], max_length=80, verbose_name='vehiclecarriage_type'),
        ),
        migrations.AlterField(
            model_name='vehicle',
            name='description',
            field=models.TextField(blank=True, verbose_name='vehicle.description'),
        ),
        migrations.AlterField(
            model_name='vehicle',
            name='gross_weight',
            field=models.FloatField(blank=True, null=True, verbose_name='vehicle.gross_weight'),
        ),
        migrations.AlterField(
            model_name='vehicle',
            name='historic_name',
            field=models.CharField(blank=True, max_length=200, verbose_name='vehicle.historic_name'),
        ),
        migrations.AlterField(
            model_name='vehicle',
            name='home',
            field=models.CharField(choices=[('bauma', 'vehicle.home.bauma'), ('uster', 'vehicle.home.uster'), ('wald', 'vehicle.home.wald')], max_length=80, verbose_name='vehicle.home'),
        ),
        migrations.AlterField(
            model_name='vehicle',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='', verbose_name='vehicle.image'),
        ),
        migrations.AlterField(
            model_name='vehicle',
            name='label',
            field=models.CharField(max_length=200, verbose_name='vehicle.label'),
        ),
        migrations.AlterField(
            model_name='vehicle',
            name='last_revision',
            field=models.DateField(blank=True, null=True, verbose_name='vehicle.last_revision'),
        ),
        migrations.AlterField(
            model_name='vehicle',
            name='length',
            field=models.FloatField(blank=True, null=True, verbose_name='vehicles.length'),
        ),
        migrations.AlterField(
            model_name='vehicle',
            name='manufacturer',
            field=models.CharField(blank=True, max_length=200, verbose_name='vehicles.manufacturer'),
        ),
        migrations.AlterField(
            model_name='vehicle',
            name='max_speed',
            field=models.IntegerField(blank=True, null=True, verbose_name='vehicles.maximum_speed'),
        ),
        migrations.AlterField(
            model_name='vehicle',
            name='next_revision',
            field=models.DateField(blank=True, null=True, verbose_name='vehicle.next_revision'),
        ),
        migrations.AlterField(
            model_name='vehicle',
            name='power_unit',
            field=models.CharField(choices=[('steam', 'vehicle.power_unit.steam'), ('diesel', 'vehicle.power_unit.diesel'), ('electric', 'vehicle.power_unit.electric'), ('dieselelectric', 'vehicle.power_unit.dieselelectric')], max_length=80, verbose_name='vehicles.power_unit'),
        ),
        migrations.AlterField(
            model_name='vehicle',
            name='seats',
            field=models.IntegerField(blank=True, null=True, verbose_name='vehicle.seats'),
        ),
        migrations.AlterField(
            model_name='vehicle',
            name='start_year',
            field=models.IntegerField(blank=True, null=True, verbose_name='vehicle.start_year'),
        ),
        migrations.AlterField(
            model_name='vehicle',
            name='status',
            field=models.CharField(choices=[('available', 'vehicle.status.available'), ('servicing', 'vehicle.status.servicing'), ('ask', 'vehicle.status.ask')], default='available', max_length=80, verbose_name='vehicle.status'),
        ),
        migrations.AlterField(
            model_name='vehicle',
            name='steam_heating',
            field=models.CharField(choices=[('no', 'vehicle.steam_heating.no'), ('front', 'vehicle.steam_heating.front'), ('back', 'vehicle.steam_heating.back'), ('both', 'vehicle.steam_heating.both')], max_length=80, verbose_name='vehicles.steam_heating'),
        ),
        migrations.AlterField(
            model_name='vehicle',
            name='traction_25',
            field=models.IntegerField(blank=True, null=True, verbose_name='vehicles.traction_25'),
        ),
        migrations.AlterField(
            model_name='vehicle',
            name='traction_30',
            field=models.IntegerField(blank=True, null=True, verbose_name='vehicles.traction_30'),
        ),
        migrations.AlterField(
            model_name='vehicle',
            name='uic',
            field=models.CharField(blank=True, max_length=200, verbose_name='vehicle.uic'),
        ),
        migrations.AlterField(
            model_name='vehicle',
            name='vehicle_type',
            field=models.CharField(choices=[('engine', 'vehicle.type.engine'), ('carriage', 'vehicle.type.carriage')], max_length=80, verbose_name='vehicle.type'),
        ),
    ]