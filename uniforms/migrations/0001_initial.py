# Generated by Django 3.1.6 on 2021-06-07 10:44

from django.db import migrations, models
import django.db.models.deletion
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('train_management', '0009_auto_20210604_1420'),
    ]

    operations = [
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('label', models.CharField(max_length=200, verbose_name='article.label')),
                ('category', models.CharField(choices=[('coat', 'article.article_category.coat'), ('hat', 'article.article_category.hat'), ('misc', 'article.article_category.misc'), ('shirt', 'article.article_category.shirt'), ('shoes', 'article.article_category.shoes'), ('vest', 'article.article_category.vest'), ('tie', 'article.article_category.tie'), ('trousers', 'article.article_category.trousers')], max_length=80, verbose_name='article.category')),
                ('status', models.CharField(choices=[('active', 'article.article_status.active'), ('inactive', 'article.article_status.inactive')], default='active', max_length=80, verbose_name='article.status')),
                ('amount', models.IntegerField(blank=True, null=True, verbose_name='article.amount')),
                ('price', models.DecimalField(decimal_places=2, max_digits=5, verbose_name='article.price')),
            ],
            options={
                'verbose_name': 'article.singular',
                'verbose_name_plural': 'article.plural',
            },
        ),
        migrations.CreateModel(
            name='Renter',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, verbose_name='renter.name')),
                ('street', models.CharField(max_length=200, verbose_name='renter.street')),
                ('zip', models.CharField(max_length=200, verbose_name='renter.zip')),
                ('city', models.CharField(max_length=200, verbose_name='renter.city')),
                ('phone', phonenumber_field.modelfields.PhoneNumberField(max_length=128, region=None, verbose_name='renter.phone')),
                ('email', models.CharField(max_length=200, verbose_name='renter.email')),
            ],
            options={
                'verbose_name': 'renter.singular',
                'verbose_name_plural': 'renter.plural',
            },
        ),
        migrations.CreateModel(
            name='CoatArticle',
            fields=[
                ('article_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='uniforms.article')),
                ('size', models.IntegerField(blank=True, null=True, verbose_name='article.coat.size')),
            ],
            options={
                'verbose_name': 'article.coat.singular',
                'verbose_name_plural': 'article.coat.plural',
            },
            bases=('uniforms.article',),
        ),
        migrations.CreateModel(
            name='HatArticle',
            fields=[
                ('article_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='uniforms.article')),
                ('circumference', models.IntegerField(blank=True, null=True, verbose_name='article.hat.circumference')),
            ],
            options={
                'verbose_name': 'article.hat.singular',
                'verbose_name_plural': 'article.hat.plural',
            },
            bases=('uniforms.article',),
        ),
        migrations.CreateModel(
            name='MiscArticle',
            fields=[
                ('article_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='uniforms.article')),
                ('type', models.CharField(choices=[('whistle', 'article.misc_article_type.whistle')], max_length=80, verbose_name='article.misc.type')),
            ],
            options={
                'verbose_name': 'article.misc.singular',
                'verbose_name_plural': 'article.misc.plural',
            },
            bases=('uniforms.article',),
        ),
        migrations.CreateModel(
            name='ShirtArticle',
            fields=[
                ('article_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='uniforms.article')),
                ('size', models.IntegerField(blank=True, null=True, verbose_name='article.shirt.size')),
            ],
            options={
                'verbose_name': 'article.shirt.singular',
                'verbose_name_plural': 'article.shirt.plural',
            },
            bases=('uniforms.article',),
        ),
        migrations.CreateModel(
            name='ShoesArticle',
            fields=[
                ('article_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='uniforms.article')),
                ('size', models.IntegerField(blank=True, null=True, verbose_name='article.shoes.size')),
            ],
            options={
                'verbose_name': 'article.shoes.singular',
                'verbose_name_plural': 'article.shoes.plural',
            },
            bases=('uniforms.article',),
        ),
        migrations.CreateModel(
            name='TieArticle',
            fields=[
                ('article_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='uniforms.article')),
                ('length', models.IntegerField(blank=True, null=True, verbose_name='article.tie.length')),
            ],
            options={
                'verbose_name': 'article.tie.singular',
                'verbose_name_plural': 'article.tie.plural',
            },
            bases=('uniforms.article',),
        ),
        migrations.CreateModel(
            name='TrousersArticle',
            fields=[
                ('article_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='uniforms.article')),
                ('waist', models.IntegerField(blank=True, null=True, verbose_name='article.trousers.waist')),
                ('length', models.IntegerField(blank=True, null=True, verbose_name='article.trousers.length')),
            ],
            options={
                'verbose_name': 'article.trousers.singular',
                'verbose_name_plural': 'article.trousers.plural',
            },
            bases=('uniforms.article',),
        ),
        migrations.CreateModel(
            name='VestArticle',
            fields=[
                ('article_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='uniforms.article')),
                ('size', models.IntegerField(blank=True, null=True, verbose_name='article.vest.size')),
            ],
            options={
                'verbose_name': 'article.vest.singular',
                'verbose_name_plural': 'article.vest.plural',
            },
            bases=('uniforms.article',),
        ),
        migrations.CreateModel(
            name='Rent',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('start', models.DateField(verbose_name='rent.start')),
                ('end', models.DateField(verbose_name='rent.start')),
                ('returned', models.CharField(choices=[('yes', 'rent.returned.yes'), ('no', 'rent.returned.no')], default='no', max_length=80, verbose_name='rent.returned')),
                ('billed', models.BooleanField(verbose_name='rent.billed')),
                ('total_per_month', models.DecimalField(decimal_places=2, max_digits=8, verbose_name='rent.total_per_month')),
                ('total', models.DecimalField(decimal_places=2, max_digits=8, verbose_name='rent.total')),
                ('renter', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='uniforms.renter')),
            ],
            options={
                'verbose_name': 'rent.singular',
                'verbose_name_plural': 'rent.plural',
            },
        ),
        migrations.CreateModel(
            name='Let',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('start', models.DateField(verbose_name='let.start')),
                ('end', models.DateField(verbose_name='let.end')),
                ('returned', models.CharField(choices=[('yes', 'let.returned.yes'), ('no', 'let.returned.no')], default='no', max_length=80, verbose_name='let.returned')),
                ('personnel', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='train_management.personnel')),
            ],
            options={
                'verbose_name': 'let.singular',
                'verbose_name_plural': 'let.plural',
            },
        ),
        migrations.CreateModel(
            name='ArticleRent',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount', models.IntegerField(verbose_name='article_rent.amount')),
                ('article', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='uniforms.article')),
                ('rent', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='uniforms.rent')),
            ],
            options={
                'verbose_name': 'article_rent.singular',
                'verbose_name_plural': 'article_rent.plural',
            },
        ),
        migrations.CreateModel(
            name='ArticleLet',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount', models.IntegerField(verbose_name='article_let.amount')),
                ('article', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='uniforms.article')),
                ('let', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='uniforms.let')),
            ],
            options={
                'verbose_name': 'article_let.singular',
                'verbose_name_plural': 'article_let.plural',
            },
        ),
    ]
