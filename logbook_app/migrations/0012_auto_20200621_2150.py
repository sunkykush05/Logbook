# Generated by Django 2.2.5 on 2020-06-21 20:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('logbook_app', '0011_auto_20200621_2131'),
    ]

    operations = [
        migrations.AlterField(
            model_name='attorneymodel',
            name='counsel_telephone',
            field=models.IntegerField(),
        ),
    ]
