# Generated by Django 4.1.3 on 2022-11-22 07:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('emp', '0005_emppersonaldetails_photo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='empaddressdetails',
            name='city',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='empaddressdetails',
            name='state',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='empaddressdetails',
            name='street',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
