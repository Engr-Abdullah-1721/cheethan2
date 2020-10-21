# Generated by Django 3.1.2 on 2020-10-20 18:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0003_activityperiod_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='activityperiod',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='activity_periods', to='api.user'),
        ),
    ]
