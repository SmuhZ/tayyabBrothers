# Generated by Django 3.0.2 on 2020-01-21 18:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Inventory', '0003_items'),
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Date', models.DateField(default=0)),
                ('TAmount', models.IntegerField()),
                ('Customer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Inventory.Customer')),
            ],
        ),
        migrations.CreateModel(
            name='Status',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Status_Name', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='OrderDetails',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Quantity', models.IntegerField()),
                ('Amount', models.IntegerField()),
                ('Item', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Inventory.Items')),
                ('Order', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Inventory.Order')),
            ],
        ),
        migrations.AddField(
            model_name='order',
            name='Status',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Inventory.Status'),
        ),
    ]
