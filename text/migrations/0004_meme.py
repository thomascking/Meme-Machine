# Generated by Django 2.0.3 on 2018-03-31 23:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('text', '0003_auto_20180331_1510'),
    ]

    operations = [
        migrations.CreateModel(
            name='Meme',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('gerund', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='text.Gerund')),
                ('image', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='text.Image')),
                ('object', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='text.Obj')),
                ('subject', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='text.Subject')),
                ('verb', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='text.Verb')),
            ],
        ),
    ]
