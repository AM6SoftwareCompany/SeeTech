# Generated by Django 3.1 on 2020-08-26 16:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='category',
            field=models.CharField(choices=[('P', 'Phone'), ('TB', 'Tablet'), ('PA', 'Phone accessories'), ('C', 'Computer'), ('LP', 'Laptop'), ('CA', 'PC accessories'), ('PS', 'Printer & Scanner'), ('T', 'Television'), ('SR', 'Satellite Receiver'), ('PJ', 'Projector'), ('AD', 'Audio'), ('TA', 'TV accessories'), ('CM', 'Camera'), ('MW', 'Men Watch'), ('WW', 'Women Watch'), ('MA', 'Men accessories'), ('WA', 'Women accessories'), ('S', 'Shirt'), ('SW', 'Sport wear'), ('OW', 'Outwear')], max_length=2),
        ),
    ]
