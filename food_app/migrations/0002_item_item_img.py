# Generated by Django 4.2.3 on 2023-08-12 14:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('food_app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='item',
            name='item_img',
            field=models.CharField(default='https://images.ctfassets.net/84wm3hhxw4gx/0sxerdVddcgpnd69VcMsx/414cb6a014fc90e5d96e07fef8022ccf/foodplaceholder.png', max_length=500),
        ),
    ]
