# Generated by Django 4.2.6 on 2023-10-05 04:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Fan',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(max_length=255)),
                ('asosiy', models.BooleanField()),
            ],
        ),
        migrations.CreateModel(
            name='Yonalish',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(max_length=255)),
                ('aktiv', models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name='Ustoz',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ism', models.CharField(max_length=255)),
                ('jins', models.CharField(choices=[('Erkak', 'Erkak'), ('Ayol', 'Ayol')], max_length=6)),
                ('yosh', models.PositiveSmallIntegerField()),
                ('daraja', models.CharField(max_length=255)),
                ('fan', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='taskApp.fan')),
            ],
        ),
        migrations.AddField(
            model_name='fan',
            name='yonalish',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='taskApp.yonalish'),
        ),
    ]
