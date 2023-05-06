# Generated by Django 4.1.7 on 2023-04-09 12:37

from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Speaker",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("full_name", models.CharField(max_length=200)),
                ("bio", models.TextField()),
                (
                    "short_bio",
                    models.TextField(blank=True, help_text="for keynote speakers"),
                ),
                ("twitter", models.CharField(blank=True, max_length=255)),
                ("github", models.CharField(blank=True, max_length=255)),
                ("email", models.EmailField(max_length=254)),
                ("photo", models.ImageField(upload_to="program/speakers/")),
                (
                    "display_position",
                    models.PositiveSmallIntegerField(
                        default=0, help_text="sort order on frontend displays"
                    ),
                ),
                ("is_public", models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name="Talk",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "type",
                    models.CharField(
                        choices=[
                            ("workshop", "Workshop"),
                            ("sprint", "Sprint"),
                            ("talk", "Talk"),
                        ],
                        max_length=10,
                    ),
                ),
                (
                    "language",
                    models.CharField(
                        choices=[("en", "English (preferred)"), ("cs", "Czech/Slovak")],
                        default="en",
                        max_length=2,
                    ),
                ),
                (
                    "difficulty",
                    models.CharField(
                        choices=[("beginner", "Beginner"), ("advanced", "Advanced")],
                        default="beginner",
                        max_length=10,
                    ),
                ),
                (
                    "order",
                    models.SmallIntegerField(
                        help_text="display order on front-end", unique=True
                    ),
                ),
                ("title", models.CharField(max_length=250)),
                ("abstract", models.TextField()),
                ("is_backup", models.BooleanField(blank=True, default=False)),
                ("is_public", models.BooleanField(blank=True, default=False)),
                (
                    "in_data_track",
                    models.BooleanField(
                        blank=True, default=False, verbose_name="PyData Track"
                    ),
                ),
                (
                    "private_note",
                    models.TextField(
                        blank=True, default="", help_text="DO NOT SHOW ON WEBSITE"
                    ),
                ),
                (
                    "og_image",
                    models.ImageField(
                        blank=True,
                        help_text="og:image (social media image) 1200×630 pixels",
                        null=True,
                        upload_to="programme/images",
                    ),
                ),
                (
                    "video_id",
                    models.CharField(
                        blank=True, default="", help_text="YouTube URL", max_length=100
                    ),
                ),
                ("is_keynote", models.BooleanField(blank=True, default=False)),
            ],
            options={
                "ordering": ("order",),
                "abstract": False,
            },
        ),
        migrations.CreateModel(
            name="Workshop",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "type",
                    models.CharField(
                        choices=[
                            ("workshop", "Workshop"),
                            ("sprint", "Sprint"),
                            ("talk", "Talk"),
                        ],
                        max_length=10,
                    ),
                ),
                (
                    "language",
                    models.CharField(
                        choices=[("en", "English (preferred)"), ("cs", "Czech/Slovak")],
                        default="en",
                        max_length=2,
                    ),
                ),
                (
                    "difficulty",
                    models.CharField(
                        choices=[("beginner", "Beginner"), ("advanced", "Advanced")],
                        default="beginner",
                        max_length=10,
                    ),
                ),
                (
                    "order",
                    models.SmallIntegerField(
                        help_text="display order on front-end", unique=True
                    ),
                ),
                ("title", models.CharField(max_length=250)),
                ("abstract", models.TextField()),
                ("is_backup", models.BooleanField(blank=True, default=False)),
                ("is_public", models.BooleanField(blank=True, default=False)),
                (
                    "in_data_track",
                    models.BooleanField(
                        blank=True, default=False, verbose_name="PyData Track"
                    ),
                ),
                (
                    "private_note",
                    models.TextField(
                        blank=True, default="", help_text="DO NOT SHOW ON WEBSITE"
                    ),
                ),
                (
                    "og_image",
                    models.ImageField(
                        blank=True,
                        help_text="og:image (social media image) 1200×630 pixels",
                        null=True,
                        upload_to="programme/images",
                    ),
                ),
                (
                    "requirements",
                    models.TextField(
                        blank=True,
                        default="",
                        help_text="include even the most obvious stuff: "
                        "laptops, GIT, Python",
                        verbose_name="What should attendees bring, "
                        "install and know?",
                    ),
                ),
                (
                    "length",
                    models.CharField(
                        blank=True,
                        choices=[
                            ("1h", "1 hour"),
                            ("2h", "2 hours"),
                            ("3h", "3 hours"),
                            ("1d", "Full day (most sprints go here!)"),
                            (
                                "xx",
                                "Something else! "
                                "(Please leave a note in the abstract!)",
                            ),
                        ],
                        max_length=2,
                    ),
                ),
                (
                    "registration",
                    models.CharField(
                        blank="free",
                        choices=[
                            ("without", "Without"),
                            ("free", "Free"),
                            ("paid", "Paid"),
                        ],
                        default="free",
                        max_length=10,
                    ),
                ),
                (
                    "is_sold_out",
                    models.BooleanField(
                        blank=True, default=False, verbose_name="Sold out"
                    ),
                ),
                (
                    "attendee_limit",
                    models.PositiveSmallIntegerField(
                        blank=True,
                        default=False,
                        help_text="maximum number of attendees allowed",
                        verbose_name="Attendee limit",
                    ),
                ),
            ],
            options={
                "ordering": ("order",),
                "abstract": False,
            },
        ),
        migrations.AddIndex(
            model_name="workshop",
            index=models.Index(
                fields=["is_public"], name="program_wor_is_publ_f833f0_idx"
            ),
        ),
        migrations.AddIndex(
            model_name="workshop",
            index=models.Index(
                fields=["is_backup"], name="program_wor_is_back_729061_idx"
            ),
        ),
        migrations.AddIndex(
            model_name="workshop",
            index=models.Index(fields=["type"], name="program_wor_type_f98503_idx"),
        ),
        migrations.AddIndex(
            model_name="talk",
            index=models.Index(
                fields=["is_public"], name="program_tal_is_publ_cd0c5d_idx"
            ),
        ),
        migrations.AddIndex(
            model_name="talk",
            index=models.Index(
                fields=["is_backup"], name="program_tal_is_back_40509f_idx"
            ),
        ),
        migrations.AddIndex(
            model_name="talk",
            index=models.Index(fields=["type"], name="program_tal_type_7027d6_idx"),
        ),
        migrations.AddField(
            model_name="speaker",
            name="talks",
            field=models.ManyToManyField(
                blank=True, related_name="talk_speakers", to="program.talk"
            ),
        ),
        migrations.AddField(
            model_name="speaker",
            name="workshops",
            field=models.ManyToManyField(
                blank=True, related_name="workshop_speakers", to="program.workshop"
            ),
        ),
    ]
