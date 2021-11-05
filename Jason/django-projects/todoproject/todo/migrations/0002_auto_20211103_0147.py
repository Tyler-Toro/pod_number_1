# Generated by Django 3.2.8 on 2021-11-03 01:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todo', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Notes',
            fields=[
                ('note_id', models.AutoField(primary_key=True, serialize=False)),
                ('note_text', models.CharField(max_length=500)),
            ],
        ),
        migrations.AddField(
            model_name='todo',
            name='completed',
            field=models.BooleanField(default=False),
        ),
    ]
