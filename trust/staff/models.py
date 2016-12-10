from django.db import models

from django.db import models

class Team_Member(models.Model):
    name = models.CharField(max_length = 120, blank = False)
