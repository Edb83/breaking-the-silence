# Generated by Django 4.2 on 2023-04-14 16:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('connections', '0004_connectionrequest_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='connectionrequest',
            name='status',
            field=models.IntegerField(choices=[(0, 'Pending'), (1, 'Accepted'), (2, 'Dismissed')], default=0),
        ),
    ]
