# Generated by Django 3.2.6 on 2021-09-10 17:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='balance',
            name='balance',
            field=models.PositiveIntegerField(blank=True, null=True),
        ),
    ]
