# Generated by Django 5.0 on 2024-01-05 22:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('translator', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='translation',
            name='pdf_file',
            field=models.FileField(blank=True, null=True, upload_to='pdf/'),
        ),
    ]
