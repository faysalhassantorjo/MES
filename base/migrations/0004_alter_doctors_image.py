# Generated by Django 4.2.4 on 2023-09-03 13:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0003_doctors_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='doctors',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='doctors/'),
        ),
    ]
