# Generated by Django 2.2.1 on 2019-05-30 13:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blogs', '0002_auto_20190530_1815'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
            ],
        ),
        migrations.RemoveField(
            model_name='blog',
            name='category',
        ),
        migrations.AddField(
            model_name='blog',
            name='category',
            field=models.ManyToManyField(to='blogs.Category'),
        ),
    ]