# Generated by Django 3.2.3 on 2021-05-27 05:52

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='PatientModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=128)),
                ('age', models.CharField(max_length=128)),
                ('dependents', models.CharField(max_length=128)),
                ('address', models.CharField(max_length=128)),
                ('healthIssues', models.CharField(max_length=128)),
            ],
        ),
    ]