# Generated by Django 5.1.3 on 2024-11-09 14:06

import datetime
import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0002_post_test'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='create_date',
            field=models.DateField(default=datetime.datetime(2024, 11, 9, 14, 6, 45, 105679)),
        ),
        migrations.AlterField(
            model_name='post',
            name='like_count',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='post',
            name='published',
            field=models.BooleanField(default=False),
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.TextField()),
                ('post', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comments', to='post.post')),
            ],
        ),
    ]