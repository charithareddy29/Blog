# Generated by Django 5.0.6 on 2024-06-11 07:17

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Destination',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('img', models.ImageField(upload_to='pictures')),
                ('desc', models.TextField()),
                ('offer', models.BooleanField(default=False)),
            ],
        ),
    ]
