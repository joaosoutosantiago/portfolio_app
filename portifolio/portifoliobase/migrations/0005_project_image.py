# Generated by Django 4.1.3 on 2022-12-11 02:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portifoliobase', '0004_rename_contato_contact'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
    ]
