# Generated by Django 5.1.2 on 2024-10-21 13:02

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('uretim', '0003_alter_ucak_ad'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.RemoveField(
            model_name='parca',
            name='kullanilan_ucak',
        ),
        migrations.RemoveField(
            model_name='personel',
            name='isim',
        ),
        migrations.AddField(
            model_name='personel',
            name='user',
            field=models.OneToOneField(default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
    ]
