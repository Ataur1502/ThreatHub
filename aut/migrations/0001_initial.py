# Generated by Django 5.0.2 on 2024-02-09 19:37

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Music',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('file_path', models.CharField(max_length=255)),
            ],
        ),
    ]
