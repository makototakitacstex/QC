# Generated by Django 4.0.5 on 2022-07-01 14:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vid02', '0008_komarigotoinput'),
    ]

    operations = [
        migrations.AlterField(
            model_name='komarigotoinput',
            name='eikyo1_code',
            field=models.CharField(blank=True, db_column='eikyo1_code', default='', max_length=1000),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='komarigotoinput',
            name='eikyo2_code',
            field=models.CharField(blank=True, db_column='eikyo2_code', default='', max_length=1000),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='komarigotoinput',
            name='genin1_code',
            field=models.CharField(blank=True, db_column='genin1_code', default='', max_length=1000),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='komarigotoinput',
            name='genin2_code',
            field=models.CharField(blank=True, db_column='genin2_code', default='', max_length=1000),
            preserve_default=False,
        ),
    ]