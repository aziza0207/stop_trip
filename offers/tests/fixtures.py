import json

import pytest

from offers.models import Advertisement


@pytest.fixture
def jwt_token(api_client, django_user_model):
    email = 'user@gmail.com'
    password = 'password'

    django_user_model.objects.create_user(
        email=email,
        password=password
    )

    response = api_client.post(
        path='/api/auth/jwt/create/',
        data=json.dumps({'email': email, 'password': password}),
        content_type='application/json'
    )

    return response.data['access']


@pytest.fixture
def transport_advertisement():
    transport_advertisement = Advertisement.objects.create(
        category="transport", title="test", price=1, transport_type_of_service='sale', transport_type='ground',
        transport_category='moped', transport_brand=None, transport_model=None, transport_engine_type='fuel',
        transport_drive_type='rear_wheel', transport_engine_volume=5.2, transport_year_of_production=2023,
        transport_transmission_type='mechanic', transport_body_type='sedan', transport_condition='new',
        transport_passengers_quality=4,
    )

    return transport_advertisement


# @pytest.fixture
# def property_advertisement():
#     property_amenities1 = PropertyAmenity.objects.create(name='test1')
#     property_amenities2 = PropertyAmenity.objects.create(name='test2')
#
#     property_advertisement = Advertisement.objects.create(
#         subcategory="property", title="test", price=1, property_city="test", property_type_of_service='Продажа',
#         property_district='test', property_coords='test', property_building_max_floor=8, property_floor=3,
#         property_bathroom_count=1, property_bathroom_type='Совмещённый', property_area=20, property_living_area=10,
#         property_balcony='Есть', property_has_furniture=True, property_rooms_count=3, property_house_type='Панельный',
#         property_has_parking=False, property_rental_condition='Семье', property_prepayment='Месяц',
#         property_sleeping_places=3,
#     )
#     property_advertisement.property_amenities.set([property_amenities1, property_amenities2])
#
#     return property_advertisement
