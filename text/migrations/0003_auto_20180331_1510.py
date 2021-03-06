# Generated by Django 2.0.3 on 2018-03-31 22:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('text', '0002_auto_20180331_1257'),
    ]

    operations = [
        migrations.AlterField(
            model_name='gerund',
            name='weight',
            field=models.DecimalField(decimal_places=8, default=0.5, max_digits=10),
        ),
        migrations.AlterField(
            model_name='gerundimage',
            name='weight',
            field=models.DecimalField(decimal_places=8, default=0.5, max_digits=10),
        ),
        migrations.AlterField(
            model_name='image',
            name='weight',
            field=models.DecimalField(decimal_places=8, default=0.5, max_digits=10),
        ),
        migrations.AlterField(
            model_name='obj',
            name='weight',
            field=models.DecimalField(decimal_places=8, default=0.5, max_digits=10),
        ),
        migrations.AlterField(
            model_name='objectgerund',
            name='weight',
            field=models.DecimalField(decimal_places=8, default=0.5, max_digits=10),
        ),
        migrations.AlterField(
            model_name='objectimage',
            name='weight',
            field=models.DecimalField(decimal_places=8, default=0.5, max_digits=10),
        ),
        migrations.AlterField(
            model_name='subject',
            name='weight',
            field=models.DecimalField(decimal_places=8, default=0.5, max_digits=10),
        ),
        migrations.AlterField(
            model_name='subjectgerund',
            name='weight',
            field=models.DecimalField(decimal_places=8, default=0.5, max_digits=10),
        ),
        migrations.AlterField(
            model_name='subjectimage',
            name='weight',
            field=models.DecimalField(decimal_places=8, default=0.5, max_digits=10),
        ),
        migrations.AlterField(
            model_name='subjectobject',
            name='weight',
            field=models.DecimalField(decimal_places=8, default=0.5, max_digits=10),
        ),
        migrations.AlterField(
            model_name='subjectverb',
            name='weight',
            field=models.DecimalField(decimal_places=8, default=0.5, max_digits=10),
        ),
        migrations.AlterField(
            model_name='verb',
            name='weight',
            field=models.DecimalField(decimal_places=8, default=0.5, max_digits=10),
        ),
        migrations.AlterField(
            model_name='verbgerund',
            name='weight',
            field=models.DecimalField(decimal_places=8, default=0.5, max_digits=10),
        ),
        migrations.AlterField(
            model_name='verbimage',
            name='weight',
            field=models.DecimalField(decimal_places=8, default=0.5, max_digits=10),
        ),
        migrations.AlterField(
            model_name='verbobject',
            name='weight',
            field=models.DecimalField(decimal_places=8, default=0.5, max_digits=10),
        ),
    ]
