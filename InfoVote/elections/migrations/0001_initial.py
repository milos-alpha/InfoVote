# Generated by Django 5.0.2 on 2025-01-10 02:45

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ElectionRequirement',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('description', models.TextField()),
                ('is_mandatory', models.BooleanField(default=True)),
                ('min_age', models.PositiveIntegerField(validators=[django.core.validators.MinValueValidator(18)])),
                ('document_needed', models.CharField(max_length=200)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
            options={
                'ordering': ['name'],
            },
        ),
        migrations.CreateModel(
            name='Election',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('description', models.TextField()),
                ('election_type', models.CharField(choices=[('PRESIDENTIAL', 'Presidential Election'), ('PARLIAMENTARY', 'Parliamentary Election'), ('LOCAL', 'Local Election'), ('REFERENDUM', 'Referendum')], max_length=20)),
                ('start_date', models.DateTimeField()),
                ('end_date', models.DateTimeField()),
                ('registration_deadline', models.DateTimeField()),
                ('location', models.CharField(max_length=200)),
                ('status', models.CharField(choices=[('UPCOMING', 'Upcoming'), ('ONGOING', 'Ongoing'), ('COMPLETED', 'Completed'), ('CANCELLED', 'Cancelled')], default='UPCOMING', max_length=20)),
                ('total_voters', models.PositiveIntegerField(default=0)),
                ('voter_turnout', models.DecimalField(blank=True, decimal_places=2, max_digits=5, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('requirements', models.ManyToManyField(to='elections.electionrequirement')),
            ],
            options={
                'ordering': ['-start_date'],
                'indexes': [models.Index(fields=['status', 'start_date'], name='elections_e_status_2b6bdc_idx'), models.Index(fields=['election_type'], name='elections_e_electio_88ab4e_idx')],
            },
        ),
    ]
