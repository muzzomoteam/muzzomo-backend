# Generated by Django 4.2.2 on 2023-06-19 09:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('listing', '0003_alter_feature_coverimage_alter_feature_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='agent',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to='listing.agent'),
        ),
    ]
