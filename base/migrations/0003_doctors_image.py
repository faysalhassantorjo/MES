# Generated by Django 4.2.4 on 2023-09-03 13:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0002_doctors'),
    ]

    operations = [
        migrations.AddField(
            model_name='doctors',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
    ]