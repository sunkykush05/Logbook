# Generated by Django 2.2.5 on 2020-03-17 09:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('logbook_app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='inventorymodel',
            name='agency',
            field=models.CharField(choices=[('NS', 'NCS'), ('PL', 'Police'), ('DS', 'DSS'), ('OT', 'Others')], max_length=4),
        ),
        migrations.AlterField(
            model_name='inventorymodel',
            name='place_of_remand',
            field=models.CharField(choices=[('NS', 'NCS'), ('PL', 'Police'), ('DS', 'DSS'), ('OT', 'Others')], max_length=4),
        ),
    ]
