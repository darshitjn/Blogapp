# Generated by Django 4.0.6 on 2022-07-11 18:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0007_alter_post_body'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='snippet',
            field=models.TextField(default='click above to read blog', max_length=255),
        ),
    ]
