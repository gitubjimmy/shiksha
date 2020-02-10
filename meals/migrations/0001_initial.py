# Generated by Django 3.0.2 on 2020-02-08 15:01

import django.contrib.postgres.fields
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='College',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('en_name', models.TextField()),
                ('kr_name', models.TextField()),
                ('created', models.DateTimeField(default=django.utils.timezone.now)),
            ],
        ),
        migrations.CreateModel(
            name='Meal',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('en_name', models.TextField()),
                ('kr_name', models.TextField()),
                ('price', models.TextField()),
                ('created', models.DateTimeField(default=django.utils.timezone.now)),
                ('etc', models.TextField(default='')),
            ],
        ),
        migrations.CreateModel(
            name='Review',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('score', models.IntegerField()),
                ('deviece', models.TextField()),
                ('device_type', models.CharField(blank=True, choices=[('A', 'android'), ('I', 'ios'), ('W', 'web')], max_length=1)),
                ('created', models.DateTimeField(default=django.utils.timezone.now)),
                ('meal', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='meals.Meal')),
            ],
        ),
        migrations.CreateModel(
            name='Restaurant',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.TextField()),
                ('en_name', django.contrib.postgres.fields.ArrayField(base_field=models.TextField(), size=None)),
                ('kr_name', django.contrib.postgres.fields.ArrayField(base_field=models.TextField(), size=None)),
                ('operating_hours', models.TextField()),
                ('hours_breakfast', models.TextField()),
                ('hours_lunch', models.TextField()),
                ('hours_dinner', models.TextField()),
                ('location', models.TextField()),
                ('latitude', models.DecimalField(decimal_places=6, max_digits=9, null=True)),
                ('longitude', models.DecimalField(decimal_places=6, max_digits=9, null=True)),
                ('created', models.DateTimeField(default=django.utils.timezone.now)),
                ('college', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='meals.College')),
            ],
        ),
        migrations.CreateModel(
            name='Menu',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('type', models.CharField(blank=True, choices=[('BR', 'breakfast'), ('LU', 'lunch'), ('DN', 'dinner')], max_length=2)),
                ('meals', models.ManyToManyField(to='meals.Meal')),
                ('restaurant', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='meals.Restaurant')),
            ],
        ),
        migrations.AddField(
            model_name='meal',
            name='restuarant',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='meals.Restaurant'),
        ),
    ]