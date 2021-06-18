# Generated by Django 3.2.4 on 2021-06-18 09:07

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Company',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('gst_number', models.CharField(max_length=20)),
                ('contact_number', models.CharField(max_length=15)),
            ],
            options={
                'verbose_name_plural': 'companies',
            },
        ),
    ]
