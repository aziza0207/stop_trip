from django.db.models import Min, Max
from django_filters.rest_framework import filters, FilterSet
from common.filters import CharInFilter

from ..constants import (
    TransportTypeOfService,
    TransportType,
    TransportCategory,
    TransportEngineType,
    TransportDriveType,
    TransportTransmissionType,
    TransportBodyType,
    TransportCondition,
)


class TransportFilter(FilterSet):
    """Фильтры транспорта."""

    transport_type_of_service = filters.ChoiceFilter(
        label="Тип услуги", choices=TransportTypeOfService.choices
    )
    transport_type = filters.ChoiceFilter(label="Тип транспорта", choices=TransportType.choices)
    transport_category = filters.ChoiceFilter(
        label="Категория транспорта", choices=TransportCategory.choices
    )
    transport_brand = filters.CharFilter(
        label="Марка транспорта", field_name="transport_brand__slug"
    )
    transport_model = CharInFilter(label="Модель транспорта", field_name="transport_model__slug")
    transport_engine_type = filters.ChoiceFilter(
        label="Тип двигателя", choices=TransportEngineType.choices
    )
    transport_drive_type = filters.ChoiceFilter(
        label="Вид привода", choices=TransportDriveType.choices
    )
    transport_engine_volume = filters.RangeFilter(label="Объём двигателя")
    transport_year_of_production = filters.RangeFilter(label="Год производства")
    transport_transmission_type = filters.ChoiceFilter(
        label="Тип коробки передач", choices=TransportTransmissionType.choices
    )
    transport_body_type = filters.ChoiceFilter(
        label="Тип кузова", choices=TransportBodyType.choices
    )
    transport_condition = filters.ChoiceFilter(
        label="Состояние транспорта", choices=TransportCondition.choices
    )
    transport_commission = filters.RangeFilter(label="Комиссия")

    @classmethod
    def _transport_filter_specs(cls, queryset) -> list[dict]:
        specs: list[dict] = []

        # Тип услуги
        transport_type_of_service_specs = {
            "name": "transport_type_of_service",
            "choices": [
                {"value": value, "label": label} for value, label in TransportTypeOfService.choices
            ],
        }
        specs.append(transport_type_of_service_specs)

        # Тип транспорта
        transport_type_specs = {
            "name": "transport_type",
            "choices": [{"value": value, "label": label} for value, label in TransportType.choices],
        }
        specs.append(transport_type_specs)

        # Категория транспорта
        transport_category_specs = {
            "name": "transport_category",
            "choices": [
                {"value": value, "label": label} for value, label in TransportCategory.choices
            ],
        }
        specs.append(transport_category_specs)

        # Марка транспорта
        transport_brand_specs = {
            "name": "transport_brand",
            "choices": [
                {"value": value, "label": label}
                for value, label in queryset.values_list(
                    "transport_brand__slug", "transport_brand__name"
                )
                .order_by("transport_brand__slug")
                .distinct("transport_brand__slug")
            ],
        }
        specs.append(transport_brand_specs)

        # Модель транспорта
        transport_model_specs = {
            "name": "transport_model",
            "choices": [
                {"value": value, "label": label}
                for value, label in queryset.values_list(
                    "transport_model__slug", "transport_model__name"
                )
                .order_by("transport_model__slug")
                .distinct("transport_model__slug")
            ],
        }
        specs.append(transport_model_specs)

        # Тип двигателя
        transport_engine_type_specs = {
            "name": "transport_engine_type",
            "choices": [
                {"value": value, "label": label} for value, label in TransportEngineType.choices
            ],
        }
        specs.append(transport_engine_type_specs)

        # Вид привода
        transport_drive_type_specs = {
            "name": "transport_drive_type",
            "choices": [
                {"value": value, "label": label} for value, label in TransportDriveType.choices
            ],
        }
        specs.append(transport_drive_type_specs)

        # Объём двигателя
        transport_engine_volume_range = queryset.aggregate(
            min=Min("transport_engine_volume"), max=Max("transport_engine_volume")
        )
        transport_engine_volume_specs = {
            "name": "transport_engine_volume",
            "range": {
                "min": transport_engine_volume_range["min"],
                "max": transport_engine_volume_range["max"],
            },
        }
        specs.append(transport_engine_volume_specs)

        # Год производства
        transport_year_of_production_range = queryset.aggregate(
            min=Min("transport_year_of_production"), max=Max("transport_year_of_production")
        )
        transport_year_of_production_specs = {
            "name": "transport_year_of_production",
            "range": {
                "min": transport_year_of_production_range["min"],
                "max": transport_year_of_production_range["max"],
            },
        }
        specs.append(transport_year_of_production_specs)

        # Тип коробки передач
        transport_transmission_type_specs = {
            "name": "transport_transmission_type",
            "choices": [
                {"value": value, "label": label}
                for value, label in TransportTransmissionType.choices
            ],
        }
        specs.append(transport_transmission_type_specs)

        # Тип кузова
        transport_body_type_specs = {
            "name": "transport_body_type",
            "choices": [
                {"value": value, "label": label} for value, label in TransportBodyType.choices
            ],
        }
        specs.append(transport_body_type_specs)

        # Состояние транспорта
        transport_condition_specs = {
            "name": "transport_condition",
            "choices": [
                {"value": value, "label": label} for value, label in TransportCondition.choices
            ],
        }
        specs.append(transport_condition_specs)

        # Комиссия
        transport_commission_range = queryset.aggregate(
            min=Min("transport_commission"), max=Max("transport_commission")
        )
        transport_commission_specs = {
            "name": "transport_commission",
            "range": {
                "min": transport_commission_range["min"],
                "max": transport_commission_range["max"],
            },
        }
        specs.append(transport_commission_specs)

        return specs
