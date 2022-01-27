# Generated by Django 4.0.1 on 2022-01-27 04:40

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Review',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('review', models.TextField()),
                ('accuracy', models.IntegerField()),
                ('value', models.IntegerField()),
                ('guarantee', models.BooleanField(default=True)),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
