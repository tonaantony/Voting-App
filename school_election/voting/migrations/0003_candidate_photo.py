# Generated by Django 4.2.13 on 2024-06-06 15:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("voting", "0002_alter_vote_voter"),
    ]

    operations = [
        migrations.AddField(
            model_name="candidate",
            name="photo",
            field=models.ImageField(
                default="candidate_photos/user.png", upload_to="candidate_photos/"
            ),
        ),
    ]