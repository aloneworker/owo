# Generated by Django 4.1.1 on 2023-09-30 10:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myap', '0015_bulletnotemodel_txt'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bulletnotemodel',
            name='txt',
            field=models.TextField(blank=True, default=''),
        ),
    ]
