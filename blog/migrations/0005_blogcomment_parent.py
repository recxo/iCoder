# Generated by Django 4.2 on 2023-04-10 17:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_alter_blogcomment_options_remove_blogcomment_active_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='blogcomment',
            name='parent',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='blog.blogcomment'),
        ),
    ]
