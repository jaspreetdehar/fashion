# Generated by Django 4.2 on 2023-05-10 08:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pay_status',
            name='orderSTATUS',
            field=models.CharField(choices=[('process', 'process'), ('complete', 'complete')], max_length=12, verbose_name='STATUS'),
        ),
    ]
