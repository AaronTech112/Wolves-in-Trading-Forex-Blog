# Generated by Django 4.1 on 2022-10-30 18:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0014_alter_comment_email'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='cat_image',
            field=models.ImageField(default='bg1.png', null=True, upload_to=''),
        ),
    ]
