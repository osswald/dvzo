# Generated by Django 3.1.6 on 2021-06-08 09:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('uniforms', '0004_auto_20210608_1027'),
    ]

    operations = [
        migrations.AddField(
            model_name='articlerent',
            name='total_per_month',
            field=models.IntegerField(editable=False, null=True, verbose_name='article_rent.total_per_month'),
        ),
    ]
