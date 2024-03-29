from functools import partial

from django.urls import reverse
from pytest import mark
from rest_framework import status
from rest_framework.test import APITestCase

from offers.constants import (
    CategoryChoices,
    TransportCondition,
    TransportBodyType,
    TransportTransmissionType,
    TransportDriveType,
    TransportEngineType,
    TransportCategory,
    TransportType,
    TransportTypeOfService,
    TaxiUnit,
    TaxiType,
    PropertyRentalCondition,
    PropertyHouseType,
    PropertyBathroomType,
    PropertyTypeOfService,
    JobType,
    JobDurationType,
    JobPaymentType,
)
from users.tests.factories import UserFactory
from ..factories import BaseAdvertisementFactory


@mark.django_db
class AdvertisementViewSetTest(APITestCase):
    def setUp(self):
        self.list_url: str = reverse("advertisements-list")
        self.detail_url = partial(reverse, "advertisements-detail")
        self.get_filter_params_url: str = reverse("advertisements-get-filter-params")

    def test_list(self):
        user = UserFactory()
        advertisements = [
            BaseAdvertisementFactory(owner=user, category=category)
            for category in CategoryChoices.values
        ]

        with self.assertNumQueries(2):
            res = self.client.get(self.list_url)

        self.assertEqual(res.status_code, status.HTTP_200_OK)
        res_json = res.json()
        self.assertEqual(len(res_json), len(advertisements))

    def test_detail(self):
        user = UserFactory()
        advertisements = [
            BaseAdvertisementFactory(owner=user, category=category)
            for category in CategoryChoices.values
        ]

        with self.assertNumQueries(3):
            res = self.client.get(self.detail_url(kwargs={"pk": advertisements[0].id}))

        self.assertEqual(res.status_code, status.HTTP_200_OK)
        res_json = res.json()
        self.assertEqual(res_json["id"], advertisements[0].id)

    def test_filter_category(self):
        user = UserFactory()
        advertisements = [
            BaseAdvertisementFactory(owner=user, category=category)
            for category in CategoryChoices.values
        ]

        with self.assertNumQueries(2):
            res = self.client.get(
                self.list_url,
                {"category": CategoryChoices.TRANSPORT},
            )

        self.assertEqual(res.status_code, status.HTTP_200_OK)
        res_json = res.json()
        self.assertEqual(len(res_json), len(advertisements) // len(CategoryChoices.values))

    def test_filter_price(self):
        user = UserFactory()
        advertisements = [
            BaseAdvertisementFactory(owner=user, price=_)
            for _ in [i * 100_000 for i in range(1, 10)]
        ]

        with self.assertNumQueries(2):
            res = self.client.get(
                self.list_url,
                {"price_min": advertisements[1].price, "price_max": advertisements[-2].price},
            )

        self.assertEqual(res.status_code, status.HTTP_200_OK)
        res_json = res.json()
        self.assertEqual(len(res_json), len(advertisements) - 2)

    def test_filter_order_date_create(self):
        user = UserFactory()
        advertisements = [BaseAdvertisementFactory(owner=user) for _ in range(3)]

        with self.assertNumQueries(2):
            res = self.client.get(
                self.list_url,
                {"order": "-date_create"},
            )

        self.assertEqual(res.status_code, status.HTTP_200_OK)
        res_json = res.json()
        self.assertEqual(len(res_json), len(advertisements))
        self.assertEqual(res_json[0]["id"], advertisements[-1].id)
        self.assertEqual(res_json[-1]["id"], advertisements[0].id)

    def test_get_filter_params(self):
        with self.assertNumQueries(1):
            res = self.client.get(self.list_url)

        self.assertEqual(res.status_code, status.HTTP_200_OK)
        res_json = res.json()

        for spec in res_json:
            if spec["name"] == "category":
                self.assertEqual(len(spec["choices"]), len(CategoryChoices.choices))
            elif spec["name"] == "price":
                self.assertTrue(len(spec["range"]))
            elif spec["name"] == "is_online":
                self.assertEqual(len(spec["choices"]), len([True, False]))
            elif spec["name"] == "job_type":
                self.assertEqual(len(spec["choices"]), len(JobType.choices))
            elif spec["name"] == "job_duration":
                self.assertEqual(len(spec["choices"]), len(JobDurationType.choices))
            elif spec["name"] == "job_payment_type":
                self.assertEqual(len(spec["choices"]), len(JobPaymentType.choices))
            elif spec["name"] == "job_experience":
                self.assertEqual(len(spec["choices"]), len([True, False]))
            elif spec["name"] == "property_type_of_service":
                self.assertEqual(len(spec["choices"]), len(PropertyTypeOfService.choices))
            elif spec["name"] == "property_city":
                self.assertEqual(len(spec["choices"]), 0)
            elif spec["name"] == "property_district":
                self.assertEqual(len(spec["choices"]), 0)
            elif spec["name"] == "property_bathroom_count":
                self.assertEqual(len(spec["choices"]), 0)
            elif spec["name"] == "property_bathroom_type":
                self.assertEqual(len(spec["choices"]), len(PropertyBathroomType.choices))
            elif spec["name"] == "property_house_type":
                self.assertEqual(len(spec["choices"]), len(PropertyHouseType.choices))
            elif spec["name"] == "property_sleeping_places":
                self.assertTrue(len(spec["range"]))
            elif spec["name"] == "property_rooms_count":
                self.assertTrue(len(spec["range"]))
            elif spec["name"] == "property_rental_condition":
                self.assertEqual(len(spec["choices"]), len(PropertyRentalCondition.choices))
            elif spec["name"] == "property_area":
                self.assertTrue(len(spec["range"]))
            elif spec["name"] == "property_has_furniture":
                self.assertEqual(len(spec["choices"]), len([True, False]))
            elif spec["name"] == "property_amenities":
                self.assertEqual(len(spec["choices"]), 0)
            elif spec["name"] == "service_home_visit":
                self.assertEqual(len(spec["choices"]), len([True, False]))
            elif spec["name"] == "taxi_unit":
                self.assertEqual(len(spec["choices"]), len(TaxiUnit.choices))
            elif spec["name"] == "taxi_type":
                self.assertEqual(len(spec["choices"]), len(TaxiType.choices))
            elif spec["name"] == "transport_type_of_service":
                self.assertEqual(len(spec["choices"]), len(TransportTypeOfService.choices))
            elif spec["name"] == "transport_type":
                self.assertEqual(len(spec["choices"]), len(TransportType.choices))
            elif spec["name"] == "transport_category":
                self.assertEqual(len(spec["choices"]), len(TransportCategory.choices))
            elif spec["name"] == "transport_brand":
                self.assertEqual(len(spec["choices"]), 0)
            elif spec["name"] == "transport_model":
                self.assertEqual(len(spec["choices"]), 0)
            elif spec["name"] == "transport_engine_type":
                self.assertEqual(len(spec["choices"]), len(TransportEngineType.choices))
            elif spec["name"] == "transport_drive_type":
                self.assertEqual(len(spec["choices"]), len(TransportDriveType.choices))
            elif spec["name"] == "transport_engine_volume":
                self.assertTrue(len(spec["range"]))
            elif spec["name"] == "transport_year_of_production":
                self.assertTrue(len(spec["range"]))
            elif spec["name"] == "transport_transmission_type":
                self.assertEqual(len(spec["choices"]), len(TransportTransmissionType.choices))
            elif spec["name"] == "transport_body_type":
                self.assertEqual(len(spec["choices"]), len(TransportBodyType.choices))
            elif spec["name"] == "transport_condition":
                self.assertEqual(len(spec["choices"]), len(TransportCondition.choices))
            elif spec["name"] == "transport_commission":
                self.assertTrue(len(spec["range"]))
            else:
                assert False, f"Add test for spec['name'] = '{spec['name']}'"
