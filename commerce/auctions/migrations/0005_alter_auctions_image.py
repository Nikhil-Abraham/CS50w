# Generated by Django 3.2.5 on 2021-08-14 10:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0004_alter_auctions_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='auctions',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='media/images'),
        ),
    ]