# Generated by Django 4.1.3 on 2022-12-02 13:27

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('post', models.TextField(max_length=5000)),
                ('pub_date', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
