from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
import mptt.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='SkosCollection',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='Collection label or name', max_length=300, verbose_name='skos:prefLabel')),
                ('label_lang', models.CharField(blank=True, default='en', help_text='Language of preferred label given above', max_length=3, verbose_name='skos:prefLabel language')),
                ('creator', models.TextField(blank=True, help_text='Person or organisation that created this collection<br>If more than one list all using a semicolon ;', verbose_name='dc:creator')),
                ('contributor', models.TextField(blank=True, help_text='Person or organisation that made contributions to the collection<br>If more than one list all using a semicolon ;', verbose_name='dc:contributor')),
                ('legacy_id', models.CharField(blank=True, max_length=200)),
                ('date_created', models.DateTimeField(default=django.utils.timezone.now, editable=False)),
                ('date_modified', models.DateTimeField(default=django.utils.timezone.now, editable=False)),
                ('created_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='skos_collection_created', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Collection',
                'ordering': ['id'],
            },
        ),
        migrations.CreateModel(
            name='SkosConceptScheme',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(help_text='Title  for new concept scheme', max_length=300, verbose_name='dc:title')),
                ('title_lang', models.CharField(blank=True, default='en', help_text='Language of title given above', max_length=3, verbose_name='dc:title language')),
                ('identifier', models.URLField(blank=True, help_text='URI to unambiguously identify current Concept Scheme')),
                ('creator', models.TextField(blank=True, help_text='Person or organisation primarily responsible for making current concept scheme<br>If more than one list all using a semicolon ;', verbose_name='dc:creator')),
                ('contributor', models.TextField(blank=True, help_text='Person or organisation that made contributions to the vocabulary<br>If more than one list all using a semicolon ;', verbose_name='dc:contributor')),
                ('language', models.TextField(blank=True, help_text='Language(s) used in concept scheme<br>If more than one list all using a semicolon ;', verbose_name='dc:language')),
                ('subject', models.TextField(blank=True, help_text='The subject of the vocabulary<br>If more than one list all using a semicolon ;', verbose_name='dc:subject')),
                ('version', models.CharField(blank=True, help_text='Current version', max_length=300)),
                ('publisher', models.CharField(blank=True, help_text='Organisation responsible for making the vocabulary available', max_length=300, verbose_name='dc:publisher')),
                ('license', models.CharField(blank=True, help_text='Information about license applied to the vocabulary', max_length=300, verbose_name='dct:license')),
                ('owner', models.CharField(blank=True, help_text='Person or organisation that owns the rights for the vocabulary', max_length=300)),
                ('relation', models.URLField(blank=True, help_text='Related resource or project<br>E.g. in case of relation to a project, add link to a project website', verbose_name='dc:relation')),
                ('coverage', models.TextField(blank=True, help_text='Spatial or temporal frame that the vocabulary relates to<br>If more than one list all using a semicolon ;', verbose_name='dc:coverage')),
                ('legacy_id', models.CharField(blank=True, max_length=200)),
                ('date_created', models.DateTimeField(default=django.utils.timezone.now, editable=False)),
                ('date_modified', models.DateTimeField(default=django.utils.timezone.now, editable=False)),
                ('date_issued', models.DateField(blank=True, help_text='Date of official publication of this concept scheme', null=True)),
                ('created_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='skos_cs_created', to=settings.AUTH_USER_MODEL)),
                ('curator', models.ManyToManyField(blank=True, help_text='The selected user(s) will be able to view and edit this Concept Scheme', related_name='skos_cs_curated', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Concept Scheme',
                'ordering': ['id'],
            },
        ),
        migrations.CreateModel(
            name='SkosConcept',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pref_label', models.CharField(help_text='Preferred label for concept', max_length=300, verbose_name='skos:prefLabel')),
                ('pref_label_lang', models.CharField(blank=True, default='en', help_text='Language of preferred label given above', max_length=3, verbose_name='skos:prefLabel language')),
                ('top_concept', models.BooleanField(help_text='Is this concept a top concept of concept scheme?', null=True)),
                ('notation', models.CharField(blank=True, help_text='A notation is a unique string used        to identify the concept in current vocabulary', max_length=300, verbose_name='skos:notation')),
                ('related', models.TextField(blank=True, help_text='An associative relationship between two concepts', verbose_name='skos:related')),
                ('broad_match', models.TextField(blank=True, help_text='External concept with a broader meaning', verbose_name='skos:broadMatch')),
                ('narrow_match', models.TextField(blank=True, help_text='External concept with a narrower meaning', verbose_name='skos:narrowMatch')),
                ('exact_match', models.TextField(blank=True, help_text='External concept that can be used interchangeably and has the exact same meaning', verbose_name='skos:exactMatch')),
                ('related_match', models.TextField(blank=True, help_text='External concept that has an associative relationship with this concept', verbose_name='skos:relatedMatch')),
                ('close_match', models.TextField(blank=True, help_text='External concept that has a similar meaning', verbose_name='skos:closeMatch')),
                ('legacy_id', models.CharField(blank=True, max_length=200)),
                ('creator', models.TextField(blank=True, help_text='Person or organisation that created this concept<br>If more than one list all using a semicolon ;', verbose_name='dc:creator')),
                ('contributor', models.TextField(blank=True, help_text='Person or organisation that made contributions to this concept<br>If more than one list all using a semicolon ;', verbose_name='dc:contributor')),
                ('needs_review', models.BooleanField(help_text='Check if this concept needs to be reviewed', null=True)),
                ('date_created', models.DateTimeField(default=django.utils.timezone.now, editable=False, verbose_name='dct:created')),
                ('date_modified', models.DateTimeField(default=django.utils.timezone.now, editable=False, verbose_name='dct:modified')),
                ('lft', models.PositiveIntegerField(db_index=True, editable=False)),
                ('rght', models.PositiveIntegerField(db_index=True, editable=False)),
                ('tree_id', models.PositiveIntegerField(db_index=True, editable=False)),
                ('level', models.PositiveIntegerField(db_index=True, editable=False)),
                ('broader_concept', mptt.fields.TreeForeignKey(blank=True, help_text='Concept with a broader meaning that this concept inherits from', null=True, on_delete=django.db.models.deletion.CASCADE, related_name='narrower_concepts', to='vocabs.SkosConcept', verbose_name='skos:broader')),
                ('collection', models.ManyToManyField(blank=True, help_text='Collection that this concept is a member of', related_name='has_members', to='vocabs.SkosCollection', verbose_name='member of skos:Collection')),
                ('created_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='skos_concept_created', to=settings.AUTH_USER_MODEL)),
                ('scheme', models.ForeignKey(help_text='Concept scheme to which this concept belongs', on_delete=django.db.models.deletion.CASCADE, related_name='has_concepts', to='vocabs.SkosConceptScheme', verbose_name='skos:inScheme')),
            ],
            options={
                'verbose_name': 'Concept',
            },
        ),
        migrations.AddField(
            model_name='skoscollection',
            name='scheme',
            field=models.ForeignKey(help_text='Concept scheme that this collection belongs to', on_delete=django.db.models.deletion.CASCADE, related_name='has_collections', to='vocabs.SkosConceptScheme', verbose_name='skos:ConceptScheme'),
        ),
        migrations.CreateModel(
            name='ConceptSource',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField(help_text="Verbal description of the concept's source", verbose_name='dc:source')),
                ('language', models.CharField(help_text='Language of source given above', max_length=3, verbose_name='language')),
                ('concept', models.ForeignKey(help_text='Which Skos:Concept current source belongs to', on_delete=django.db.models.deletion.CASCADE, related_name='has_sources', to='vocabs.SkosConcept', verbose_name='skos:Concept')),
            ],
        ),
        migrations.CreateModel(
            name='ConceptSchemeTitle',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='Other title for new concept scheme', max_length=500, verbose_name='dc:title')),
                ('language', models.CharField(help_text='Language of title given above', max_length=3, verbose_name='dc:title language')),
                ('concept_scheme', models.ForeignKey(help_text='Which Skos:ConceptScheme current Title belongs to', on_delete=django.db.models.deletion.CASCADE, related_name='has_titles', to='vocabs.SkosConceptScheme', verbose_name='skos:ConceptScheme')),
            ],
        ),
        migrations.CreateModel(
            name='ConceptSchemeSource',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField(help_text="Verbal description of a concept scheme's source", verbose_name='dc:source')),
                ('language', models.CharField(help_text='Language of source given above', max_length=3, verbose_name='dc:source language')),
                ('concept_scheme', models.ForeignKey(help_text='Which Skos:ConceptScheme current source belongs to', on_delete=django.db.models.deletion.CASCADE, related_name='has_sources', to='vocabs.SkosConceptScheme', verbose_name='skos:ConceptScheme')),
            ],
        ),
        migrations.CreateModel(
            name='ConceptSchemeDescription',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField(help_text='Description of concept scheme', verbose_name='dc:description')),
                ('language', models.CharField(help_text='Language of description given above', max_length=3, verbose_name='dc:description language')),
                ('concept_scheme', models.ForeignKey(help_text='Which Skos:ConceptScheme current Description belongs to', on_delete=django.db.models.deletion.CASCADE, related_name='has_descriptions', to='vocabs.SkosConceptScheme', verbose_name='skos:ConceptScheme')),
            ],
        ),
        migrations.CreateModel(
            name='ConceptNote',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField(help_text='Provide some information about this concept', verbose_name='documentary note')),
                ('language', models.CharField(help_text='Language of note given above', max_length=3, verbose_name='language')),
                ('note_type', models.CharField(choices=[('note', 'note'), ('scopeNote', 'scopeNote'), ('changeNote', 'changeNote'), ('editorialNote', 'editorialNote'), ('historyNote', 'historyNote'), ('definition', 'definition'), ('example', 'example')], default='note', help_text='Choose note type', max_length=15, verbose_name='note type')),
                ('concept', models.ForeignKey(help_text='Which Skos:Concept current documentary note belongs to', on_delete=django.db.models.deletion.CASCADE, related_name='has_notes', to='vocabs.SkosConcept', verbose_name='skos:Concept')),
            ],
        ),
        migrations.CreateModel(
            name='ConceptLabel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='Other label for this concept', max_length=500, verbose_name='label')),
                ('language', models.CharField(help_text='Language of label given above', max_length=3, verbose_name='language')),
                ('label_type', models.CharField(choices=[('prefLabel', 'prefLabel'), ('altLabel', 'altLabel'), ('hiddenLabel', 'hiddenLabel')], default='altLabel', help_text='Choose label type', max_length=12, verbose_name='label type')),
                ('concept', models.ForeignKey(help_text='Which Skos:Concept current label belongs to', on_delete=django.db.models.deletion.CASCADE, related_name='has_labels', to='vocabs.SkosConcept', verbose_name='skos:Concept')),
            ],
        ),
        migrations.CreateModel(
            name='CollectionSource',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField(help_text="Verbal description of the collection's source", verbose_name='dc:source')),
                ('language', models.CharField(help_text='Language of source given above', max_length=3, verbose_name='language')),
                ('collection', models.ForeignKey(help_text='Which Skos:Collection current source belongs to', on_delete=django.db.models.deletion.CASCADE, related_name='has_sources', to='vocabs.SkosCollection', verbose_name='skos:Collection')),
            ],
        ),
        migrations.CreateModel(
            name='CollectionNote',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField(help_text='Provide some information about this collection', verbose_name='documentary note')),
                ('language', models.CharField(help_text='Language of note given above', max_length=3, verbose_name='language')),
                ('note_type', models.CharField(choices=[('note', 'note'), ('scopeNote', 'scopeNote'), ('changeNote', 'changeNote'), ('editorialNote', 'editorialNote'), ('historyNote', 'historyNote'), ('definition', 'definition'), ('example', 'example')], default='note', help_text='Choose note type', max_length=15, verbose_name='note type')),
                ('collection', models.ForeignKey(help_text='Which Skos:Collection current documentary note belongs to', on_delete=django.db.models.deletion.CASCADE, related_name='has_notes', to='vocabs.SkosCollection', verbose_name='skos:Collection')),
            ],
        ),
        migrations.CreateModel(
            name='CollectionLabel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='Other label for this collection', max_length=500, verbose_name='label')),
                ('language', models.CharField(help_text='Language of label given above', max_length=3, verbose_name='language')),
                ('label_type', models.CharField(choices=[('prefLabel', 'prefLabel'), ('altLabel', 'altLabel'), ('hiddenLabel', 'hiddenLabel')], default='altLabel', help_text='Choose label type', max_length=12, verbose_name='label type')),
                ('collection', models.ForeignKey(help_text='Which Skos:Collection current label belongs to', on_delete=django.db.models.deletion.CASCADE, related_name='has_labels', to='vocabs.SkosCollection', verbose_name='skos:Collection')),
            ],
        ),
    ]
