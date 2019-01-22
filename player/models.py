from django.db import models

# Create your models here.
# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Country(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'country'


class League(models.Model):
    id = models.IntegerField(primary_key=True)
    country = models.ForeignKey(Country, models.DO_NOTHING, blank=True, null=True)
    name = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'league'


class Match(models.Model):
    id = models.IntegerField(primary_key=True)
    country = models.ForeignKey(Country, models.DO_NOTHING, blank=True, null=True)
    league = models.ForeignKey(League, models.DO_NOTHING, blank=True, null=True)
    season = models.TextField(blank=True, null=True)
    stage = models.IntegerField(blank=True, null=True)
    date = models.TextField(blank=True, null=True)
    match_api_id = models.IntegerField(unique=True, blank=True, null=True)
    home_team_api = models.ForeignKey('Team', models.DO_NOTHING, blank=True, null=True,related_name='home_team_api')
    away_team_api = models.ForeignKey('Team', models.DO_NOTHING, blank=True, null=True,related_name='away_team_api')
    home_team_goal = models.IntegerField(blank=True, null=True)
    away_team_goal = models.IntegerField(blank=True, null=True)
    home_player_x1 = models.IntegerField(db_column='home_player_X1', blank=True, null=True)  # Field name made lowercase.
    home_player_x2 = models.IntegerField(db_column='home_player_X2', blank=True, null=True)  # Field name made lowercase.
    home_player_x3 = models.IntegerField(db_column='home_player_X3', blank=True, null=True)  # Field name made lowercase.
    home_player_x4 = models.IntegerField(db_column='home_player_X4', blank=True, null=True)  # Field name made lowercase.
    home_player_x5 = models.IntegerField(db_column='home_player_X5', blank=True, null=True)  # Field name made lowercase.
    home_player_x6 = models.IntegerField(db_column='home_player_X6', blank=True, null=True)  # Field name made lowercase.
    home_player_x7 = models.IntegerField(db_column='home_player_X7', blank=True, null=True)  # Field name made lowercase.
    home_player_x8 = models.IntegerField(db_column='home_player_X8', blank=True, null=True)  # Field name made lowercase.
    home_player_x9 = models.IntegerField(db_column='home_player_X9', blank=True, null=True)  # Field name made lowercase.
    home_player_x10 = models.IntegerField(db_column='home_player_X10', blank=True, null=True)  # Field name made lowercase.
    home_player_x11 = models.IntegerField(db_column='home_player_X11', blank=True, null=True)  # Field name made lowercase.
    away_player_x1 = models.IntegerField(db_column='away_player_X1', blank=True, null=True)  # Field name made lowercase.
    away_player_x2 = models.IntegerField(db_column='away_player_X2', blank=True, null=True)  # Field name made lowercase.
    away_player_x3 = models.IntegerField(db_column='away_player_X3', blank=True, null=True)  # Field name made lowercase.
    away_player_x4 = models.IntegerField(db_column='away_player_X4', blank=True, null=True)  # Field name made lowercase.
    away_player_x5 = models.IntegerField(db_column='away_player_X5', blank=True, null=True)  # Field name made lowercase.
    away_player_x6 = models.IntegerField(db_column='away_player_X6', blank=True, null=True)  # Field name made lowercase.
    away_player_x7 = models.IntegerField(db_column='away_player_X7', blank=True, null=True)  # Field name made lowercase.
    away_player_x8 = models.IntegerField(db_column='away_player_X8', blank=True, null=True)  # Field name made lowercase.
    away_player_x9 = models.IntegerField(db_column='away_player_X9', blank=True, null=True)  # Field name made lowercase.
    away_player_x10 = models.IntegerField(db_column='away_player_X10', blank=True, null=True)  # Field name made lowercase.
    away_player_x11 = models.IntegerField(db_column='away_player_X11', blank=True, null=True)  # Field name made lowercase.
    home_player_y1 = models.IntegerField(db_column='home_player_Y1', blank=True, null=True)  # Field name made lowercase.
    home_player_y2 = models.IntegerField(db_column='home_player_Y2', blank=True, null=True)  # Field name made lowercase.
    home_player_y3 = models.IntegerField(db_column='home_player_Y3', blank=True, null=True)  # Field name made lowercase.
    home_player_y4 = models.IntegerField(db_column='home_player_Y4', blank=True, null=True)  # Field name made lowercase.
    home_player_y5 = models.IntegerField(db_column='home_player_Y5', blank=True, null=True)  # Field name made lowercase.
    home_player_y6 = models.IntegerField(db_column='home_player_Y6', blank=True, null=True)  # Field name made lowercase.
    home_player_y7 = models.IntegerField(db_column='home_player_Y7', blank=True, null=True)  # Field name made lowercase.
    home_player_y8 = models.IntegerField(db_column='home_player_Y8', blank=True, null=True)  # Field name made lowercase.
    home_player_y9 = models.IntegerField(db_column='home_player_Y9', blank=True, null=True)  # Field name made lowercase.
    home_player_y10 = models.IntegerField(db_column='home_player_Y10', blank=True, null=True)  # Field name made lowercase.
    home_player_y11 = models.IntegerField(db_column='home_player_Y11', blank=True, null=True)  # Field name made lowercase.
    away_player_y1 = models.IntegerField(db_column='away_player_Y1', blank=True, null=True)  # Field name made lowercase.
    away_player_y2 = models.IntegerField(db_column='away_player_Y2', blank=True, null=True)  # Field name made lowercase.
    away_player_y3 = models.IntegerField(db_column='away_player_Y3', blank=True, null=True)  # Field name made lowercase.
    away_player_y4 = models.IntegerField(db_column='away_player_Y4', blank=True, null=True)  # Field name made lowercase.
    away_player_y5 = models.IntegerField(db_column='away_player_Y5', blank=True, null=True)  # Field name made lowercase.
    away_player_y6 = models.IntegerField(db_column='away_player_Y6', blank=True, null=True)  # Field name made lowercase.
    away_player_y7 = models.IntegerField(db_column='away_player_Y7', blank=True, null=True)  # Field name made lowercase.
    away_player_y8 = models.IntegerField(db_column='away_player_Y8', blank=True, null=True)  # Field name made lowercase.
    away_player_y9 = models.IntegerField(db_column='away_player_Y9', blank=True, null=True)  # Field name made lowercase.
    away_player_y10 = models.IntegerField(db_column='away_player_Y10', blank=True, null=True)  # Field name made lowercase.
    away_player_y11 = models.IntegerField(db_column='away_player_Y11', blank=True, null=True)  # Field name made lowercase.
    home_player_1 = models.ForeignKey('Player', models.DO_NOTHING, related_name='home_player_1', db_column='home_player_1', blank=True, null=True)
    home_player_2 = models.ForeignKey('Player', models.DO_NOTHING, related_name='home_player_2', db_column='home_player_2', blank=True, null=True)
    home_player_3 = models.ForeignKey('Player', models.DO_NOTHING, related_name='home_player_3', db_column='home_player_3', blank=True, null=True)
    home_player_4 = models.ForeignKey('Player', models.DO_NOTHING, related_name='home_player_4', db_column='home_player_4', blank=True, null=True)
    home_player_5 = models.ForeignKey('Player', models.DO_NOTHING, related_name='home_player_5', db_column='home_player_5', blank=True, null=True)
    home_player_6 = models.ForeignKey('Player', models.DO_NOTHING, related_name='home_player_6', db_column='home_player_6', blank=True, null=True)
    home_player_7 = models.ForeignKey('Player', models.DO_NOTHING, related_name='home_player_7', db_column='home_player_7', blank=True, null=True)
    home_player_8 = models.ForeignKey('Player', models.DO_NOTHING, related_name='home_player_8', db_column='home_player_8', blank=True, null=True)
    home_player_9 = models.ForeignKey('Player', models.DO_NOTHING, related_name='home_player_9', db_column='home_player_9', blank=True, null=True)
    home_player_10 = models.ForeignKey('Player', models.DO_NOTHING, related_name='home_player_10', db_column='home_player_10', blank=True, null=True)
    home_player_11 = models.ForeignKey('Player', models.DO_NOTHING, related_name='home_player_11', db_column='home_player_11', blank=True, null=True)
    away_player_1 = models.ForeignKey('Player', models.DO_NOTHING, related_name='away_player_1', db_column='away_player_1', blank=True, null=True)
    away_player_2 = models.ForeignKey('Player', models.DO_NOTHING, related_name='away_player_2', db_column='away_player_2', blank=True, null=True)
    away_player_3 = models.ForeignKey('Player', models.DO_NOTHING, related_name='away_player_3', db_column='away_player_3', blank=True, null=True)
    away_player_4 = models.ForeignKey('Player', models.DO_NOTHING, related_name='away_player_4', db_column='away_player_4', blank=True, null=True)
    away_player_5 = models.ForeignKey('Player', models.DO_NOTHING, related_name='away_player_5', db_column='away_player_5', blank=True, null=True)
    away_player_6 = models.ForeignKey('Player', models.DO_NOTHING, related_name='away_player_6', db_column='away_player_6', blank=True, null=True)
    away_player_7 = models.ForeignKey('Player', models.DO_NOTHING, related_name='away_player_7', db_column='away_player_7', blank=True, null=True)
    away_player_8 = models.ForeignKey('Player', models.DO_NOTHING, related_name='away_player_8', db_column='away_player_8', blank=True, null=True)
    away_player_9 = models.ForeignKey('Player', models.DO_NOTHING, related_name='away_player_9', db_column='away_player_9', blank=True, null=True)
    away_player_10 = models.ForeignKey('Player', models.DO_NOTHING, related_name='away_player_10', db_column='away_player_10', blank=True, null=True)
    away_player_11 = models.ForeignKey('Player', models.DO_NOTHING, related_name='away_player_11', db_column='away_player_11', blank=True, null=True)
    goal = models.TextField(blank=True, null=True)
    shoton = models.TextField(blank=True, null=True)
    shotoff = models.TextField(blank=True, null=True)
    foulcommit = models.TextField(blank=True, null=True)
    card = models.TextField(blank=True, null=True)
    cross = models.TextField(blank=True, null=True)
    corner = models.TextField(blank=True, null=True)
    possession = models.TextField(blank=True, null=True)
    b365h = models.DecimalField(db_column='B365H', max_digits=10, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    b365d = models.DecimalField(db_column='B365D', max_digits=10, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    b365a = models.DecimalField(db_column='B365A', max_digits=10, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    bwh = models.DecimalField(db_column='BWH', max_digits=10, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    bwd = models.DecimalField(db_column='BWD', max_digits=10, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    bwa = models.DecimalField(db_column='BWA', max_digits=10, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    iwh = models.DecimalField(db_column='IWH', max_digits=10, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    iwd = models.DecimalField(db_column='IWD', max_digits=10, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    iwa = models.DecimalField(db_column='IWA', max_digits=10, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    lbh = models.DecimalField(db_column='LBH', max_digits=10, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    lbd = models.DecimalField(db_column='LBD', max_digits=10, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    lba = models.DecimalField(db_column='LBA', max_digits=10, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    psh = models.DecimalField(db_column='PSH', max_digits=10, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    psd = models.DecimalField(db_column='PSD', max_digits=10, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    psa = models.DecimalField(db_column='PSA', max_digits=10, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    whh = models.DecimalField(db_column='WHH', max_digits=10, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    whd = models.DecimalField(db_column='WHD', max_digits=10, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    wha = models.DecimalField(db_column='WHA', max_digits=10, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    sjh = models.DecimalField(db_column='SJH', max_digits=10, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    sjd = models.DecimalField(db_column='SJD', max_digits=10, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    sja = models.DecimalField(db_column='SJA', max_digits=10, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    vch = models.DecimalField(db_column='VCH', max_digits=10, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    vcd = models.DecimalField(db_column='VCD', max_digits=10, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    vca = models.DecimalField(db_column='VCA', max_digits=10, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    gbh = models.DecimalField(db_column='GBH', max_digits=10, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    gbd = models.DecimalField(db_column='GBD', max_digits=10, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    gba = models.DecimalField(db_column='GBA', max_digits=10, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    bsh = models.DecimalField(db_column='BSH', max_digits=10, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    bsd = models.DecimalField(db_column='BSD', max_digits=10, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    bsa = models.DecimalField(db_column='BSA', max_digits=10, decimal_places=0, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'match'


class Player(models.Model):
    id = models.IntegerField(primary_key=True)
    player_api_id = models.IntegerField(unique=True, blank=True, null=True)
    player_name = models.TextField(blank=True, null=True)
    player_fifa_api_id = models.IntegerField(unique=True, blank=True, null=True)
    birthday = models.TextField(blank=True, null=True)
    height = models.IntegerField(blank=True, null=True)
    weight = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'player'


class PlayerAttributes(models.Model):
    id = models.IntegerField(primary_key=True)
    player_fifa_api = models.ForeignKey(Player, models.DO_NOTHING, blank=True, null=True,related_name='player_fifa_api')
    player_api = models.ForeignKey(Player, models.DO_NOTHING, blank=True, null=True,related_name='player_api')
    date = models.TextField(blank=True, null=True)
    overall_rating = models.IntegerField(blank=True, null=True)
    potential = models.IntegerField(blank=True, null=True)
    preferred_foot = models.TextField(blank=True, null=True)
    attacking_work_rate = models.TextField(blank=True, null=True)
    defensive_work_rate = models.TextField(blank=True, null=True)
    crossing = models.IntegerField(blank=True, null=True)
    finishing = models.IntegerField(blank=True, null=True)
    heading_accuracy = models.IntegerField(blank=True, null=True)
    short_passing = models.IntegerField(blank=True, null=True)
    volleys = models.IntegerField(blank=True, null=True)
    dribbling = models.IntegerField(blank=True, null=True)
    curve = models.IntegerField(blank=True, null=True)
    free_kick_accuracy = models.IntegerField(blank=True, null=True)
    long_passing = models.IntegerField(blank=True, null=True)
    ball_control = models.IntegerField(blank=True, null=True)
    acceleration = models.IntegerField(blank=True, null=True)
    sprint_speed = models.IntegerField(blank=True, null=True)
    agility = models.IntegerField(blank=True, null=True)
    reactions = models.IntegerField(blank=True, null=True)
    balance = models.IntegerField(blank=True, null=True)
    shot_power = models.IntegerField(blank=True, null=True)
    jumping = models.IntegerField(blank=True, null=True)
    stamina = models.IntegerField(blank=True, null=True)
    strength = models.IntegerField(blank=True, null=True)
    long_shots = models.IntegerField(blank=True, null=True)
    aggression = models.IntegerField(blank=True, null=True)
    interceptions = models.IntegerField(blank=True, null=True)
    positioning = models.IntegerField(blank=True, null=True)
    vision = models.IntegerField(blank=True, null=True)
    penalties = models.IntegerField(blank=True, null=True)
    marking = models.IntegerField(blank=True, null=True)
    standing_tackle = models.IntegerField(blank=True, null=True)
    sliding_tackle = models.IntegerField(blank=True, null=True)
    gk_diving = models.IntegerField(blank=True, null=True)
    gk_handling = models.IntegerField(blank=True, null=True)
    gk_kicking = models.IntegerField(blank=True, null=True)
    gk_positioning = models.IntegerField(blank=True, null=True)
    gk_reflexes = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'player_attributes'


class Team(models.Model):
    id = models.IntegerField(primary_key=True)
    team_api_id = models.IntegerField(unique=True, blank=True, null=True)
    team_fifa_api_id = models.IntegerField(unique=True, blank=True, null=True)
    team_long_name = models.TextField(blank=True, null=True)
    team_short_name = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'team'


class TeamAttributes(models.Model):
    id = models.IntegerField(primary_key=True)
    team_fifa_api = models.ForeignKey(Team, models.DO_NOTHING, blank=True, null=True,related_name='team_fifa_api')
    team_api = models.ForeignKey(Team, models.DO_NOTHING, blank=True, null=True,related_name='team_api')
    date = models.TextField(blank=True, null=True)
    buildupplayspeed = models.IntegerField(db_column='buildUpPlaySpeed', blank=True, null=True)  # Field name made lowercase.
    buildupplayspeedclass = models.TextField(db_column='buildUpPlaySpeedClass', blank=True, null=True)  # Field name made lowercase.
    buildupplaydribbling = models.IntegerField(db_column='buildUpPlayDribbling', blank=True, null=True)  # Field name made lowercase.
    buildupplaydribblingclass = models.TextField(db_column='buildUpPlayDribblingClass', blank=True, null=True)  # Field name made lowercase.
    buildupplaypassing = models.IntegerField(db_column='buildUpPlayPassing', blank=True, null=True)  # Field name made lowercase.
    buildupplaypassingclass = models.TextField(db_column='buildUpPlayPassingClass', blank=True, null=True)  # Field name made lowercase.
    buildupplaypositioningclass = models.TextField(db_column='buildUpPlayPositioningClass', blank=True, null=True)  # Field name made lowercase.
    chancecreationpassing = models.IntegerField(db_column='chanceCreationPassing', blank=True, null=True)  # Field name made lowercase.
    chancecreationpassingclass = models.TextField(db_column='chanceCreationPassingClass', blank=True, null=True)  # Field name made lowercase.
    chancecreationcrossing = models.IntegerField(db_column='chanceCreationCrossing', blank=True, null=True)  # Field name made lowercase.
    chancecreationcrossingclass = models.TextField(db_column='chanceCreationCrossingClass', blank=True, null=True)  # Field name made lowercase.
    chancecreationshooting = models.IntegerField(db_column='chanceCreationShooting', blank=True, null=True)  # Field name made lowercase.
    chancecreationshootingclass = models.TextField(db_column='chanceCreationShootingClass', blank=True, null=True)  # Field name made lowercase.
    chancecreationpositioningclass = models.TextField(db_column='chanceCreationPositioningClass', blank=True, null=True)  # Field name made lowercase.
    defencepressure = models.IntegerField(db_column='defencePressure', blank=True, null=True)  # Field name made lowercase.
    defencepressureclass = models.TextField(db_column='defencePressureClass', blank=True, null=True)  # Field name made lowercase.
    defenceaggression = models.IntegerField(db_column='defenceAggression', blank=True, null=True)  # Field name made lowercase.
    defenceaggressionclass = models.TextField(db_column='defenceAggressionClass', blank=True, null=True)  # Field name made lowercase.
    defenceteamwidth = models.IntegerField(db_column='defenceTeamWidth', blank=True, null=True)  # Field name made lowercase.
    defenceteamwidthclass = models.TextField(db_column='defenceTeamWidthClass', blank=True, null=True)  # Field name made lowercase.
    defencedefenderlineclass = models.TextField(db_column='defenceDefenderLineClass', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'team_attributes'
