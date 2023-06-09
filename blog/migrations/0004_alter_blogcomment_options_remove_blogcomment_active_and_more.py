# Generated by Django 4.2 on 2023-04-10 14:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_blogcomment'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='blogcomment',
            options={},
        ),
        migrations.RemoveField(
            model_name='blogcomment',
            name='active',
        ),
        migrations.RemoveField(
            model_name='blogcomment',
            name='created_on',
        ),
        migrations.RemoveField(
            model_name='blogcomment',
            name='email',
        ),
        migrations.RemoveField(
            model_name='blogcomment',
            name='name',
        ),
        migrations.RemoveField(
            model_name='blogcomment',
            name='parent',
        ),
        migrations.AlterField(
            model_name='blogcomment',
            name='post',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='blog.post'),
        ),
        migrations.AlterField(
            model_name='blogcomment',
            name='timestamp',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
