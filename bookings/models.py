from django.db import models

### -----  Booking Class -----
""" 
This class represents a single reservation of a resource (e.g. a stage,
room, or piece of equipment) for a defined time window.

Two bookings for the same resource are considered conflicting if their
time ranges overlap — i.e. one booking starts before the other ends,
and vice versa. This model intentionally keeps `resource` as a plain
string for now; a full implementation would relate it to a separate
Resource model with its own attributes (capacity, location, etc).
 """

class Booking(models.Model):
    resource = models.CharField(max_length=100)
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()
    description = models.CharField(max_length=500, blank=True)

    def __str__(self):
        return f"{self.resource}, {self.description}, ({self.start_time} - {self.end_time})"