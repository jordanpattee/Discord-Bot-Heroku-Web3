# Generated by Django 4.2.15 on 2024-10-14 17:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("CloaksMart", "0013_posts_delete_post_delete_thread"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="posts",
            name="username",
        ),
    ]
