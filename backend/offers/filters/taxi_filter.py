from django_filters.rest_framework import filters, FilterSet

from ..constants import TaxiType, TaxiUnit


class TaxiFilter(FilterSet):
    """Фильтры такси."""

    taxi_unit = filters.ChoiceFilter(label="Единица измерения", choices=TaxiUnit.choices)
    taxi_type = filters.ChoiceFilter(label="Вид такси", choices=TaxiType.choices)

    @classmethod
    def _taxi_filter_specs(cls, queryset) -> list[dict]:
        specs: list[dict] = []

        # Единица измерения
        taxi_unit_specs = {
            "name": "taxi_unit",
            "choices": [{"value": value, "label": label} for value, label in TaxiUnit.choices],
        }
        specs.append(taxi_unit_specs)

        # Вид такси
        taxi_type_specs = {
            "name": "taxi_type",
            "choices": [{"value": value, "label": label} for value, label in TaxiType.choices],
        }
        specs.append(taxi_type_specs)

        return specs
