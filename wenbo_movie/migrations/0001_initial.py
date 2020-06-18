# Generated by Django 3.0.5 on 2020-04-17 23:13

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Movie',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=64)),
                ('duration', models.IntegerField()),
                ('type', models.CharField(max_length=128)),
                ('country', models.CharField(max_length=64)),
                ('language', models.CharField(max_length=64)),
                ('imdb_num', models.CharField(max_length=256)),
                ('date', models.CharField(max_length=64)),
            ],
        ),
        migrations.CreateModel(
            name='Worker',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=64)),
                ('gender', models.CharField(max_length=64)),
                ('birthday', models.CharField(max_length=64)),
                ('english_name', models.CharField(max_length=64)),
                ('imdb_num', models.CharField(max_length=256)),
                ('work_type', models.CharField(max_length=32)),
                ('related_movie', models.ManyToManyField(blank=True, related_name='workers', to='wenbo_movie.Movie')),
            ],
        ),
    ]
