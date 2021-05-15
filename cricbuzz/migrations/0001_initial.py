# Generated by Django 3.1.7 on 2021-05-15 10:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Team',
            fields=[
                ('team_id', models.DecimalField(decimal_places=0, max_digits=2, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=50)),
                ('captain', models.CharField(max_length=50)),
                ('logo', models.ImageField(upload_to='media/')),
                ('club_state', models.CharField(max_length=5)),
            ],
        ),
        migrations.CreateModel(
            name='points',
            fields=[
                ('points_id', models.DecimalField(decimal_places=0, max_digits=2, primary_key=True, serialize=False)),
                ('played', models.IntegerField()),
                ('won', models.IntegerField()),
                ('lost', models.IntegerField()),
                ('tied', models.IntegerField()),
                ('points', models.IntegerField()),
                ('team', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cricbuzz.team')),
            ],
        ),
        migrations.CreateModel(
            name='Player',
            fields=[
                ('player_id', models.DecimalField(decimal_places=0, max_digits=2, primary_key=True, serialize=False)),
                ('first_name', models.CharField(max_length=50)),
                ('last_name', models.CharField(max_length=50)),
                ('image', models.ImageField(upload_to='media/')),
                ('jersey_number', models.CharField(max_length=100)),
                ('role', models.CharField(max_length=50)),
                ('matches', models.IntegerField(max_length=100)),
                ('runs', models.IntegerField(max_length=200)),
                ('Highest_score', models.IntegerField(max_length=100)),
                ('half_centuries', models.IntegerField(max_length=100)),
                ('centuries', models.IntegerField(max_length=100)),
                ('wickets', models.IntegerField(max_length=100)),
                ('team', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cricbuzz.team')),
            ],
        ),
        migrations.CreateModel(
            name='Match',
            fields=[
                ('match_id', models.DecimalField(decimal_places=0, max_digits=2, primary_key=True, serialize=False)),
                ('date', models.DateField()),
                ('time', models.TimeField()),
                ('team1_score', models.CharField(blank=True, max_length=50, null=True)),
                ('team2_score', models.CharField(blank=True, max_length=50, null=True)),
                ('team1_overs', models.CharField(blank=True, max_length=50, null=True)),
                ('team2_overs', models.CharField(blank=True, max_length=50, null=True)),
                ('result', models.CharField(blank=True, max_length=50, null=True)),
                ('team1', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='team_one', to='cricbuzz.team')),
                ('team2', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='team_two', to='cricbuzz.team')),
            ],
        ),
    ]