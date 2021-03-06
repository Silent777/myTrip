"""Testing module for like views."""

import json

from django.test import TestCase
from django.urls import reverse

from checkpoint.models import Checkpoint
from comment.models import Comment
from like.models import Like
from photo.models import Photo
from registration.models import CustomUser
from trip.models import Trip

FAKE_ID = 999


def make_long_url(trip_id=10, checkpoint_id=20, photo_id=30, comment_id=40):
    """Create url without like id."""
    return '/api/v1/trip/{}/checkpoint/{}/photo/{}/comment/{}/like/'.\
        format(trip_id, checkpoint_id, photo_id, comment_id)


class ViewTest(TestCase):
    """Test for CRUD operation in like view."""

    def setUp(self):
        """
        Preconfiguration for test.
        Include instance of Client to class as attribute.
        Create a model of trip, checkpoint, photo, comment and like.
        """
        user = CustomUser.objects.create(
            id=1,
            first_name='name',
            last_name='surname',
            email='email.test@gmail.com',
            password='password'
        )
        user.is_active = True
        user.save()
        user.set_password('password')
        user.save()

        self.user = CustomUser.objects.create(
            id=2,
            first_name='second_name',
            last_name='second_surname',
            email='second.email.test@mail.com',
            password='password'
        )
        self.user.set_password('password')
        self.user.is_active = True
        self.user.save()

        self.client.login(username="email.test@gmail.com", password="password")

        trip = Trip.objects.create(
            id=10,
            user=user,
            title="trip_title",
            description="some_cool_trip",
            status=0
        )

        checkpoint = Checkpoint.objects.create(
            id=20,
            longitude=12,
            latitude=13,
            title="first_checkpoint",
            description="cool checkpoint",
            source_url="http://example.com",
            position_number=1,
            trip=trip
        )

        photo = Photo.objects.create(
            id=30,
            src='src1',
            user=user,
            trip=trip,
            checkpoint=checkpoint,
            description='photo_description'
        )

        comment = Comment.objects.create(
            id=40,
            message='test message',
            user=user,
            trip=trip,
            checkpoint=checkpoint,
            photo=photo
        )

        Like.objects.create(
            id=50,
            user=user,
            trip=trip,
            checkpoint=checkpoint,
            photo=photo,
            comment=comment
        )

        Like.objects.create(
            id=51,
            user=self.user,
            trip=trip,
            checkpoint=checkpoint,
            photo=photo,
            comment=comment
        )

    def test_get_all_likes_by_url_200(self):
        """
        Ensure that GET method returns status 200 with given Object<Trip> id,
        Object<Checkpoint> id, Object<Photo> id, Object<Comment> id.
        """

        response = self.client.get(make_long_url())
        self.assertEqual(response.status_code, 200)

    def test_get_all_likes_by_url_status_no_content_204(self):
        """Ensure that GET method returns status 204 when some wrong id was send."""

        response = self.client.get(make_long_url(FAKE_ID))
        self.assertEqual(response.status_code, 204)

    def test_get_number_of_likes_by_url(self):
        """Ensure that get method returns correct number of Like objects."""

        response = self.client.get(make_long_url())
        data = response.json()
        self.assertEqual(len(data), 3)

    def test_post_status_success_201(self):
        """Ensure that POST method creates new object with it relations and status 201."""

        response = self.client.post(make_long_url(FAKE_ID), json.dumps({}),
                                    content_type="application/json")
        self.assertEqual(response.status_code, 201)

    def test_post_delete_like_status_200(self):
        """Ensure that POST method returns status 200, when like deleted."""

        response = self.client.post(make_long_url(), json.dumps({}),
                                    content_type="application/json")
        self.assertEqual(response.status_code, 200)

    def test_post_by_not_logged_user_status_401(self):
        """Ensure that POST method returns status 401, if user not logged."""

        self.client.get(reverse('logout_view'))
        response = self.client.post(make_long_url(), json.dumps({}),
                                    content_type="application/json")
        self.assertEqual(response.status_code, 401)
