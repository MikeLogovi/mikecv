# Generated by Django 3.0.4 on 2020-07-04 18:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('personal', '0019_certification_picture_certification'),
    ]

    operations = [
        migrations.AddField(
            model_name='certification',
            name='school_url',
            field=models.CharField(max_length=100, null=True, verbose_name='school_url'),
        ),
    ]
