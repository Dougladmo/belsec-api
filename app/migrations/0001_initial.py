# Generated by Django 5.0.4 on 2024-04-24 23:26

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Report',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tipo', models.CharField(max_length=100)),
                ('description', models.TextField()),
                ('address', models.CharField(max_length=255)),
                ('time', models.DateTimeField()),
                ('image', models.ImageField(upload_to='report_images')),
            ],
        ),
    ]