# Generated by Django 2.2.2 on 2019-07-01 17:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('microBlogger', '0008_blogs_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blogs',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='image/'),
        ),
    ]
