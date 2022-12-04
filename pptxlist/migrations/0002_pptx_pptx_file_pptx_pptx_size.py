# Generated by Django 4.0 on 2022-02-01 12:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pptxlist', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='pptx',
            name='pptx_file',
            field=models.BinaryField(blank=True),
        ),
        migrations.AddField(
            model_name='pptx',
            name='pptx_size',
            field=models.CharField(default=0, max_length=100),
            preserve_default=False,
        ),
    ]