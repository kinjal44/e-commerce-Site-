# Generated by Django 3.2.2 on 2021-07-03 21:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_rename_blog_blogpost'),
    ]

    operations = [
        migrations.AddField(
            model_name='blogpost',
            name='thumbnail',
            field=models.ImageField(default='', upload_to='shop/images'),
        ),
    ]