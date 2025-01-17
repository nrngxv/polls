from django.db import models


class Poll(models.Model):
    question = models.TextField()
    option_one = models.CharField(max_length=30)
    option_two = models.CharField(max_length=30)
    option_three = models.CharField(max_length=30)
    #counting the total number of option input by the user
    option_one_count = models.IntegerField(default=0)
    option_two_count = models.IntegerField(default=0)
    option_three_count = models.IntegerField(default=0)

    # Instance method. Returns the total number of vote counts
    def total(self): 
        return self.option_one_count + self.option_two_count + self.option_three_count

    def __str__(self):
        return (f"{self.question}")