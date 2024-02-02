# Generated by Django 5.0.1 on 2024-02-02 18:58

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Person',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=20)),
                ('usermail', models.EmailField(max_length=50, unique=True)),
                ('password', models.CharField(max_length=20)),
                ('phone', models.CharField(max_length=20)),
                ('address', models.TextField()),
                ('birthday', models.DateTimeField()),
                ('gender', models.CharField(max_length=10)),
                ('join_date', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
