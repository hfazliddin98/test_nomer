# Generated by Django 5.1.3 on 2024-11-25 14:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('nomer', '0004_alter_qiymat_qiymat'),
    ]

    operations = [
        migrations.AlterField(
            model_name='qiymat',
            name='qiymat',
            field=models.CharField(max_length=255),
        ),
    ]
