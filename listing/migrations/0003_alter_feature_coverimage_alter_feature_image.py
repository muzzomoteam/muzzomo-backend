# Generated by Django 4.2.2 on 2023-06-17 12:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('listing', '0002_alter_customuser_profile_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='feature',
            name='coverimage',
            field=models.ImageField(upload_to='coverImage/'),
        ),
        migrations.AlterField(
            model_name='feature',
            name='image',
            field=models.ImageField(upload_to='apartmentImage/'),
        ),
    ]