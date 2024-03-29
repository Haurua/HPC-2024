# Generated by Django 5.0.1 on 2024-01-20 06:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crm_jobs', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='clients',
            name='business_name',
            field=models.CharField(max_length=30, verbose_name='Business Name'),
        ),
        migrations.AlterField(
            model_name='clients',
            name='notes',
            field=models.TextField(blank=True, null=True, verbose_name='Client Notes'),
        ),
        migrations.AlterField(
            model_name='clients',
            name='postcode',
            field=models.CharField(max_length=12, verbose_name='Postcode'),
        ),
        migrations.AlterField(
            model_name='clients',
            name='telephone',
            field=models.CharField(max_length=12, verbose_name='Telephone'),
        ),
    ]
