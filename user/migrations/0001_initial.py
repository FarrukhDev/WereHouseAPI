# Generated by Django 4.0.3 on 2022-03-12 17:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('ombor', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Client',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ism', models.CharField(max_length=35)),
                ('tel', models.CharField(max_length=15)),
                ('dokon_nomi', models.CharField(max_length=25)),
                ('manzil', models.CharField(max_length=50)),
                ('omborxona', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ombor.ombor')),
            ],
        ),
    ]