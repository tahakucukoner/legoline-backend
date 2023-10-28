# Generated by Django 4.2.6 on 2023-10-28 16:29

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('workstations', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ForemanInfo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('worker_name', models.CharField(max_length=100, null=True)),
                ('worker_surname', models.CharField(max_length=100, null=True)),
                ('worker_tel_no', models.CharField(max_length=100, null=True)),
                ('worker_task_time', models.FloatField(default=0)),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='created at')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='update at')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('worker_workstation', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='workstations.workstations')),
            ],
        ),
    ]
