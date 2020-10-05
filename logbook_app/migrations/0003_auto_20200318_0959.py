# Generated by Django 2.2.5 on 2020-03-18 08:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('logbook_app', '0002_auto_20200317_1043'),
    ]

    operations = [
        migrations.AddField(
            model_name='inventorymodel',
            name='export_to_CSV',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='inventorymodel',
            name='case_no',
            field=models.CharField(blank=True, max_length=25),
        ),
        migrations.AlterField(
            model_name='inventorymodel',
            name='court',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AlterField(
            model_name='inventorymodel',
            name='court_no',
            field=models.CharField(blank=True, max_length=15),
        ),
        migrations.AlterField(
            model_name='inventorymodel',
            name='entry_made_by',
            field=models.CharField(blank=True, max_length=200),
        ),
        migrations.AlterField(
            model_name='inventorymodel',
            name='file_no',
            field=models.CharField(blank=True, max_length=25),
        ),
    ]
