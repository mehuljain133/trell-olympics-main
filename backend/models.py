from django.db import models

# Create your models here.


class Country(models.Model):
    country_name = models.CharField(max_length=50)
    country_cheers = models.IntegerField(default=0)

    def __str__(self):
        return f'{self.country_name} <cheers={self.country_cheers}>'


class Event(models.Model):
    event_name = models.CharField(max_length=50)
    event_sport = models.CharField(max_length=50)
    event_date = models.DateField()

    def __str__(self):
        return f'{self.event_name} <sport={self.event_sport}, event_date={self.event_date}>'


class Medal(models.Model):
    medal_type = models.CharField(max_length=8, default='')
    country = models.ForeignKey(Country, on_delete=models.CASCADE)
    event = models.ForeignKey(Event, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.country} <event={self.event}, date={self.medal_type}>'


class Participant(models.Model):
    country = models.ForeignKey(Country, on_delete=models.CASCADE)
    event = models.ForeignKey(Event, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.country} <event={self.event}>'
