# Generated by Django 4.2.20 on 2025-03-20 21:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('patient', '0002_remove_patient_name_patient_patient_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='patient',
            name='koumoku1',
            field=models.TextField(default=1),
            preserve_default=False,
        ),
    ]
