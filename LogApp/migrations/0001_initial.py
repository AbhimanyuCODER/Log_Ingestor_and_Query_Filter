# Generated by Django 4.2.7 on 2023-11-19 15:22

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Log',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('traceId', models.CharField(max_length=50)),
                ('level', models.CharField(max_length=50)),
                ('message', models.TextField()),
                ('resourceId', models.CharField(max_length=50)),
                ('timestamp', models.DateTimeField()),
                ('spanId', models.CharField(max_length=50)),
                ('commit', models.CharField(max_length=50)),
                ('metadata', models.JSONField(default=dict)),
            ],
        ),
    ]
