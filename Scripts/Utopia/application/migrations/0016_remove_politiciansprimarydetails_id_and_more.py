# Generated by Django 4.2.5 on 2023-10-03 09:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('application', '0015_remove_mpelection_candidate2id_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='politiciansprimarydetails',
            name='id',
        ),
        migrations.AlterField(
            model_name='politiciansprimarydetails',
            name='PoliticianID',
            field=models.IntegerField(primary_key=True, serialize=False),
        ),
    ]