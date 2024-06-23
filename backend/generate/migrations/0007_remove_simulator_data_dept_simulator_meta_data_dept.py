# Generated by Django 5.0.6 on 2024-06-17 15:32

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('generate', '0006_simulator_meta_data_alter_simulator_data_options_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='simulator_data',
            name='dept',
        ),
        migrations.AddField(
            model_name='simulator_meta_data',
            name='dept',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to='generate.department'),
        ),
    ]