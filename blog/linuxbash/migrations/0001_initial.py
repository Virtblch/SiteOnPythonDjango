# Generated by Django 4.0.4 on 2022-04-19 14:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('categName', models.CharField(max_length=100)),
                ('categHumanName', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=1000)),
                ('post', models.TextField(max_length=99999)),
                ('url', models.CharField(max_length=200)),
                ('description', models.TextField(max_length=1000)),
                ('datePost', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='UploadFile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('imagesPost', models.FileField(upload_to='blog/%Y/%m/%d')),
                ('keyPost', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='linuxbash.post')),
            ],
        ),
        migrations.CreateModel(
            name='SubCategory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('subCategName', models.CharField(max_length=100)),
                ('subCategHumanName', models.CharField(max_length=100)),
                ('keyCateg', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='linuxbash.category')),
            ],
        ),
        migrations.AddField(
            model_name='post',
            name='keyCateg',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='linuxbash.subcategory'),
        ),
    ]
