# Generated by Django 4.2 on 2023-06-16 12:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0003_contact'),
    ]

    operations = [
        migrations.CreateModel(
            name='Orders',
            fields=[
                ('order_id', models.AutoField(primary_key=True, serialize=False)),
                ('items_json', models.TextField()),
                ('name', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=100)),
                ('address', models.CharField(max_length=300)),
                ('city', models.CharField(max_length=70)),
                ('state', models.CharField(max_length=70)),
                ('zip_code', models.CharField(max_length=5)),
                ('phone_number', models.CharField(max_length=10)),
            ],
        ),
    ]
