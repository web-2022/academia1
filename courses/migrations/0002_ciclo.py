# Generated by Django 4.2.6 on 2024-10-22 11:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Ciclo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=200)),
                ('subtitulo', models.CharField(blank=True, max_length=200)),
                ('descripcion', models.TextField()),
                ('imagen', models.ImageField(blank=True, upload_to='courses/img/')),
            ],
        ),
    ]
