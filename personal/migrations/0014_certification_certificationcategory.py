# Generated by Django 3.0.4 on 2020-07-04 10:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('personal', '0013_auto_20200318_0524'),
    ]

    operations = [
        migrations.CreateModel(
            name='CertificationCategory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, unique=True, verbose_name='name')),
            ],
            options={
                'verbose_name': 'Categories of certification',
            },
        ),
        migrations.CreateModel(
            name='Certification',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, unique=True, verbose_name='name')),
                ('slug', models.SlugField(null=True, verbose_name='slug')),
                ('school', models.CharField(max_length=100, unique=True, verbose_name='school')),
                ('picture_branding', models.URLField(verbose_name='picture_branding')),
                ('picture_certification', models.URLField(verbose_name='picture_certification')),
                ('link_certification', models.URLField(verbose_name='link_certification')),
                ('description', models.TextField(verbose_name='description')),
                ('CertificationCategory', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='certifications', to='personal.CertificationCategory', verbose_name='Certification Category')),
            ],
        ),
    ]
