import datetime
from functools import partial

from django.urls import reverse
from django.utils.timezone import now
from pytest import mark
from rest_framework import status
from rest_framework.test import APITestCase

from offers.constants import CategoryChoices
from offers.models import Advertisement
from users.tests.factories import UserFactory
from ..factories import EventAdvertisementFactory


@mark.django_db
class EventTest(APITestCase):
    def setUp(self):
        self.list_url: str = reverse("advertisements-list")
        self.detail_url = partial(reverse, "advertisements-detail")

    def test_create_event(self):
        payload = {
            "category": CategoryChoices.EVENT.value,
            "title": "event",
            "price": 12_000,
            "start_date": str(now() + datetime.timedelta(days=2)),
            "end_date": str(now() + datetime.timedelta(days=3)),
            "is_online": True,
        }
        self.assertEqual(Advertisement.objects.count(), 0)
        user = UserFactory()
        self.client.force_login(user)

        with self.assertNumQueries(3):
            res = self.client.post(self.list_url, data=payload)

        self.assertEqual(res.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Advertisement.objects.count(), 1)

        new_advertisement = Advertisement.objects.first()

        self.assertEqual(new_advertisement.owner, user)
        self.assertEqual(new_advertisement.category, payload["category"])
        self.assertEqual(new_advertisement.title, payload["title"])
        self.assertEqual(str(new_advertisement.start_date), payload["start_date"])
        self.assertEqual(str(new_advertisement.end_date), payload["end_date"])
        self.assertEqual(new_advertisement.is_online, payload["is_online"])

    def test_update_event(self):
        user = UserFactory()
        advertisement = EventAdvertisementFactory(owner=user)
        payload = {
            "category": CategoryChoices.EVENT.value,
            "title": "event_test",
            "price": 13_000,
            "start_date": str(now() + datetime.timedelta(days=2)),
            "end_date": str(now() + datetime.timedelta(days=3)),
            "is_online": True,
        }
        self.assertEqual(Advertisement.objects.count(), 1)

        self.client.force_login(user)
        with self.assertNumQueries(7):
            res = self.client.put(self.detail_url(kwargs={"pk": advertisement.id}), data=payload)

        self.assertEqual(res.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Advertisement.objects.count(), 1)
        advertisement.refresh_from_db()

        self.assertEqual(advertisement.owner, user)

    def test_delete_event(self):
        user = UserFactory()
        advertisement = EventAdvertisementFactory(owner=user)

        self.assertEqual(Advertisement.objects.count(), 1)
        self.client.force_login(user)

        with self.assertNumQueries(6):
            res = self.client.delete(self.detail_url(kwargs={"pk": advertisement.id}))

        self.assertEqual(res.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Advertisement.objects.count(), 0)

    def test_filter_event_start_date(self):
        user = UserFactory()
        start_date = "2023-11-06 00:00:00"
        end_date = "2023-11-07 00:00:00"
        events_set = [
            EventAdvertisementFactory(
                owner=user,
                category=CategoryChoices.EVENT.value,
                price=100_000 + _ * 50_000,
                start_date=start_date,
                end_date=end_date,
                is_online=True,
            )
            for _ in range(2)
        ]

        with self.assertNumQueries(2):
            res = self.client.get(
                self.list_url,
                {"start_date": str(start_date)},
            )

        self.assertEqual(res.status_code, status.HTTP_200_OK)
        res_json = res.json()
        self.assertEqual(len(res_json), len(events_set))

    def test_filter_event_end_date(self):
        user = UserFactory()
        start_date = "2023-11-06 00:00:00"
        end_date = "2023-11-07 00:00:00"
        events_set = [
            EventAdvertisementFactory(
                owner=user,
                category=CategoryChoices.EVENT.value,
                price=100_000 + _ * 50_000,
                start_date=start_date,
                end_date=end_date,
                is_online=True,
            )
            for _ in range(2)
        ]

        with self.assertNumQueries(2):
            res = self.client.get(
                self.list_url,
                {"end_date": str(end_date)},
            )

        self.assertEqual(res.status_code, status.HTTP_200_OK)
        res_json = res.json()
        self.assertEqual(len(res_json), len(events_set))

    def test_filter_event_is_online(self):
        user = UserFactory()
        # start_date = "2023-11-06 00:00:00"
        # end_date = "2023-11-07 00:00:00"
        events_set = [
            EventAdvertisementFactory(
                owner=user,
                category=CategoryChoices.EVENT.value,
                price=100_000 + _ * 50_000,
                # start_date=start_date,
                # end_date=end_date,
                is_online=[True, False][_ % 2],
                start_date="2023-12-5 00:00:00",
                end_date="2023-12-5 00:00:00",
            )
            for _ in range(2)
        ]

        with self.assertNumQueries(2):
            res = self.client.get(
                self.list_url,
                {"is_online": True},
            )

        self.assertEqual(res.status_code, status.HTTP_200_OK)
        res_json = res.json()
        self.assertEqual(len(res_json), len(events_set) // 2)
