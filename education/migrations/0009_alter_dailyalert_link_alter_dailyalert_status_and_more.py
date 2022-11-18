# Generated by Django 4.1.2 on 2022-11-18 09:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('education', '0008_alter_slideshow_link'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dailyalert',
            name='link',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='link'),
        ),
        migrations.AlterField(
            model_name='dailyalert',
            name='status',
            field=models.SmallIntegerField(choices=[(1, 'Draft'), (2, 'Published')], default=2),
        ),
        migrations.AlterField(
            model_name='document',
            name='status',
            field=models.SmallIntegerField(choices=[(1, 'Draft'), (2, 'Published')], default=2),
        ),
        migrations.AlterField(
            model_name='popup',
            name='status',
            field=models.SmallIntegerField(choices=[(1, 'Draft'), (2, 'Published')], default=2),
        ),
    ]
