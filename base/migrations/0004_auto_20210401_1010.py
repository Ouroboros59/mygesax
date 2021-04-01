# Generated by Django 3.1.7 on 2021-04-01 10:10

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('base', '0003_auto_20210331_1534'),
    ]

    operations = [
        migrations.AddField(
            model_name='subject',
            name='user',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='auth.user'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='promotion',
            name='name',
            field=models.CharField(default=None, max_length=30),
        ),
    ]
