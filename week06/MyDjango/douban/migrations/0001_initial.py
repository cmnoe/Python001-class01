# Generated by Django 2.2.13 on 2020-08-02 11:35

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Shorts',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('user', models.CharField(max_length=50)),
                ('star', models.IntegerField()),
                ('content', models.CharField(max_length=500)),
            ],
            options={
                'db_table': 'shorts',
                'managed': False,
            },
        ),
    ]