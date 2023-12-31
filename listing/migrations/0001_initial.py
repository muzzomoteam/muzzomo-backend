# Generated by Django 4.2.2 on 2023-06-22 06:49

from django.conf import settings
import django.contrib.auth.models
import django.contrib.auth.validators
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='CustomUser',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('username', models.CharField(error_messages={'unique': 'A user with that username already exists.'}, help_text='Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.', max_length=150, unique=True, validators=[django.contrib.auth.validators.UnicodeUsernameValidator()], verbose_name='username')),
                ('first_name', models.CharField(blank=True, max_length=150, verbose_name='first name')),
                ('last_name', models.CharField(blank=True, max_length=150, verbose_name='last name')),
                ('email', models.EmailField(blank=True, max_length=254, verbose_name='email address')),
                ('is_staff', models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status')),
                ('is_active', models.BooleanField(default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('user_type', models.CharField(choices=[('Agent', 'Agent'), ('User', 'User'), ('Expert', 'Expert')], default='Agent', max_length=50)),
                ('profile_image', models.ImageField(upload_to='profiles/')),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.permission', verbose_name='user permissions')),
            ],
            options={
                'verbose_name': 'user',
                'verbose_name_plural': 'users',
                'abstract': False,
            },
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name='Agent',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fullname', models.CharField(max_length=50)),
                ('phone', models.CharField(max_length=20)),
                ('registration_date', models.DateField(auto_now_add=True)),
                ('is_active', models.BooleanField(default=True)),
                ('admin', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Location',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('city', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='ProductAmenitiesModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Air_Conditioning', models.BooleanField(default=True)),
                ('Balcony', models.BooleanField(default=True)),
                ('Garden_Yard', models.BooleanField(default=True)),
                ('Pool', models.BooleanField(default=True)),
                ('Security_System', models.BooleanField(default=True)),
                ('Parking_Space', models.BooleanField(default=True)),
                ('Basement', models.BooleanField(default=True)),
                ('BBQ_Area', models.BooleanField(default=True)),
                ('Walk_in_Closet', models.BooleanField(default=True)),
                ('Central_Heating', models.BooleanField(default=True)),
                ('Deck_Patio', models.BooleanField(default=True)),
                ('Dishwasher', models.BooleanField(default=True)),
                ('Fireplace', models.BooleanField(default=True)),
                ('Fitness_Center_Gym', models.BooleanField(default=True)),
                ('Garage', models.BooleanField(default=True)),
                ('Hardwood_Floors', models.BooleanField(default=True)),
                ('Laundry_Room', models.BooleanField(default=True)),
                ('Washer_Dryer_Hookups', models.BooleanField(default=True)),
                ('Wheelchair_Accessible', models.BooleanField(default=True)),
                ('Pet_Friendly', models.BooleanField(default=True)),
                ('High_Speed_Internet_Access', models.BooleanField(default=True)),
                ('Cable_Satellite_TV', models.BooleanField(default=True)),
                ('Fully_Furnished', models.BooleanField(default=True)),
                ('Gated_Community', models.BooleanField(default=True)),
                ('Tennis_Basketball_Court', models.BooleanField(default=True)),
                ('Playground', models.BooleanField(default=True)),
                ('Elevator', models.BooleanField(default=True)),
                ('Waterfront_Access', models.BooleanField(default=True)),
                ('Close_to_Public_Transportation', models.BooleanField(default=True)),
                ('Proximity_to_Schools', models.BooleanField(default=True)),
                ('Nearby_Shopping_Restaurants', models.BooleanField(default=True)),
                ('Access_to_Parks_Recreational_Areas', models.BooleanField(default=True)),
                ('On_Site_Maintenance', models.BooleanField(default=True)),
                ('On_Site_Management', models.BooleanField(default=True)),
                ('Hour_Security', models.BooleanField(default=True)),
                ('Energy_Efficient_Appliances', models.BooleanField(default=True)),
                ('Green_Building_Features', models.BooleanField(default=True)),
                ('Smart_Home_Technology', models.BooleanField(default=True)),
                ('Outdoor_Entertaining_Area', models.BooleanField(default=True)),
                ('Wine_Cellar', models.BooleanField(default=True)),
                ('Home_Theater', models.BooleanField(default=True)),
                ('Office_Study_Room', models.BooleanField(default=True)),
                ('Guest_House_In_Law_Suite', models.BooleanField(default=True)),
                ('Game_Room', models.BooleanField(default=True)),
                ('Vaulted_Ceilings', models.BooleanField(default=True)),
                ('Skylights', models.BooleanField(default=True)),
                ('Workshop_Studio_Space', models.BooleanField(default=True)),
                ('Solar_Panels', models.BooleanField(default=True)),
                ('Mountain_City_View', models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name='ProductPropertyModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tile', models.CharField(max_length=100)),
                ('description', models.CharField(max_length=4000)),
                ('type', models.CharField(max_length=200)),
                ('city', models.CharField(max_length=200)),
                ('status', models.CharField(max_length=200)),
                ('postal_Code', models.CharField(max_length=100)),
                ('floor', models.IntegerField()),
                ('bed', models.IntegerField()),
                ('bath', models.IntegerField()),
                ('room', models.IntegerField()),
                ('area', models.IntegerField()),
                ('lotarea', models.IntegerField()),
                ('price', models.FloatField()),
                ('grauge', models.CharField(max_length=100)),
                ('medai_url', models.CharField(max_length=400)),
                ('coverPhoto', models.ImageField(upload_to='ProductCoverPhoto/')),
                ('amenities', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='listing.productamenitiesmodel')),
            ],
        ),
        migrations.CreateModel(
            name='WishList',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='listing.productpropertymodel')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='ProducttRate',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comment', models.TextField()),
                ('rate', models.IntegerField()),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='listing.productpropertymodel')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='ProductImageModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='ProductImage/')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='listing.productpropertymodel')),
            ],
        ),
        migrations.CreateModel(
            name='Expert',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fullname', models.CharField(max_length=50)),
                ('phone', models.CharField(max_length=50)),
                ('registration_date', models.DateField(auto_now_add=True)),
                ('is_active', models.BooleanField(default=True)),
                ('admin', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('location', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='listing.location')),
            ],
        ),
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fullname', models.CharField(max_length=50)),
                ('phone', models.CharField(max_length=50)),
                ('registration_date', models.DateField(auto_now_add=True)),
                ('is_active', models.BooleanField(default=True)),
                ('admin', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('location', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='listing.location')),
            ],
        ),
        migrations.CreateModel(
            name='AgentRate',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comment', models.TextField()),
                ('rate', models.IntegerField()),
                ('agent', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='listing.agent')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='agent',
            name='location',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='listing.location'),
        ),
    ]
