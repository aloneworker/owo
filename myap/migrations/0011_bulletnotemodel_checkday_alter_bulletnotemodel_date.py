# Generated by Django 4.1.1 on 2023-08-23 14:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myap', '0010_rename_ntrdescription_charact_ntrfdescription_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='bulletnotemodel',
            name='checkday',
            field=models.DateTimeField(default=''),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='bulletnotemodel',
            name='date',
            field=models.DateTimeField(default='2023-08-23'),
        ),
    ]
