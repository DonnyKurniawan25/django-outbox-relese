# Generated by Django 4.1.2 on 2022-11-21 11:28

import ckeditor_uploader.fields
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django_cryptography.fields
import parler.fields
import parler.models
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('menu', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('sites', '0002_alter_domain_unique'),
    ]

    operations = [
        migrations.CreateModel(
            name='Categories',
            fields=[
                ('id', models.BigAutoField(editable=False, primary_key=True, serialize=False)),
                ('uuid', models.UUIDField(default=uuid.uuid4, editable=False, unique=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('slug', models.SlugField(blank=True, default='', editable=False, unique=True)),
                ('site', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='sites.site')),
            ],
            options={
                'verbose_name': 'category',
                'verbose_name_plural': 'categories',
            },
            bases=(parler.models.TranslatableModelMixin, models.Model),
        ),
        migrations.CreateModel(
            name='DailyAlert',
            fields=[
                ('id', models.BigAutoField(editable=False, primary_key=True, serialize=False)),
                ('uuid', models.UUIDField(default=uuid.uuid4, editable=False, unique=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('link', models.CharField(blank=True, max_length=255, null=True, verbose_name='link')),
                ('status', models.SmallIntegerField(choices=[(1, 'Draft'), (2, 'Published')], default=2)),
                ('admin', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL)),
                ('site', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='sites.site')),
            ],
            options={
                'verbose_name': 'daily alert',
                'verbose_name_plural': 'daily alerts',
            },
            bases=(parler.models.TranslatableModelMixin, models.Model),
        ),
        migrations.CreateModel(
            name='Document',
            fields=[
                ('id', models.BigAutoField(editable=False, primary_key=True, serialize=False)),
                ('uuid', models.UUIDField(default=uuid.uuid4, editable=False, unique=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('file_path_doc', models.FileField(upload_to='', verbose_name='file path Document')),
                ('size', models.BigIntegerField(blank=True, default=0, editable=False, null=True, verbose_name='size')),
                ('hits', models.IntegerField(default=0, editable=False, verbose_name='hits')),
                ('status', models.SmallIntegerField(choices=[(1, 'Draft'), (2, 'Published')], default=2)),
                ('admin', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL)),
                ('categories', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='education.categories')),
                ('site', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='sites.site', verbose_name='site')),
            ],
            options={
                'ordering': ['-updated_at'],
                'abstract': False,
            },
            bases=(parler.models.TranslatableModelMixin, models.Model),
        ),
        migrations.CreateModel(
            name='Greeting',
            fields=[
                ('id', models.BigAutoField(editable=False, primary_key=True, serialize=False)),
                ('uuid', models.UUIDField(default=uuid.uuid4, editable=False, unique=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('view_count', models.PositiveIntegerField(default=0, editable=False)),
                ('status', models.SmallIntegerField(choices=[(1, 'Draft'), (2, 'Published')], default=2)),
                ('admin', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL)),
                ('site', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='sites.site', verbose_name='site')),
            ],
            options={
                'verbose_name': 'greeting',
                'verbose_name_plural': 'greetings',
            },
            bases=(parler.models.TranslatableModelMixin, models.Model),
        ),
        migrations.CreateModel(
            name='PhotoGallery',
            fields=[
                ('id', models.BigAutoField(editable=False, primary_key=True, serialize=False)),
                ('uuid', models.UUIDField(default=uuid.uuid4, editable=False, unique=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('view_count', models.PositiveIntegerField(default=0, editable=False)),
                ('slug', models.SlugField(blank=True, default='', max_length=255, unique=True)),
                ('status', models.SmallIntegerField(choices=[(1, 'Draft'), (2, 'Published')], default=2)),
                ('admin', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL)),
                ('site', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='sites.site', verbose_name='site')),
            ],
            options={
                'ordering': ['-updated_at'],
                'abstract': False,
            },
            bases=(parler.models.TranslatableModelMixin, models.Model),
        ),
        migrations.CreateModel(
            name='Popup',
            fields=[
                ('id', models.BigAutoField(editable=False, primary_key=True, serialize=False)),
                ('uuid', models.UUIDField(default=uuid.uuid4, editable=False, unique=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('link', django_cryptography.fields.encrypt(models.URLField(blank=True, max_length=255, null=True, verbose_name='link'))),
                ('status', models.SmallIntegerField(choices=[(1, 'Draft'), (2, 'Published')], default=2)),
                ('admin', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL)),
                ('site', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='sites.site', verbose_name='site')),
            ],
            options={
                'ordering': ['-updated_at'],
                'abstract': False,
            },
            bases=(parler.models.TranslatableModelMixin, models.Model),
        ),
        migrations.CreateModel(
            name='RelatedLink',
            fields=[
                ('id', models.BigAutoField(editable=False, primary_key=True, serialize=False)),
                ('uuid', models.UUIDField(default=uuid.uuid4, editable=False, unique=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('link', django_cryptography.fields.encrypt(models.URLField(max_length=255, verbose_name='link'))),
                ('status', models.SmallIntegerField(choices=[(1, 'Draft'), (2, 'Published')], default=2)),
                ('site', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='sites.site', verbose_name='site')),
            ],
            options={
                'ordering': ['-updated_at'],
                'abstract': False,
            },
            bases=(parler.models.TranslatableModelMixin, models.Model),
        ),
        migrations.CreateModel(
            name='SlideShow',
            fields=[
                ('id', models.BigAutoField(editable=False, primary_key=True, serialize=False)),
                ('uuid', models.UUIDField(default=uuid.uuid4, editable=False, unique=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('link', models.CharField(blank=True, max_length=255, null=True, verbose_name='link')),
                ('status', models.SmallIntegerField(choices=[(1, 'Draft'), (2, 'Published')], default=2)),
                ('admin', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL)),
                ('site', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='sites.site', verbose_name='site')),
            ],
            options={
                'verbose_name': 'slide show',
                'verbose_name_plural': 'slides show',
            },
            bases=(parler.models.TranslatableModelMixin, models.Model),
        ),
        migrations.CreateModel(
            name='Tags',
            fields=[
                ('id', models.BigAutoField(editable=False, primary_key=True, serialize=False)),
                ('uuid', models.UUIDField(default=uuid.uuid4, editable=False, unique=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('slug', models.SlugField(blank=True, default='', editable=False, unique=True)),
                ('site', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='sites.site')),
            ],
            options={
                'verbose_name': 'tag',
                'verbose_name_plural': 'tags',
            },
            bases=(parler.models.TranslatableModelMixin, models.Model),
        ),
        migrations.CreateModel(
            name='VideoGallery',
            fields=[
                ('id', models.BigAutoField(editable=False, primary_key=True, serialize=False)),
                ('uuid', models.UUIDField(default=uuid.uuid4, editable=False, unique=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('view_count', models.PositiveIntegerField(default=0, editable=False)),
                ('slug', models.SlugField(blank=True, default='', max_length=255, unique=True)),
                ('status', models.SmallIntegerField(choices=[(1, 'Draft'), (2, 'Published')], default=2)),
                ('embed', ckeditor_uploader.fields.RichTextUploadingField(blank=True, null=True, verbose_name='embed')),
                ('admin', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL)),
                ('site', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='sites.site', verbose_name='site')),
            ],
            options={
                'ordering': ['-updated_at'],
                'abstract': False,
            },
            bases=(parler.models.TranslatableModelMixin, models.Model),
        ),
        migrations.CreateModel(
            name='SocialMedia',
            fields=[
                ('id', models.BigAutoField(editable=False, primary_key=True, serialize=False)),
                ('uuid', models.UUIDField(default=uuid.uuid4, editable=False, unique=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('kind', models.SmallIntegerField(choices=[(1, 'Facebook'), (2, 'Twitter'), (3, 'Pinterest'), (4, 'Youtube'), (5, 'Instagram')], verbose_name='kind')),
                ('link', django_cryptography.fields.encrypt(models.URLField(max_length=255, verbose_name='link'))),
                ('status', models.SmallIntegerField(choices=[(1, 'Draft'), (2, 'Published')], default=2)),
                ('site', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='sites.site', verbose_name='site')),
            ],
            options={
                'ordering': ['-updated_at'],
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Pages',
            fields=[
                ('id', models.BigAutoField(editable=False, primary_key=True, serialize=False)),
                ('uuid', models.UUIDField(default=uuid.uuid4, editable=False, unique=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('view_count', models.PositiveIntegerField(default=0, editable=False, verbose_name='view count')),
                ('share_count', models.PositiveIntegerField(default=0, editable=False, verbose_name='share count')),
                ('slug', models.SlugField(blank=True, default='', editable=False, max_length=255, unique=True)),
                ('status', models.SmallIntegerField(choices=[(1, 'Draft'), (2, 'Published')], default=2)),
                ('admin', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL)),
                ('menu', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='menu.menu', verbose_name='Access From Menu')),
                ('site', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='sites.site', verbose_name='site')),
                ('tags', models.ManyToManyField(to='education.tags', verbose_name='tags')),
            ],
            options={
                'verbose_name': 'page',
                'verbose_name_plural': 'pages',
            },
            bases=(parler.models.TranslatableModelMixin, models.Model),
        ),
        migrations.CreateModel(
            name='News',
            fields=[
                ('id', models.BigAutoField(editable=False, primary_key=True, serialize=False)),
                ('uuid', models.UUIDField(default=uuid.uuid4, editable=False, unique=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('view_count', models.PositiveIntegerField(default=0, editable=False, verbose_name='view count')),
                ('share_count', models.PositiveIntegerField(default=0, editable=False, verbose_name='share count')),
                ('slug', models.SlugField(blank=True, default='', editable=False, max_length=255, unique=True)),
                ('status', models.SmallIntegerField(choices=[(1, 'Draft'), (2, 'Published')], default=2)),
                ('admin', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL)),
                ('categories', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='education.categories')),
                ('site', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='sites.site', verbose_name='site')),
                ('tags', models.ManyToManyField(to='education.tags', verbose_name='tags')),
            ],
            options={
                'verbose_name': 'news',
                'verbose_name_plural': 'news',
            },
            bases=(parler.models.TranslatableModelMixin, models.Model),
        ),
        migrations.CreateModel(
            name='Logo',
            fields=[
                ('id', models.BigAutoField(editable=False, primary_key=True, serialize=False)),
                ('uuid', models.UUIDField(default=uuid.uuid4, editable=False, unique=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(max_length=100, verbose_name='logo name')),
                ('site', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='sites.site')),
            ],
            options={
                'verbose_name': 'logo',
                'verbose_name_plural': 'logos',
            },
        ),
        migrations.CreateModel(
            name='Events',
            fields=[
                ('id', models.BigAutoField(editable=False, primary_key=True, serialize=False)),
                ('uuid', models.UUIDField(default=uuid.uuid4, editable=False, unique=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('view_count', models.PositiveIntegerField(default=0, editable=False, verbose_name='view count')),
                ('share_count', models.PositiveIntegerField(default=0, editable=False, verbose_name='share count')),
                ('slug', models.SlugField(blank=True, default='', editable=False, max_length=255, unique=True)),
                ('status', models.SmallIntegerField(choices=[(1, 'Draft'), (2, 'Published')], default=2)),
                ('date', models.DateField(verbose_name='date')),
                ('time', models.TimeField(verbose_name='time')),
                ('admin', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL)),
                ('categories', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='education.categories')),
                ('site', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='sites.site', verbose_name='site')),
                ('tags', models.ManyToManyField(to='education.tags', verbose_name='tags')),
            ],
            options={
                'verbose_name': 'event',
                'verbose_name_plural': 'events',
            },
            bases=(parler.models.TranslatableModelMixin, models.Model),
        ),
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.BigAutoField(editable=False, primary_key=True, serialize=False)),
                ('uuid', models.UUIDField(default=uuid.uuid4, editable=False, unique=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('view_count', models.PositiveIntegerField(default=0, editable=False, verbose_name='view count')),
                ('share_count', models.PositiveIntegerField(default=0, editable=False, verbose_name='share count')),
                ('slug', models.SlugField(blank=True, default='', editable=False, max_length=255, unique=True)),
                ('status', models.SmallIntegerField(choices=[(1, 'Draft'), (2, 'Published')], default=2)),
                ('admin', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL)),
                ('categories', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='education.categories')),
                ('site', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='sites.site', verbose_name='site')),
                ('tags', models.ManyToManyField(to='education.tags', verbose_name='tags')),
            ],
            options={
                'verbose_name': 'article',
                'verbose_name_plural': 'articles',
            },
            bases=(parler.models.TranslatableModelMixin, models.Model),
        ),
        migrations.CreateModel(
            name='Announcement',
            fields=[
                ('id', models.BigAutoField(editable=False, primary_key=True, serialize=False)),
                ('uuid', models.UUIDField(default=uuid.uuid4, editable=False, unique=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('view_count', models.PositiveIntegerField(default=0, editable=False, verbose_name='view count')),
                ('share_count', models.PositiveIntegerField(default=0, editable=False, verbose_name='share count')),
                ('slug', models.SlugField(blank=True, default='', editable=False, max_length=255, unique=True)),
                ('status', models.SmallIntegerField(choices=[(1, 'Draft'), (2, 'Published')], default=2)),
                ('admin', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL)),
                ('categories', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='education.categories')),
                ('site', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='sites.site', verbose_name='site')),
                ('tags', models.ManyToManyField(to='education.tags', verbose_name='tags')),
            ],
            options={
                'verbose_name': 'announcement',
                'verbose_name_plural': 'announcements',
            },
            bases=(parler.models.TranslatableModelMixin, models.Model),
        ),
        migrations.CreateModel(
            name='VideoGalleryTranslation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('language_code', models.CharField(db_index=True, max_length=15, verbose_name='Language')),
                ('title', django_cryptography.fields.encrypt(models.CharField(max_length=500, verbose_name='title'))),
                ('master', parler.fields.TranslationsForeignKey(editable=False, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='translations', to='education.videogallery')),
            ],
            options={
                'verbose_name': 'video gallery Translation',
                'db_table': 'education_videogallery_translation',
                'db_tablespace': '',
                'managed': True,
                'default_permissions': (),
                'unique_together': {('language_code', 'master')},
            },
            bases=(parler.models.TranslatedFieldsModelMixin, models.Model),
        ),
        migrations.CreateModel(
            name='TagsTranslation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('language_code', models.CharField(db_index=True, max_length=15, verbose_name='Language')),
                ('name', models.CharField(max_length=50, verbose_name='tags name')),
                ('master', parler.fields.TranslationsForeignKey(editable=False, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='translations', to='education.tags')),
            ],
            options={
                'verbose_name': 'tag Translation',
                'db_table': 'education_tags_translation',
                'db_tablespace': '',
                'managed': True,
                'default_permissions': (),
                'unique_together': {('language_code', 'master')},
            },
            bases=(parler.models.TranslatedFieldsModelMixin, models.Model),
        ),
        migrations.CreateModel(
            name='SlideShowTranslation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('language_code', models.CharField(db_index=True, max_length=15, verbose_name='Language')),
                ('title', models.CharField(max_length=500, verbose_name='title')),
                ('content', django_cryptography.fields.encrypt(ckeditor_uploader.fields.RichTextUploadingField(blank=True, null=True, verbose_name='content'))),
                ('master', parler.fields.TranslationsForeignKey(editable=False, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='translations', to='education.slideshow')),
            ],
            options={
                'verbose_name': 'slide show Translation',
                'db_table': 'education_slideshow_translation',
                'db_tablespace': '',
                'managed': True,
                'default_permissions': (),
                'unique_together': {('language_code', 'master')},
            },
            bases=(parler.models.TranslatedFieldsModelMixin, models.Model),
        ),
        migrations.CreateModel(
            name='RelatedLinkTranslation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('language_code', models.CharField(db_index=True, max_length=15, verbose_name='Language')),
                ('name', django_cryptography.fields.encrypt(models.CharField(max_length=150, verbose_name='name'))),
                ('master', parler.fields.TranslationsForeignKey(editable=False, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='translations', to='education.relatedlink')),
            ],
            options={
                'verbose_name': 'related link Translation',
                'db_table': 'education_relatedlink_translation',
                'db_tablespace': '',
                'managed': True,
                'default_permissions': (),
                'unique_together': {('language_code', 'master')},
            },
            bases=(parler.models.TranslatedFieldsModelMixin, models.Model),
        ),
        migrations.CreateModel(
            name='PopupTranslation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('language_code', models.CharField(db_index=True, max_length=15, verbose_name='Language')),
                ('title', django_cryptography.fields.encrypt(models.CharField(max_length=500, verbose_name='title'))),
                ('master', parler.fields.TranslationsForeignKey(editable=False, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='translations', to='education.popup')),
            ],
            options={
                'verbose_name': 'popup Translation',
                'db_table': 'education_popup_translation',
                'db_tablespace': '',
                'managed': True,
                'default_permissions': (),
                'unique_together': {('language_code', 'master')},
            },
            bases=(parler.models.TranslatedFieldsModelMixin, models.Model),
        ),
        migrations.CreateModel(
            name='PhotoGalleryTranslation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('language_code', models.CharField(db_index=True, max_length=15, verbose_name='Language')),
                ('title', django_cryptography.fields.encrypt(models.CharField(max_length=500, verbose_name='title'))),
                ('master', parler.fields.TranslationsForeignKey(editable=False, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='translations', to='education.photogallery')),
            ],
            options={
                'verbose_name': 'photo gallery Translation',
                'db_table': 'education_photogallery_translation',
                'db_tablespace': '',
                'managed': True,
                'default_permissions': (),
                'unique_together': {('language_code', 'master')},
            },
            bases=(parler.models.TranslatedFieldsModelMixin, models.Model),
        ),
        migrations.CreateModel(
            name='PagesTranslation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('language_code', models.CharField(db_index=True, max_length=15, verbose_name='Language')),
                ('title', django_cryptography.fields.encrypt(models.CharField(max_length=500, verbose_name='title'))),
                ('content', django_cryptography.fields.encrypt(ckeditor_uploader.fields.RichTextUploadingField(blank=True, null=True, verbose_name='content'))),
                ('master', parler.fields.TranslationsForeignKey(editable=False, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='translations', to='education.pages')),
            ],
            options={
                'verbose_name': 'page Translation',
                'db_table': 'education_pages_translation',
                'db_tablespace': '',
                'managed': True,
                'default_permissions': (),
                'unique_together': {('language_code', 'master')},
            },
            bases=(parler.models.TranslatedFieldsModelMixin, models.Model),
        ),
        migrations.CreateModel(
            name='NewsTranslation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('language_code', models.CharField(db_index=True, max_length=15, verbose_name='Language')),
                ('title', django_cryptography.fields.encrypt(models.CharField(max_length=500, verbose_name='title'))),
                ('content', django_cryptography.fields.encrypt(ckeditor_uploader.fields.RichTextUploadingField(blank=True, null=True, verbose_name='content'))),
                ('master', parler.fields.TranslationsForeignKey(editable=False, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='translations', to='education.news')),
            ],
            options={
                'verbose_name': 'news Translation',
                'db_table': 'education_news_translation',
                'db_tablespace': '',
                'managed': True,
                'default_permissions': (),
                'unique_together': {('language_code', 'master')},
            },
            bases=(parler.models.TranslatedFieldsModelMixin, models.Model),
        ),
        migrations.CreateModel(
            name='GreetingTranslation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('language_code', models.CharField(db_index=True, max_length=15, verbose_name='Language')),
                ('title', models.CharField(max_length=500, verbose_name='title')),
                ('content', django_cryptography.fields.encrypt(ckeditor_uploader.fields.RichTextUploadingField(blank=True, null=True, verbose_name='content'))),
                ('name', django_cryptography.fields.encrypt(models.CharField(blank=True, max_length=255, null=True, verbose_name='greeting name'))),
                ('designation', django_cryptography.fields.encrypt(models.CharField(blank=True, max_length=255, null=True, verbose_name='designation'))),
                ('master', parler.fields.TranslationsForeignKey(editable=False, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='translations', to='education.greeting')),
            ],
            options={
                'verbose_name': 'greeting Translation',
                'db_table': 'education_greeting_translation',
                'db_tablespace': '',
                'managed': True,
                'default_permissions': (),
                'unique_together': {('language_code', 'master')},
            },
            bases=(parler.models.TranslatedFieldsModelMixin, models.Model),
        ),
        migrations.CreateModel(
            name='EventsTranslation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('language_code', models.CharField(db_index=True, max_length=15, verbose_name='Language')),
                ('title', django_cryptography.fields.encrypt(models.CharField(max_length=500, verbose_name='title'))),
                ('content', django_cryptography.fields.encrypt(ckeditor_uploader.fields.RichTextUploadingField(blank=True, null=True, verbose_name='content'))),
                ('location', django_cryptography.fields.encrypt(models.CharField(blank=True, max_length=255, null=True, verbose_name='location'))),
                ('master', parler.fields.TranslationsForeignKey(editable=False, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='translations', to='education.events')),
            ],
            options={
                'verbose_name': 'event Translation',
                'db_table': 'education_events_translation',
                'db_tablespace': '',
                'managed': True,
                'default_permissions': (),
                'unique_together': {('language_code', 'master')},
            },
            bases=(parler.models.TranslatedFieldsModelMixin, models.Model),
        ),
        migrations.CreateModel(
            name='DocumentTranslation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('language_code', models.CharField(db_index=True, max_length=15, verbose_name='Language')),
                ('name', django_cryptography.fields.encrypt(models.CharField(max_length=150, verbose_name='name'))),
                ('content', django_cryptography.fields.encrypt(ckeditor_uploader.fields.RichTextUploadingField(blank=True, null=True, verbose_name='content'))),
                ('master', parler.fields.TranslationsForeignKey(editable=False, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='translations', to='education.document')),
            ],
            options={
                'verbose_name': 'document Translation',
                'db_table': 'education_document_translation',
                'db_tablespace': '',
                'managed': True,
                'default_permissions': (),
                'unique_together': {('language_code', 'master')},
            },
            bases=(parler.models.TranslatedFieldsModelMixin, models.Model),
        ),
        migrations.CreateModel(
            name='DailyAlertTranslation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('language_code', models.CharField(db_index=True, max_length=15, verbose_name='Language')),
                ('alert', django_cryptography.fields.encrypt(models.CharField(max_length=500, verbose_name='alert'))),
                ('master', parler.fields.TranslationsForeignKey(editable=False, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='translations', to='education.dailyalert')),
            ],
            options={
                'verbose_name': 'daily alert Translation',
                'db_table': 'education_dailyalert_translation',
                'db_tablespace': '',
                'managed': True,
                'default_permissions': (),
                'unique_together': {('language_code', 'master')},
            },
            bases=(parler.models.TranslatedFieldsModelMixin, models.Model),
        ),
        migrations.CreateModel(
            name='CategoriesTranslation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('language_code', models.CharField(db_index=True, max_length=15, verbose_name='Language')),
                ('name', models.CharField(max_length=50, verbose_name='categories name')),
                ('master', parler.fields.TranslationsForeignKey(editable=False, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='translations', to='education.categories')),
            ],
            options={
                'verbose_name': 'category Translation',
                'db_table': 'education_categories_translation',
                'db_tablespace': '',
                'managed': True,
                'default_permissions': (),
                'unique_together': {('language_code', 'master')},
            },
            bases=(parler.models.TranslatedFieldsModelMixin, models.Model),
        ),
        migrations.CreateModel(
            name='ArticleTranslation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('language_code', models.CharField(db_index=True, max_length=15, verbose_name='Language')),
                ('title', django_cryptography.fields.encrypt(models.CharField(max_length=500, verbose_name='title'))),
                ('content', django_cryptography.fields.encrypt(ckeditor_uploader.fields.RichTextUploadingField(blank=True, null=True, verbose_name='content'))),
                ('master', parler.fields.TranslationsForeignKey(editable=False, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='translations', to='education.article')),
            ],
            options={
                'verbose_name': 'article Translation',
                'db_table': 'education_article_translation',
                'db_tablespace': '',
                'managed': True,
                'default_permissions': (),
                'unique_together': {('language_code', 'master')},
            },
            bases=(parler.models.TranslatedFieldsModelMixin, models.Model),
        ),
        migrations.CreateModel(
            name='AnnouncementTranslation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('language_code', models.CharField(db_index=True, max_length=15, verbose_name='Language')),
                ('title', django_cryptography.fields.encrypt(models.CharField(max_length=500, verbose_name='title'))),
                ('content', django_cryptography.fields.encrypt(ckeditor_uploader.fields.RichTextUploadingField(blank=True, null=True, verbose_name='content'))),
                ('master', parler.fields.TranslationsForeignKey(editable=False, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='translations', to='education.announcement')),
            ],
            options={
                'verbose_name': 'announcement Translation',
                'db_table': 'education_announcement_translation',
                'db_tablespace': '',
                'managed': True,
                'default_permissions': (),
                'unique_together': {('language_code', 'master')},
            },
            bases=(parler.models.TranslatedFieldsModelMixin, models.Model),
        ),
    ]