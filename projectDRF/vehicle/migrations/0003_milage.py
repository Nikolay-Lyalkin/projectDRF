# Generated by Django 5.1.4 on 2024-12-15 20:25

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vehicle', '0002_moto'),
    ]

    operations = [
        migrations.CreateModel(
            name='Milage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('milage', models.PositiveIntegerField(verbose_name='пробег')),
                ('year', models.SmallIntegerField(verbose_name='год')),
                ('car', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='vehicle.car')),
                ('moto', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='vehicle.moto')),
            ],
            options={
                'verbose_name': '',
                'verbose_name_plural': '',
                'ordering': ('-year',),
            },
        ),
    ]
