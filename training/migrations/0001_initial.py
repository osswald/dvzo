# Generated by Django 3.1.6 on 2021-06-12 16:28

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django_currentuser.db.models.fields
import django_currentuser.middleware


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('train_management', '0011_auto_20210609_1311'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='MedicalFitnessLevel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('create_timestamp', models.DateTimeField(auto_now_add=True, null=True, verbose_name='create_timestamp')),
                ('update_timestamp', models.DateTimeField(auto_now=True, null=True, verbose_name='update_timestamp')),
                ('label', models.CharField(max_length=200, verbose_name='medical_fitness_level.label')),
                ('create_user', django_currentuser.db.models.fields.CurrentUserField(default=django_currentuser.middleware.get_current_authenticated_user, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='created_medicalfitnesslevels', to=settings.AUTH_USER_MODEL)),
                ('update_user', django_currentuser.db.models.fields.CurrentUserField(default=django_currentuser.middleware.get_current_authenticated_user, null=True, on_delete=django.db.models.deletion.CASCADE, on_update=True, related_name='updated_medicalfitnesslevels', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'medical_fitness_level.singular',
                'verbose_name_plural': 'medical_fitness_level.plural',
            },
        ),
        migrations.CreateModel(
            name='PeriodicExam',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('create_timestamp', models.DateTimeField(auto_now_add=True, null=True, verbose_name='create_timestamp')),
                ('update_timestamp', models.DateTimeField(auto_now=True, null=True, verbose_name='update_timestamp')),
                ('date', models.DateField(blank=True, null=True, verbose_name='periodic_exam.date')),
                ('create_user', django_currentuser.db.models.fields.CurrentUserField(default=django_currentuser.middleware.get_current_authenticated_user, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='created_periodicexams', to=settings.AUTH_USER_MODEL)),
                ('personnel', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='train_management.personnel')),
            ],
            options={
                'verbose_name': 'periodic_exam.singular',
                'verbose_name_plural': 'periodic_exam.plural',
            },
        ),
        migrations.CreateModel(
            name='Qualification',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('create_timestamp', models.DateTimeField(auto_now_add=True, null=True, verbose_name='create_timestamp')),
                ('update_timestamp', models.DateTimeField(auto_now=True, null=True, verbose_name='update_timestamp')),
                ('label', models.CharField(blank=True, max_length=200, verbose_name='qualification.label')),
                ('description', models.TextField(verbose_name='qualification.description')),
                ('type', models.CharField(choices=[('vte', 'qualification.type.vte'), ('zstebv', 'qualification.type.zstebv'), ('dvzo', 'qualification.type.dvzo')], max_length=80, verbose_name='qualification.type')),
                ('valid_years', models.IntegerField(verbose_name='qualification.valid_years')),
                ('create_user', django_currentuser.db.models.fields.CurrentUserField(default=django_currentuser.middleware.get_current_authenticated_user, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='created_qualifications', to=settings.AUTH_USER_MODEL)),
                ('update_user', django_currentuser.db.models.fields.CurrentUserField(default=django_currentuser.middleware.get_current_authenticated_user, null=True, on_delete=django.db.models.deletion.CASCADE, on_update=True, related_name='updated_qualifications', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'qualification.singular',
                'verbose_name_plural': 'qualification.plural',
            },
        ),
        migrations.CreateModel(
            name='Training',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('create_timestamp', models.DateTimeField(auto_now_add=True, null=True, verbose_name='create_timestamp')),
                ('update_timestamp', models.DateTimeField(auto_now=True, null=True, verbose_name='update_timestamp')),
                ('label', models.CharField(max_length=200, verbose_name='training.label')),
                ('course_label', models.CharField(max_length=200, verbose_name='training.course_label')),
                ('start_date', models.DateField(blank=True, null=True, verbose_name='training.start_date')),
                ('end_date', models.DateField(blank=True, null=True, verbose_name='training.end_date')),
                ('create_user', django_currentuser.db.models.fields.CurrentUserField(default=django_currentuser.middleware.get_current_authenticated_user, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='created_trainings', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'training.singular',
                'verbose_name_plural': 'training.plural',
            },
        ),
        migrations.CreateModel(
            name='TrainingModule',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('create_timestamp', models.DateTimeField(auto_now_add=True, null=True, verbose_name='create_timestamp')),
                ('update_timestamp', models.DateTimeField(auto_now=True, null=True, verbose_name='update_timestamp')),
                ('label', models.CharField(blank=True, max_length=200, verbose_name='module.label')),
                ('label_short', models.CharField(max_length=5, verbose_name='module.label_short')),
                ('description', models.TextField(verbose_name='module.description')),
                ('create_user', django_currentuser.db.models.fields.CurrentUserField(default=django_currentuser.middleware.get_current_authenticated_user, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='created_trainingmodules', to=settings.AUTH_USER_MODEL)),
                ('update_user', django_currentuser.db.models.fields.CurrentUserField(default=django_currentuser.middleware.get_current_authenticated_user, null=True, on_delete=django.db.models.deletion.CASCADE, on_update=True, related_name='updated_trainingmodules', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'module.singular',
                'verbose_name_plural': 'module.plural',
            },
        ),
        migrations.CreateModel(
            name='TrainingDate',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('create_timestamp', models.DateTimeField(auto_now_add=True, null=True, verbose_name='create_timestamp')),
                ('update_timestamp', models.DateTimeField(auto_now=True, null=True, verbose_name='update_timestamp')),
                ('label', models.CharField(blank=True, max_length=200, null=True, verbose_name='training_date.label')),
                ('start_datetime', models.DateTimeField(blank=True, null=True, verbose_name='training_date.start_date')),
                ('end_datetime', models.DateTimeField(blank=True, null=True, verbose_name='training_date.end_date')),
                ('create_user', django_currentuser.db.models.fields.CurrentUserField(default=django_currentuser.middleware.get_current_authenticated_user, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='created_trainingdates', to=settings.AUTH_USER_MODEL)),
                ('responsible', models.ManyToManyField(blank=True, related_name='training_date_responsible', to='train_management.Personnel')),
                ('training', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='training.training')),
                ('update_user', django_currentuser.db.models.fields.CurrentUserField(default=django_currentuser.middleware.get_current_authenticated_user, null=True, on_delete=django.db.models.deletion.CASCADE, on_update=True, related_name='updated_trainingdates', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'training_date.singular',
                'verbose_name_plural': 'training_date.plural',
            },
        ),
        migrations.AddField(
            model_name='training',
            name='module',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='training.trainingmodule'),
        ),
        migrations.AddField(
            model_name='training',
            name='responsible',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='train_management.personnel'),
        ),
        migrations.AddField(
            model_name='training',
            name='update_user',
            field=django_currentuser.db.models.fields.CurrentUserField(default=django_currentuser.middleware.get_current_authenticated_user, null=True, on_delete=django.db.models.deletion.CASCADE, on_update=True, related_name='updated_trainings', to=settings.AUTH_USER_MODEL),
        ),
        migrations.CreateModel(
            name='Requirement',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('create_timestamp', models.DateTimeField(auto_now_add=True, null=True, verbose_name='create_timestamp')),
                ('update_timestamp', models.DateTimeField(auto_now=True, null=True, verbose_name='update_timestamp')),
                ('create_user', django_currentuser.db.models.fields.CurrentUserField(default=django_currentuser.middleware.get_current_authenticated_user, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='created_requirements', to=settings.AUTH_USER_MODEL)),
                ('medical_fitness', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='training.medicalfitnesslevel')),
                ('module', models.ManyToManyField(blank=True, to='training.TrainingModule')),
                ('periodic_exam', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='training.periodicexam')),
                ('qualification', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='training.qualification')),
                ('update_user', django_currentuser.db.models.fields.CurrentUserField(default=django_currentuser.middleware.get_current_authenticated_user, null=True, on_delete=django.db.models.deletion.CASCADE, on_update=True, related_name='updated_requirements', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'requirement.singular',
                'verbose_name_plural': 'requirement.plural',
            },
        ),
        migrations.CreateModel(
            name='PersonnelQualification',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('create_timestamp', models.DateTimeField(auto_now_add=True, null=True, verbose_name='create_timestamp')),
                ('update_timestamp', models.DateTimeField(auto_now=True, null=True, verbose_name='update_timestamp')),
                ('valid_until', models.DateField(verbose_name='personnel_qualification.valid_until')),
                ('automatically_added', models.BooleanField(verbose_name='personnel_qualification.automatically_added')),
                ('create_user', django_currentuser.db.models.fields.CurrentUserField(default=django_currentuser.middleware.get_current_authenticated_user, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='created_personnelqualifications', to=settings.AUTH_USER_MODEL)),
                ('personnel', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='train_management.personnel')),
                ('qualification', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='training.qualification')),
                ('update_user', django_currentuser.db.models.fields.CurrentUserField(default=django_currentuser.middleware.get_current_authenticated_user, null=True, on_delete=django.db.models.deletion.CASCADE, on_update=True, related_name='updated_personnelqualifications', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'personnel_qualification.singular',
                'verbose_name_plural': 'personnel_qualification.plural',
            },
        ),
        migrations.AddField(
            model_name='periodicexam',
            name='qualification',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='training.qualification'),
        ),
        migrations.AddField(
            model_name='periodicexam',
            name='update_user',
            field=django_currentuser.db.models.fields.CurrentUserField(default=django_currentuser.middleware.get_current_authenticated_user, null=True, on_delete=django.db.models.deletion.CASCADE, on_update=True, related_name='updated_periodicexams', to=settings.AUTH_USER_MODEL),
        ),
        migrations.CreateModel(
            name='Participant',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('create_timestamp', models.DateTimeField(auto_now_add=True, null=True, verbose_name='create_timestamp')),
                ('update_timestamp', models.DateTimeField(auto_now=True, null=True, verbose_name='update_timestamp')),
                ('attended', models.BooleanField(verbose_name='participant.attended')),
                ('passed', models.BooleanField(verbose_name='participant.passed')),
                ('create_user', django_currentuser.db.models.fields.CurrentUserField(default=django_currentuser.middleware.get_current_authenticated_user, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='created_participants', to=settings.AUTH_USER_MODEL)),
                ('personnel', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='train_management.personnel')),
                ('update_user', django_currentuser.db.models.fields.CurrentUserField(default=django_currentuser.middleware.get_current_authenticated_user, null=True, on_delete=django.db.models.deletion.CASCADE, on_update=True, related_name='updated_participants', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'participant.singular',
                'verbose_name_plural': 'participant.plural',
            },
        ),
        migrations.CreateModel(
            name='MedicalFitness',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('create_timestamp', models.DateTimeField(auto_now_add=True, null=True, verbose_name='create_timestamp')),
                ('update_timestamp', models.DateTimeField(auto_now=True, null=True, verbose_name='update_timestamp')),
                ('date', models.DateField(blank=True, null=True, verbose_name='medical_fitness.date')),
                ('create_user', django_currentuser.db.models.fields.CurrentUserField(default=django_currentuser.middleware.get_current_authenticated_user, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='created_medicalfitnesss', to=settings.AUTH_USER_MODEL)),
                ('level', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='training.medicalfitnesslevel')),
                ('personnel', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='train_management.personnel')),
                ('update_user', django_currentuser.db.models.fields.CurrentUserField(default=django_currentuser.middleware.get_current_authenticated_user, null=True, on_delete=django.db.models.deletion.CASCADE, on_update=True, related_name='updated_medicalfitnesss', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'medical_fitness.singular',
                'verbose_name_plural': 'medical_fitness.plural',
            },
        ),
        migrations.CreateModel(
            name='Attendance',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('create_timestamp', models.DateTimeField(auto_now_add=True, null=True, verbose_name='create_timestamp')),
                ('update_timestamp', models.DateTimeField(auto_now=True, null=True, verbose_name='update_timestamp')),
                ('attended', models.BooleanField(verbose_name='attendance.attended')),
                ('create_user', django_currentuser.db.models.fields.CurrentUserField(default=django_currentuser.middleware.get_current_authenticated_user, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='created_attendances', to=settings.AUTH_USER_MODEL)),
                ('participant', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='training.participant')),
                ('training_date', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='training.trainingdate')),
                ('update_user', django_currentuser.db.models.fields.CurrentUserField(default=django_currentuser.middleware.get_current_authenticated_user, null=True, on_delete=django.db.models.deletion.CASCADE, on_update=True, related_name='updated_attendances', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'attendance.singular',
                'verbose_name_plural': 'attendance.plural',
            },
        ),
    ]
