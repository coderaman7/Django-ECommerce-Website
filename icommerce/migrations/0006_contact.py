# Generated by Django 3.1.1 on 2020-09-15 16:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('icommerce', '0005_order_country'),
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fname', models.CharField(max_length=50)),
                ('lname', models.CharField(max_length=50)),
                ('subject', models.CharField(max_length=100)),
                ('message', models.CharField(max_length=10000)),
                ('email', models.CharField(max_length=50)),
            ],
        ),
    ]
