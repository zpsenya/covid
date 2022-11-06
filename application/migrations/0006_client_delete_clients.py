# Generated by Django 4.1.2 on 2022-11-02 18:55

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('application', '0005_delete_users'),
    ]

    operations = [
        migrations.CreateModel(
            name='Client',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField(max_length=80)),
                ('surname', models.TextField(max_length=80)),
                ('time_create', models.DateTimeField(auto_now_add=True, verbose_name='Time of create')),
                ('time_update', models.DateTimeField(auto_now=True, verbose_name='Time of update')),
                ('time_of_analyse', models.DateTimeField(verbose_name='Time of analyse')),
                ('email', models.EmailField(max_length=254)),
                ('is_corona', models.BooleanField(default=False)),
                ('doctor_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.DeleteModel(
            name='Clients',
        ),
    ]
