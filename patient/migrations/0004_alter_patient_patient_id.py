# Generated by Django 4.2.20 on 2025-03-20 22:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('patient', '0003_patient_koumoku1'),
    ]

    operations = [
        migrations.AlterField(
            model_name='patient',
            name='patient_id',
            field=models.IntegerField(),
        ),
    ]
