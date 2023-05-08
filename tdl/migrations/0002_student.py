# Generated by Django 4.1.7 on 2023-05-08 12:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tdl', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField()),
                ('age', models.IntegerField()),
                ('grade', models.CharField(max_length=2)),
                ('result', models.BooleanField()),
                ('marks', models.FloatField()),
            ],
        ),
    ]
