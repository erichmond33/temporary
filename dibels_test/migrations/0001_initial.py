# Generated by Django 4.0.3 on 2022-07-12 15:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Font',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('link', models.CharField(max_length=50)),
                ('style', models.CharField(max_length=75)),
                ('size', models.CharField(max_length=20)),
                ('angular', models.FloatField(blank=True)),
                ('artistic', models.FloatField(blank=True)),
                ('attention_grabbing', models.FloatField(blank=True)),
                ('attractive', models.FloatField(blank=True)),
                ('bad', models.FloatField(blank=True)),
                ('boring', models.FloatField(blank=True)),
                ('calm', models.FloatField(blank=True)),
                ('capitals', models.FloatField(blank=True)),
                ('charming', models.FloatField(blank=True)),
                ('clumsy', models.FloatField(blank=True)),
                ('complex', models.FloatField(blank=True)),
                ('cursive', models.FloatField(blank=True)),
                ('delicate', models.FloatField(blank=True)),
                ('disorderly', models.FloatField(blank=True)),
                ('display', models.FloatField(blank=True)),
                ('dramatic', models.FloatField(blank=True)),
                ('formal', models.FloatField(blank=True)),
                ('fresh', models.FloatField(blank=True)),
                ('friendly', models.FloatField(blank=True)),
                ('gentle', models.FloatField(blank=True)),
                ('graceful', models.FloatField(blank=True)),
                ('happy', models.FloatField(blank=True)),
                ('italic', models.FloatField(blank=True)),
                ('legible', models.FloatField(blank=True)),
                ('modern', models.FloatField(blank=True)),
                ('monospace', models.FloatField(blank=True)),
                ('playful', models.FloatField(blank=True)),
                ('pretentious', models.FloatField(blank=True)),
                ('serif', models.FloatField(blank=True)),
                ('sharp', models.FloatField(blank=True)),
                ('sloppy', models.FloatField(blank=True)),
                ('soft', models.FloatField(blank=True)),
                ('strong', models.FloatField(blank=True)),
                ('technical', models.FloatField(blank=True)),
                ('thin', models.FloatField(blank=True)),
                ('warm', models.FloatField(blank=True)),
                ('wide', models.FloatField(blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='Image',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('body', models.CharField(max_length=30)),
                ('gradeLevel', models.CharField(default='null', max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='imageQuestionAttempt',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('wordSelection', models.CharField(max_length=50)),
                ('wordAttempt', models.CharField(max_length=50)),
                ('correct', models.BooleanField(blank=True)),
                ('font', models.ForeignKey(default=230, on_delete=django.db.models.deletion.CASCADE, to='dibels_test.font')),
            ],
        ),
        migrations.CreateModel(
            name='imageTest',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('testAdmin', models.CharField(default='null', max_length=50)),
                ('gradeLevel', models.CharField(default='null', max_length=20)),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('imageQuestionAttempts', models.ManyToManyField(related_name='imageQuestionAttemps', to='dibels_test.imagequestionattempt')),
            ],
        ),
        migrations.CreateModel(
            name='mazeQuestionAttempt',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('wordSelection', models.CharField(max_length=50)),
                ('wordAttempt', models.CharField(max_length=50)),
                ('correct', models.BooleanField(blank=True)),
                ('font', models.ForeignKey(default=230, on_delete=django.db.models.deletion.CASCADE, to='dibels_test.font')),
            ],
        ),
        migrations.CreateModel(
            name='mazeTest',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('testAdmin', models.CharField(default='null', max_length=50)),
                ('gradeLevel', models.CharField(default='null', max_length=20)),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('mazeQuestionAttempts', models.ManyToManyField(related_name='mazeQuestionAttemps', to='dibels_test.mazequestionattempt')),
            ],
        ),
        migrations.CreateModel(
            name='Sentence',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('body', models.TextField(blank=True)),
                ('gradeLevel', models.CharField(default='null', max_length=20)),
                ('selectedWord', models.CharField(max_length=50)),
                ('distractorWord1', models.CharField(max_length=50)),
                ('distractorWord2', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='queuedMazeQuestion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('queuedSentenceId', models.IntegerField(default='-1')),
                ('queuedWordSelection', models.CharField(blank=True, max_length=50)),
                ('queuedGeneratedWord1', models.CharField(blank=True, max_length=50)),
                ('queuedGeneratedWord2', models.CharField(blank=True, max_length=50)),
                ('font', models.ForeignKey(default=300, on_delete=django.db.models.deletion.CASCADE, to='dibels_test.font')),
                ('testId', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dibels_test.mazetest')),
            ],
        ),
        migrations.CreateModel(
            name='queuedImageQuestion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('queuedImageSelection', models.CharField(default='null', max_length=50)),
                ('queuedGeneratedWord1', models.CharField(blank=True, max_length=50)),
                ('queuedGeneratedWord2', models.CharField(blank=True, max_length=50)),
                ('font', models.ForeignKey(default=160, on_delete=django.db.models.deletion.CASCADE, to='dibels_test.font')),
                ('testId', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dibels_test.imagetest')),
            ],
        ),
        migrations.AddField(
            model_name='mazequestionattempt',
            name='question',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dibels_test.sentence'),
        ),
    ]