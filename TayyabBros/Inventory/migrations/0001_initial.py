# Generated by Django 3.0.2 on 2020-01-20 17:28

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Customer_Name', models.CharField(max_length=50)),
                ('Phone_no', models.CharField(max_length=20)),
                ('Address', models.CharField(max_length=50)),
                ('CNIC', models.CharField(max_length=50)),
            ],
        ),
    ]
