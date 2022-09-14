# Generated by Django 4.0.6 on 2022-08-08 12:23

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('user_app', '0003_alter_customer_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='user',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='customer', to=settings.AUTH_USER_MODEL),
        ),
    ]