from django.db import models


class Team(models.Model):
    team_id = models.DecimalField(max_digits=2, primary_key=True, decimal_places=0)
    name = models.CharField(max_length=50)
    captain = models.CharField(max_length=50)
    logo= models.ImageField(upload_to='media/')
    club_state = models.CharField(max_length=5)

    def __str__(self):
        return self.name


class Player(models.Model):
    player_id = models.DecimalField(max_digits=2, primary_key=True, decimal_places=0)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    image = models.ImageField(upload_to='media/')
    jersey_number = models.CharField(max_length=100)
    role = models.CharField(max_length=50)
    matches = models.IntegerField(max_length=100)
    runs = models.IntegerField(max_length=200)
    Highest_score = models.IntegerField(max_length=100)
    half_centuries = models.IntegerField(max_length=100)
    centuries = models.IntegerField(max_length=100)
    wickets = models.IntegerField(max_length=100)
    team = models.ForeignKey(Team, on_delete=models.CASCADE)

    def __str__(self):
        return self.jersy_number


class Match(models.Model):
    match_id = models.DecimalField(max_digits=2, primary_key=True, decimal_places=0)
    date = models.DateField()
    time = models.TimeField()
    team1 = models.ForeignKey(Team, on_delete=models.CASCADE, related_name='team_one')
    team2 = models.ForeignKey(Team, on_delete=models.CASCADE, related_name='team_two')
    team1_score = models.CharField(max_length=50, null=True, blank=True)
    team2_score = models.CharField(max_length=50, null=True, blank=True)
    team1_overs = models.CharField(max_length=50, null=True, blank=True)
    team2_overs = models.CharField(max_length=50, null=True, blank=True)
    result = models.CharField(max_length=50, null=True, blank=True)

    def __str__(self):
        return self.match_id


class points(models.Model):
    points_id = models.DecimalField(max_digits=2, primary_key=True, decimal_places=0)
    team = models.ForeignKey(Team, on_delete=models.CASCADE)
    played = models.IntegerField()
    won = models.IntegerField()
    lost = models.IntegerField()
    tied = models.IntegerField()
    points = models.IntegerField()

    def __str__(self):
        return self.points_id