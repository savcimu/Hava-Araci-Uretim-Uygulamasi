# Generated by Django 5.1.2 on 2024-10-21 18:29

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('uretim', '0007_parca_kullanilan_ucak'),
    ]

    operations = [
        migrations.CreateModel(
            name='UretilenUcak',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tarih', models.DateTimeField(auto_now_add=True)),
                ('kullanilan_parcalar', models.ManyToManyField(related_name='kullanildigi_uretilen_ucaklar', to='uretim.parca')),
                ('ucak_tipi', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='uretim.ucak')),
            ],
        ),
    ]