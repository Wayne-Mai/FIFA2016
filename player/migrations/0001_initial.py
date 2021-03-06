# Generated by Django 2.1.5 on 2019-01-19 06:51

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Country',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('name', models.TextField(blank=True, null=True)),
            ],
            options={
                'managed': False,
                'db_table': 'country',
            },
        ),
        migrations.CreateModel(
            name='League',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('name', models.TextField(blank=True, null=True)),
            ],
            options={
                'managed': False,
                'db_table': 'league',
            },
        ),
        migrations.CreateModel(
            name='Match',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('season', models.TextField(blank=True, null=True)),
                ('stage', models.IntegerField(blank=True, null=True)),
                ('date', models.TextField(blank=True, null=True)),
                ('match_api_id', models.IntegerField(blank=True, null=True, unique=True)),
                ('home_team_goal', models.IntegerField(blank=True, null=True)),
                ('away_team_goal', models.IntegerField(blank=True, null=True)),
                ('home_player_x1', models.IntegerField(blank=True, db_column='home_player_X1', null=True)),
                ('home_player_x2', models.IntegerField(blank=True, db_column='home_player_X2', null=True)),
                ('home_player_x3', models.IntegerField(blank=True, db_column='home_player_X3', null=True)),
                ('home_player_x4', models.IntegerField(blank=True, db_column='home_player_X4', null=True)),
                ('home_player_x5', models.IntegerField(blank=True, db_column='home_player_X5', null=True)),
                ('home_player_x6', models.IntegerField(blank=True, db_column='home_player_X6', null=True)),
                ('home_player_x7', models.IntegerField(blank=True, db_column='home_player_X7', null=True)),
                ('home_player_x8', models.IntegerField(blank=True, db_column='home_player_X8', null=True)),
                ('home_player_x9', models.IntegerField(blank=True, db_column='home_player_X9', null=True)),
                ('home_player_x10', models.IntegerField(blank=True, db_column='home_player_X10', null=True)),
                ('home_player_x11', models.IntegerField(blank=True, db_column='home_player_X11', null=True)),
                ('away_player_x1', models.IntegerField(blank=True, db_column='away_player_X1', null=True)),
                ('away_player_x2', models.IntegerField(blank=True, db_column='away_player_X2', null=True)),
                ('away_player_x3', models.IntegerField(blank=True, db_column='away_player_X3', null=True)),
                ('away_player_x4', models.IntegerField(blank=True, db_column='away_player_X4', null=True)),
                ('away_player_x5', models.IntegerField(blank=True, db_column='away_player_X5', null=True)),
                ('away_player_x6', models.IntegerField(blank=True, db_column='away_player_X6', null=True)),
                ('away_player_x7', models.IntegerField(blank=True, db_column='away_player_X7', null=True)),
                ('away_player_x8', models.IntegerField(blank=True, db_column='away_player_X8', null=True)),
                ('away_player_x9', models.IntegerField(blank=True, db_column='away_player_X9', null=True)),
                ('away_player_x10', models.IntegerField(blank=True, db_column='away_player_X10', null=True)),
                ('away_player_x11', models.IntegerField(blank=True, db_column='away_player_X11', null=True)),
                ('home_player_y1', models.IntegerField(blank=True, db_column='home_player_Y1', null=True)),
                ('home_player_y2', models.IntegerField(blank=True, db_column='home_player_Y2', null=True)),
                ('home_player_y3', models.IntegerField(blank=True, db_column='home_player_Y3', null=True)),
                ('home_player_y4', models.IntegerField(blank=True, db_column='home_player_Y4', null=True)),
                ('home_player_y5', models.IntegerField(blank=True, db_column='home_player_Y5', null=True)),
                ('home_player_y6', models.IntegerField(blank=True, db_column='home_player_Y6', null=True)),
                ('home_player_y7', models.IntegerField(blank=True, db_column='home_player_Y7', null=True)),
                ('home_player_y8', models.IntegerField(blank=True, db_column='home_player_Y8', null=True)),
                ('home_player_y9', models.IntegerField(blank=True, db_column='home_player_Y9', null=True)),
                ('home_player_y10', models.IntegerField(blank=True, db_column='home_player_Y10', null=True)),
                ('home_player_y11', models.IntegerField(blank=True, db_column='home_player_Y11', null=True)),
                ('away_player_y1', models.IntegerField(blank=True, db_column='away_player_Y1', null=True)),
                ('away_player_y2', models.IntegerField(blank=True, db_column='away_player_Y2', null=True)),
                ('away_player_y3', models.IntegerField(blank=True, db_column='away_player_Y3', null=True)),
                ('away_player_y4', models.IntegerField(blank=True, db_column='away_player_Y4', null=True)),
                ('away_player_y5', models.IntegerField(blank=True, db_column='away_player_Y5', null=True)),
                ('away_player_y6', models.IntegerField(blank=True, db_column='away_player_Y6', null=True)),
                ('away_player_y7', models.IntegerField(blank=True, db_column='away_player_Y7', null=True)),
                ('away_player_y8', models.IntegerField(blank=True, db_column='away_player_Y8', null=True)),
                ('away_player_y9', models.IntegerField(blank=True, db_column='away_player_Y9', null=True)),
                ('away_player_y10', models.IntegerField(blank=True, db_column='away_player_Y10', null=True)),
                ('away_player_y11', models.IntegerField(blank=True, db_column='away_player_Y11', null=True)),
                ('goal', models.TextField(blank=True, null=True)),
                ('shoton', models.TextField(blank=True, null=True)),
                ('shotoff', models.TextField(blank=True, null=True)),
                ('foulcommit', models.TextField(blank=True, null=True)),
                ('card', models.TextField(blank=True, null=True)),
                ('cross', models.TextField(blank=True, null=True)),
                ('corner', models.TextField(blank=True, null=True)),
                ('possession', models.TextField(blank=True, null=True)),
                ('b365h', models.DecimalField(blank=True, db_column='B365H', decimal_places=0, max_digits=10, null=True)),
                ('b365d', models.DecimalField(blank=True, db_column='B365D', decimal_places=0, max_digits=10, null=True)),
                ('b365a', models.DecimalField(blank=True, db_column='B365A', decimal_places=0, max_digits=10, null=True)),
                ('bwh', models.DecimalField(blank=True, db_column='BWH', decimal_places=0, max_digits=10, null=True)),
                ('bwd', models.DecimalField(blank=True, db_column='BWD', decimal_places=0, max_digits=10, null=True)),
                ('bwa', models.DecimalField(blank=True, db_column='BWA', decimal_places=0, max_digits=10, null=True)),
                ('iwh', models.DecimalField(blank=True, db_column='IWH', decimal_places=0, max_digits=10, null=True)),
                ('iwd', models.DecimalField(blank=True, db_column='IWD', decimal_places=0, max_digits=10, null=True)),
                ('iwa', models.DecimalField(blank=True, db_column='IWA', decimal_places=0, max_digits=10, null=True)),
                ('lbh', models.DecimalField(blank=True, db_column='LBH', decimal_places=0, max_digits=10, null=True)),
                ('lbd', models.DecimalField(blank=True, db_column='LBD', decimal_places=0, max_digits=10, null=True)),
                ('lba', models.DecimalField(blank=True, db_column='LBA', decimal_places=0, max_digits=10, null=True)),
                ('psh', models.DecimalField(blank=True, db_column='PSH', decimal_places=0, max_digits=10, null=True)),
                ('psd', models.DecimalField(blank=True, db_column='PSD', decimal_places=0, max_digits=10, null=True)),
                ('psa', models.DecimalField(blank=True, db_column='PSA', decimal_places=0, max_digits=10, null=True)),
                ('whh', models.DecimalField(blank=True, db_column='WHH', decimal_places=0, max_digits=10, null=True)),
                ('whd', models.DecimalField(blank=True, db_column='WHD', decimal_places=0, max_digits=10, null=True)),
                ('wha', models.DecimalField(blank=True, db_column='WHA', decimal_places=0, max_digits=10, null=True)),
                ('sjh', models.DecimalField(blank=True, db_column='SJH', decimal_places=0, max_digits=10, null=True)),
                ('sjd', models.DecimalField(blank=True, db_column='SJD', decimal_places=0, max_digits=10, null=True)),
                ('sja', models.DecimalField(blank=True, db_column='SJA', decimal_places=0, max_digits=10, null=True)),
                ('vch', models.DecimalField(blank=True, db_column='VCH', decimal_places=0, max_digits=10, null=True)),
                ('vcd', models.DecimalField(blank=True, db_column='VCD', decimal_places=0, max_digits=10, null=True)),
                ('vca', models.DecimalField(blank=True, db_column='VCA', decimal_places=0, max_digits=10, null=True)),
                ('gbh', models.DecimalField(blank=True, db_column='GBH', decimal_places=0, max_digits=10, null=True)),
                ('gbd', models.DecimalField(blank=True, db_column='GBD', decimal_places=0, max_digits=10, null=True)),
                ('gba', models.DecimalField(blank=True, db_column='GBA', decimal_places=0, max_digits=10, null=True)),
                ('bsh', models.DecimalField(blank=True, db_column='BSH', decimal_places=0, max_digits=10, null=True)),
                ('bsd', models.DecimalField(blank=True, db_column='BSD', decimal_places=0, max_digits=10, null=True)),
                ('bsa', models.DecimalField(blank=True, db_column='BSA', decimal_places=0, max_digits=10, null=True)),
            ],
            options={
                'managed': False,
                'db_table': 'match',
            },
        ),
        migrations.CreateModel(
            name='Player',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('player_api_id', models.IntegerField(blank=True, null=True, unique=True)),
                ('player_name', models.TextField(blank=True, null=True)),
                ('player_fifa_api_id', models.IntegerField(blank=True, null=True, unique=True)),
                ('birthday', models.TextField(blank=True, null=True)),
                ('height', models.IntegerField(blank=True, null=True)),
                ('weight', models.IntegerField(blank=True, null=True)),
            ],
            options={
                'managed': False,
                'db_table': 'player',
            },
        ),
        migrations.CreateModel(
            name='PlayerAttributes',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('date', models.TextField(blank=True, null=True)),
                ('overall_rating', models.IntegerField(blank=True, null=True)),
                ('potential', models.IntegerField(blank=True, null=True)),
                ('preferred_foot', models.TextField(blank=True, null=True)),
                ('attacking_work_rate', models.TextField(blank=True, null=True)),
                ('defensive_work_rate', models.TextField(blank=True, null=True)),
                ('crossing', models.IntegerField(blank=True, null=True)),
                ('finishing', models.IntegerField(blank=True, null=True)),
                ('heading_accuracy', models.IntegerField(blank=True, null=True)),
                ('short_passing', models.IntegerField(blank=True, null=True)),
                ('volleys', models.IntegerField(blank=True, null=True)),
                ('dribbling', models.IntegerField(blank=True, null=True)),
                ('curve', models.IntegerField(blank=True, null=True)),
                ('free_kick_accuracy', models.IntegerField(blank=True, null=True)),
                ('long_passing', models.IntegerField(blank=True, null=True)),
                ('ball_control', models.IntegerField(blank=True, null=True)),
                ('acceleration', models.IntegerField(blank=True, null=True)),
                ('sprint_speed', models.IntegerField(blank=True, null=True)),
                ('agility', models.IntegerField(blank=True, null=True)),
                ('reactions', models.IntegerField(blank=True, null=True)),
                ('balance', models.IntegerField(blank=True, null=True)),
                ('shot_power', models.IntegerField(blank=True, null=True)),
                ('jumping', models.IntegerField(blank=True, null=True)),
                ('stamina', models.IntegerField(blank=True, null=True)),
                ('strength', models.IntegerField(blank=True, null=True)),
                ('long_shots', models.IntegerField(blank=True, null=True)),
                ('aggression', models.IntegerField(blank=True, null=True)),
                ('interceptions', models.IntegerField(blank=True, null=True)),
                ('positioning', models.IntegerField(blank=True, null=True)),
                ('vision', models.IntegerField(blank=True, null=True)),
                ('penalties', models.IntegerField(blank=True, null=True)),
                ('marking', models.IntegerField(blank=True, null=True)),
                ('standing_tackle', models.IntegerField(blank=True, null=True)),
                ('sliding_tackle', models.IntegerField(blank=True, null=True)),
                ('gk_diving', models.IntegerField(blank=True, null=True)),
                ('gk_handling', models.IntegerField(blank=True, null=True)),
                ('gk_kicking', models.IntegerField(blank=True, null=True)),
                ('gk_positioning', models.IntegerField(blank=True, null=True)),
                ('gk_reflexes', models.IntegerField(blank=True, null=True)),
            ],
            options={
                'managed': False,
                'db_table': 'player_attributes',
            },
        ),
        migrations.CreateModel(
            name='Team',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('team_api_id', models.IntegerField(blank=True, null=True, unique=True)),
                ('team_fifa_api_id', models.IntegerField(blank=True, null=True, unique=True)),
                ('team_long_name', models.TextField(blank=True, null=True)),
                ('team_short_name', models.TextField(blank=True, null=True)),
            ],
            options={
                'managed': False,
                'db_table': 'team',
            },
        ),
        migrations.CreateModel(
            name='TeamAttributes',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('date', models.TextField(blank=True, null=True)),
                ('buildupplayspeed', models.IntegerField(blank=True, db_column='buildUpPlaySpeed', null=True)),
                ('buildupplayspeedclass', models.TextField(blank=True, db_column='buildUpPlaySpeedClass', null=True)),
                ('buildupplaydribbling', models.IntegerField(blank=True, db_column='buildUpPlayDribbling', null=True)),
                ('buildupplaydribblingclass', models.TextField(blank=True, db_column='buildUpPlayDribblingClass', null=True)),
                ('buildupplaypassing', models.IntegerField(blank=True, db_column='buildUpPlayPassing', null=True)),
                ('buildupplaypassingclass', models.TextField(blank=True, db_column='buildUpPlayPassingClass', null=True)),
                ('buildupplaypositioningclass', models.TextField(blank=True, db_column='buildUpPlayPositioningClass', null=True)),
                ('chancecreationpassing', models.IntegerField(blank=True, db_column='chanceCreationPassing', null=True)),
                ('chancecreationpassingclass', models.TextField(blank=True, db_column='chanceCreationPassingClass', null=True)),
                ('chancecreationcrossing', models.IntegerField(blank=True, db_column='chanceCreationCrossing', null=True)),
                ('chancecreationcrossingclass', models.TextField(blank=True, db_column='chanceCreationCrossingClass', null=True)),
                ('chancecreationshooting', models.IntegerField(blank=True, db_column='chanceCreationShooting', null=True)),
                ('chancecreationshootingclass', models.TextField(blank=True, db_column='chanceCreationShootingClass', null=True)),
                ('chancecreationpositioningclass', models.TextField(blank=True, db_column='chanceCreationPositioningClass', null=True)),
                ('defencepressure', models.IntegerField(blank=True, db_column='defencePressure', null=True)),
                ('defencepressureclass', models.TextField(blank=True, db_column='defencePressureClass', null=True)),
                ('defenceaggression', models.IntegerField(blank=True, db_column='defenceAggression', null=True)),
                ('defenceaggressionclass', models.TextField(blank=True, db_column='defenceAggressionClass', null=True)),
                ('defenceteamwidth', models.IntegerField(blank=True, db_column='defenceTeamWidth', null=True)),
                ('defenceteamwidthclass', models.TextField(blank=True, db_column='defenceTeamWidthClass', null=True)),
                ('defencedefenderlineclass', models.TextField(blank=True, db_column='defenceDefenderLineClass', null=True)),
            ],
            options={
                'managed': False,
                'db_table': 'team_attributes',
            },
        ),
    ]
