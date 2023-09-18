# Generated by Django 2.2 on 2023-09-18 17:56

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='BlogPost',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('my_field_name', models.CharField(help_text='Enter Blog Title', max_length=50)),
            ],
            options={
                'ordering': ['-my_field_name'],
            },
        ),
    ]