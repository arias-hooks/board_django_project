# Generated by Django 4.1.7 on 2023-02-25 02:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('board', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='boardmodel',
            name='read_text',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='boardmodel',
            name='sns_image',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
    ]