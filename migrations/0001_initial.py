# Generated by Django 3.1.14 on 2022-02-05 10:16

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cricketer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('age', models.IntegerField()),
                ('address', models.CharField(max_length=50)),
                ('country', models.CharField(max_length=50)),
                ('occupation', models.CharField(max_length=50)),
            ],
        ),
    ]
