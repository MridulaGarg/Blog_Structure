# Generated by Django 2.1.1 on 2018-10-21 12:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('django_blog_it', '0016_auto_20181021_1730'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='featured_image',
            field=models.ImageField(blank=True, null=True, upload_to='static/blog/uploads/%Y/%m/%d/'),
        ),
    ]
