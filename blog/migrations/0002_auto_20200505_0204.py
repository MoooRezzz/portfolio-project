# Generated by Django 2.2.12 on 2020-05-04 21:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Blog',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='images/')),
                ('title', models.CharField(max_length=255)),
                ('pub_date', models.DateTimeField()),
                ('body', models.TextField()),
            ],
        ),
        migrations.DeleteModel(
            name='Post',
        ),
    ]