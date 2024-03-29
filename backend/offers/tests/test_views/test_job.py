from functools import partial

from django.urls import reverse
from pytest import mark
from rest_framework import status
from rest_framework.test import APITestCase

from offers.constants import (
    CategoryChoices,
    JobType,
    JobDurationType,
    JobPaymentType,
)
from offers.models import Advertisement
from users.tests.factories import UserFactory
from ..factories import JobAdvertisementFactory


@mark.django_db
class JobTest(APITestCase):
    def setUp(self):
        self.list_url: str = reverse("advertisements-list")
        self.detail_url = partial(reverse, "advertisements-detail")

    def test_create_job(self):
        payload = {
            "category": CategoryChoices.JOB.value,
            "job_type": JobType.PART_TIME.value,
            "title": "job",
            "price": 10_000,
            "job_duration": JobDurationType.TEMPORARY,
            "job_payment_type": JobPaymentType.MONTHLY_PAYMENT.value,
            "job_experience": True,
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
        self.assertEqual(new_advertisement.job_type, payload["job_type"])
        self.assertEqual(new_advertisement.job_duration, payload["job_duration"])
        self.assertEqual(new_advertisement.job_experience, payload["job_experience"])

    def test_update_job(self):
        user = UserFactory()
        advertisement = JobAdvertisementFactory(owner=user)
        payload = {
            "category": CategoryChoices.JOB.value,
            "title": "job",
            "price": 10_000,
            "job_type": JobType.PART_TIME,
            "job_duration": JobDurationType.TEMPORARY.value,
            "job_payment_type": JobPaymentType.DAILY_PAYMENT.value,
            "job_experience": True,
        }
        self.assertEqual(Advertisement.objects.count(), 1)

        self.client.force_login(user)
        with self.assertNumQueries(7):
            res = self.client.put(self.detail_url(kwargs={"pk": advertisement.id}), data=payload)

        self.assertEqual(res.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Advertisement.objects.count(), 1)
        advertisement.refresh_from_db()

        self.assertEqual(advertisement.owner, user)
        self.assertEqual(advertisement.category, payload["category"])
        self.assertEqual(advertisement.title, payload["title"])
        self.assertEqual(advertisement.price, payload["price"])
        self.assertEqual(advertisement.job_type, payload["job_type"])
        self.assertEqual(advertisement.job_duration, payload["job_duration"])
        self.assertEqual(advertisement.job_payment_type, payload["job_payment_type"])
        self.assertEqual(advertisement.job_experience, payload["job_experience"])

    def test_delete_job(self):
        user = UserFactory()
        advertisement = JobAdvertisementFactory(owner=user)

        self.assertEqual(Advertisement.objects.count(), 1)
        self.client.force_login(user)

        with self.assertNumQueries(6):
            res = self.client.delete(self.detail_url(kwargs={"pk": advertisement.id}))

        self.assertEqual(res.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Advertisement.objects.count(), 0)

    def test_filter_job_type(self):
        user = UserFactory()
        job_set = [
            JobAdvertisementFactory(
                owner=user,
                category=CategoryChoices.TRANSPORT.value,
                price=100_000 + _ * 50_000,
                job_type=[JobType.FULL_TIME, JobType.PART_TIME][_ % 2],
                job_duration=JobDurationType.ONE_TIME_TASK,
                job_payment_type=JobPaymentType.HOURLY_PAYMENT,
                job_experience=True,
            )
            for _ in range(2)
        ]
        with self.assertNumQueries(2):
            res = self.client.get(
                self.list_url,
                {"job_type": JobType.FULL_TIME.value},
            )

        self.assertEqual(res.status_code, status.HTTP_200_OK)
        res_json = res.json()
        self.assertEqual(len(res_json), len(job_set) // 2)

    def test_filter_job_duration(self):
        user = UserFactory()
        job_set = [
            JobAdvertisementFactory(
                owner=user,
                category=CategoryChoices.TRANSPORT.value,
                price=100_000 + _ * 50_000,
                job_type=JobType.FULL_TIME,
                job_duration=[JobDurationType.ONE_TIME_TASK, JobDurationType.TEMPORARY][_ % 2],
                job_payment_type=JobPaymentType.HOURLY_PAYMENT,
                job_experience=True,
            )
            for _ in range(2)
        ]
        with self.assertNumQueries(2):
            res = self.client.get(
                self.list_url,
                {"job_duration": JobDurationType.TEMPORARY.value},
            )

        self.assertEqual(res.status_code, status.HTTP_200_OK)
        res_json = res.json()
        self.assertEqual(len(res_json), len(job_set) // 2)

    def test_filer_job_payment_type(self):
        user = UserFactory()
        job_set = [
            JobAdvertisementFactory(
                owner=user,
                category=CategoryChoices.TRANSPORT.value,
                price=100_000 + _ * 50_000,
                job_type=JobType.FULL_TIME,
                job_duration=JobDurationType.ONE_TIME_TASK,
                job_payment_type=[JobPaymentType.HOURLY_PAYMENT, JobPaymentType.WEEKLY_PAYMENT][
                    _ % 2
                ],
                job_experience=True,
            )
            for _ in range(2)
        ]
        with self.assertNumQueries(2):
            res = self.client.get(
                self.list_url,
                {"job_payment_type": JobPaymentType.WEEKLY_PAYMENT.value},
            )

        self.assertEqual(res.status_code, status.HTTP_200_OK)
        res_json = res.json()
        self.assertEqual(len(res_json), len(job_set) // 2)

    def test_filter_job_experience(self):
        user = UserFactory()
        job_set = [
            JobAdvertisementFactory(
                owner=user,
                category=CategoryChoices.TRANSPORT.value,
                price=100_000 + _ * 50_000,
                job_type=JobType.FULL_TIME,
                job_duration=JobDurationType.ONE_TIME_TASK,
                job_payment_type=JobPaymentType.HOURLY_PAYMENT,
                job_experience=[True, False][_ % 2],
            )
            for _ in range(2)
        ]
        with self.assertNumQueries(2):
            res = self.client.get(
                self.list_url,
                {"job_experience": True},
            )

        self.assertEqual(res.status_code, status.HTTP_200_OK)
        res_json = res.json()
        self.assertEqual(len(res_json), len(job_set) // 2)
