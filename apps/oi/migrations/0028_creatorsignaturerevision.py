# Generated by Django 2.2.12 on 2020-05-29 20:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('gcd', '0029_creatorsignature'),
        ('oi', '0027_add_printer'),
    ]

    operations = [
        migrations.CreateModel(
            name='CreatorSignatureRevision',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('deleted', models.BooleanField(db_index=True, default=False)),
                ('committed', models.NullBooleanField(db_index=True, default=None)),
                ('created', models.DateTimeField(auto_now_add=True, db_index=True)),
                ('modified', models.DateTimeField(auto_now=True, db_index=True)),
                ('name', models.CharField(max_length=255)),
                ('generic', models.BooleanField(default=False)),
                ('notes', models.TextField(blank=True)),
                ('changeset', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='creatorsignaturerevisions', to='oi.Changeset')),
                ('creator', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='signature_revisions', to='gcd.Creator')),
                ('creator_signature', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='revisions', to='gcd.CreatorSignature')),
                ('image_revision', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='signature_revisions', to='oi.ImageRevision')),
                ('previous_revision', models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='next_revision', to='oi.CreatorSignatureRevision')),
            ],
            options={
                'verbose_name_plural': 'Creator Signature Revisions',
                'db_table': 'oi_creator_signature_revision',
                'ordering': ['name', '-creator__sort_name', '-creator__birth_date__year'],
            },
        ),
    ]
