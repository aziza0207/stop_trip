from django_filters.rest_framework import filters, FilterSet

from ..constants import (
    PropertyTypeOfService,
    PropertyBathroomType,
    PropertyHouseType,
    PropertyRentalCondition,
)


class PropertyFilter(FilterSet):
    property_type_of_service = filters.ChoiceFilter(
        label="Тип услуги", choices=PropertyTypeOfService.choices
    )
    property_city = filters.CharFilter(label="Город", field_name="property_city__slug")
    property_district = filters.CharFilter(label="Район", field_name="property_district__slug")
    property_bathroom_count = filters.NumberFilter(label="Количество санузлов")
    property_bathroom_type = filters.ChoiceFilter(
        label="Тип санузла", choices=PropertyBathroomType.choices
    )
    property_house_type = filters.ChoiceFilter(label="Тип дома", choices=PropertyHouseType.choices)
    property_sleeping_places = filters.NumberFilter(label="Количество спальных мест")
    property_rooms_count = filters.NumberFilter(label="Количество комнат")
    property_rental_condition = filters.ChoiceFilter(
        label="Условия аренды", choices=PropertyRentalCondition.choices
    )
    property_area = filters.RangeFilter(label="Общая площадь")
    property_has_furniture = filters.BooleanFilter(label="Мебель")
    property_amenities = filters.CharFilter(label="Удобства", field_name="property_amenities__name")
