# Generated by Django 4.0.1 on 2022-01-20 04:44

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django_countries.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Room',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(max_length=100)),
                ('description', models.TextField(max_length=30)),
                ('country', django_countries.fields.CountryField(max_length=2)),
                ('nation', models.CharField(choices=[('usa', '미국'), ('japan', '일본'), ('china', '중국'), ('hokong', '홍콩'), ('europe', '유럽')], default='미국', max_length=20)),
                ('price', models.IntegerField()),
                ('brand', models.CharField(choices=[('nike', '나이키'), ('dior', '디올'), ('adidas', '아디다스'), ('cuggi', '구찌')], default='나이키', max_length=20)),
                ('categories', models.CharField(choices=[('clothes', '의류'), ('shoes', '신발'), ('cosmetic', '화장품'), ('health', '건강식품')], default='의류', max_length=20)),
                ('delivery_condition', models.CharField(choices=[('abroad', '해외배송'), ('domestic', '국내배송')], default='해외배송', max_length=20)),
                ('delivery_term', models.CharField(choices=[('three', '3일이내 배송'), ('seven', '7일이내 배송'), ('ten', '10일이내 배송')], default='7일이내 배송', max_length=20)),
                ('discount_rate', models.IntegerField()),
                ('host', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
