# Generated by Django 3.1.6 on 2021-06-16 12:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('train_management', '0013_remove_personnel_date_of_birth'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='dayplanning',
            name='text',
        ),
        migrations.AddField(
            model_name='dayplanning',
            name='post_mortem',
            field=models.TextField(blank=True, verbose_name='dayplanning.post_mortem'),
        ),
    ]