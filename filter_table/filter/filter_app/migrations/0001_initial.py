# Generated by Django 2.0.2 on 2018-03-10 05:09

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Data',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=25)),
                ('type_of', models.CharField(max_length=4)),
                ('brand_obj', models.CharField(max_length=20)),
                ('brand_sent', models.CharField(max_length=20)),
                ('seg', models.CharField(max_length=3)),
                ('image', models.CharField(max_length=15)),
            ],
        ),
    ]