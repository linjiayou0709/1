# Generated by Django 3.2.18 on 2023-10-28 14:24

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('first', '0008_auto_20231028_2222'),
    ]

    operations = [
        migrations.AlterField(
            model_name='preference',
            name='user',
            field=models.ForeignKey(default=333, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='preference_food',
            name='user',
            field=models.ForeignKey(default=333, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
