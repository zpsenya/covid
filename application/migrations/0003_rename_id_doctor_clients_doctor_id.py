# Generated by Django 4.1.2 on 2022-10-30 08:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('application', '0002_alter_clients_id_doctor'),
    ]

    operations = [
        migrations.RenameField(
            model_name='clients',
            old_name='id_doctor',
            new_name='doctor_id',
        ),
    ]
