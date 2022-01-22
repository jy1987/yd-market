# Generated by Django 4.0.1 on 2022-01-22 08:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rooms', '0004_alter_room_brand_alter_room_host_alter_room_nation'),
    ]

    operations = [
        migrations.AlterField(
            model_name='room',
            name='color',
            field=models.ManyToManyField(blank=True, related_name='rooms', to='rooms.ItemColor'),
        ),
    ]