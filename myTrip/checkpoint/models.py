"""This module contains checkpoint model class and basic functions"""

from django.db import models
from django.core.exceptions import ObjectDoesNotExist

from trip.models import Trip


class Checkpoint(models.Model):
    """
    Checkpoint
    :argument longitude: float - 1-st position coordinate
    :argument latitude: float - 2-nd position coordinate
    :argument title: char - checkpoint's title
    :argument description: text - description of checkpoint
    :argument position_number: int - ordinal number of checkpoint
    :argument source_url: url - url of the checkpoint's source
    :argument trip: Object<Trip>: - foreign key to Trip model
    """

    longitude = models.FloatField()
    latitude = models.FloatField()
    title = models.CharField(max_length=70)
    description = models.TextField()
    position_number = models.IntegerField()
    source_url = models.URLField(blank=True)
    trip = models.ForeignKey(Trip, on_delete=models.CASCADE)
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True, editable=True)

    def to_dict(self):
        """
        Convert model object to dictionary.
        Return:
            dict:
                {
                    "longitude": longitude,
                    "latitude": latitude,
                    "title": title,
                    "description": description,
                    "source_url": source_url,
                    "position_number": position_number,
                    "trip_id": id of trip object
                }
        """
        return {"id": self.id,
                "longitude": self.longitude,
                "latitude": self.latitude,
                "title": self.title,
                "description": self.description,
                "source_url": self.source_url,
                "position_number": self.position_number,
                "trip_id": self.trip.id}

    @staticmethod
    def get_by_id(checkpoint_id):
        """
        Returns checkpoint by given checkpoint id.
        Args:
            checkpoint_id (int): id - primary key
        Returns:
            Object<Checkpoint>: Object of Checkpoint.
        """
        try:
            checkpoint = Checkpoint.objects.get(id=checkpoint_id)
        except ObjectDoesNotExist:
            checkpoint = None
        return checkpoint

    @staticmethod
    def get_by_trip_id(trip_id):
        """
        Returns checkpoints by given trip id.
        Args:
            trip_id (int): foreign key to Trip model
        Returns:
            <QuerySet [<Checkpoint: Checkpoint object>, ...>]>: QuerySet of Checkpoints.
        """
        try:
            trip = Trip.objects.get(id=trip_id)
        except ObjectDoesNotExist:
            return None
        checkpoints = trip.checkpoint_set.all().order_by('create_at')
        return checkpoints

    @staticmethod
    def create(longitude, latitude, title, description, source_url, position_number, trip):
        """
        Create checkpoint with given trip_id, longitude,latitude,title,description,source_url,
        position_number,trip.
        Args:
            longitude (float):  1-st position coordinate.
            latitude (float): 2-nd position coordinate.
            title (char): checkpoint's title.
            description (text): description of checkpoint.
            position_number (int):  ordinal number of checkpoint.
            source_url (url):  url of the checkpoint's source.
            trip (Object<Trip>):  foreign key to Trip model.
        Returns:
            Object<Checkpoint>: Object of Checkpoint.
        """

        checkpoint = Checkpoint()
        checkpoint.longitude = longitude
        checkpoint.latitude = latitude
        checkpoint.title = title
        checkpoint.description = description
        checkpoint.source_url = source_url
        checkpoint.position_number = position_number
        checkpoint.trip = trip
        checkpoint.save()
        return checkpoint

    def update(self,
               longitude=None,
               latitude=None,
               title=None,
               description=None,
               position_number=None):
        """
        Updates checkpoint with given parameters.
        Args:
            longitude (float):  1-st position coordinate.
            latitude (float): 2-nd position coordinate.
            title (str): checkpoint's title.
            description (str): description of checkpoint.
            position_number (int):  ordinal number of checkpoint.
        Returns:
            Object<Checkpoint>: Object of Checkpoint if updating was successful and None if wasn't
        """

        if longitude:
            self.longitude = longitude
        if latitude:
            self.latitude = latitude
        if title:
            self.title = title
        if description:
            self.description = description
        if position_number:
            self.position_number = position_number
        self.save()

    @staticmethod
    def delete_by_id(checkpoint_id):
        """
        Deletes checkpoint.
        Args:
            self - checkpoint object
        Returns:
            True if deleting was successful
            False if deleting wasn't complete
        """

        try:
            checkpoint = Checkpoint.objects.get(id=checkpoint_id)
        except ObjectDoesNotExist:
            return False
        checkpoint.delete()
        return True
    