# Generated by Django 2.2.9 on 2020-02-01 10:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='page',
            name='slug',
            field=models.SlugField(blank=True, help_text='Unique URL slug (leave empty to auto-generate)', max_length=150, unique=True),
        ),
    ]
