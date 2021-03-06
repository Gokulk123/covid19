# Generated by Django 3.0.4 on 2020-06-03 02:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('covid19_app', '0002_medical_details'),
    ]

    operations = [
        migrations.CreateModel(
            name='symptoms',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fever', models.CharField(max_length=100)),
                ('cough', models.CharField(max_length=100)),
                ('tiredness', models.CharField(max_length=100)),
                ('chest_pain', models.CharField(max_length=100)),
                ('headache', models.CharField(max_length=100)),
                ('breathing', models.CharField(max_length=100)),
                ('speech', models.CharField(max_length=100)),
                ('taste', models.CharField(max_length=100)),
            ],
        ),
    ]
