# Generated by Django 3.0.4 on 2020-06-08 12:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('covid19_app', '0010_symp_result'),
    ]

    operations = [
        migrations.CreateModel(
            name='message',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('u_id', models.CharField(default='SOME STRING', max_length=100)),
                ('message', models.CharField(default='SOME STRING', max_length=1000)),
            ],
        ),
    ]