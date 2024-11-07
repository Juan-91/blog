# Generated by Django 5.1.2 on 2024-10-25 02:39

from django.db import migrations


def populate_status(apps, schemaeditor):
    entries = {
        "published": "A post that all can view",
        "draft": "A post only visible to the author",
        "archived": "Older posts only logged in users can view"
    }
    Status = apps.get_model("posts", "Status")
    for key, value in entries.items():
        status = Status(name=key, description=value)
        status.save()

class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0001_initial'),
    ]

    operations = [
        migrations.RunPython(populate_status)
    ]
