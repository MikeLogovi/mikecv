# Generated by Django 3.0.4 on 2020-07-04 12:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('personal', '0015_auto_20200704_1151'),
    ]

    operations = [
        migrations.AddField(
            model_name='certificationcategory',
            name='slug',
            field=models.SlugField(null=True, verbose_name='slug'),
        ),
    ]
