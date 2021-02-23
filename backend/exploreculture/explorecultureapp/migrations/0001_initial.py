# Generated by Django 2.2 on 2020-07-28 22:58

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AR',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=120)),
                ('content', models.TextField()),
                ('poster', models.CharField(max_length=120)),
                ('arimg', models.ImageField(max_length=255, upload_to='img/')),
                ('arfile', models.FileField(upload_to='ar/')),
            ],
        ),
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=120)),
                ('content', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='CulturalPhotography',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=120)),
                ('content', models.TextField()),
                ('imgposter', models.CharField(max_length=120)),
                ('culturalphotographyimg', models.ImageField(max_length=255, upload_to='img/')),
            ],
        ),
        migrations.CreateModel(
            name='EightDAudio',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=120)),
                ('content', models.TextField()),
                ('songposter', models.CharField(max_length=120)),
                ('eightdaudioimg', models.ImageField(max_length=255, upload_to='img/')),
                ('eightdaudiofile', models.FileField(upload_to='audio/')),
            ],
        ),
        migrations.CreateModel(
            name='TraditionalFood',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=120)),
                ('content', models.TextField()),
                ('recipeposter', models.CharField(max_length=120)),
                ('recipeimg', models.ImageField(max_length=255, upload_to='img/')),
            ],
        ),
        migrations.CreateModel(
            name='View360',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=120)),
                ('content', models.TextField()),
                ('imgposter', models.CharField(max_length=120)),
                ('view360img', models.ImageField(max_length=255, upload_to='img/')),
                ('view360url', models.TextField()),
            ],
        ),
    ]
