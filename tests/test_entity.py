from datetime import datetime

from src.smartis_sdk.common import GroupBy, TypeReport
from src.smartis_sdk.entity import Attribution, AttributionModel, Payload

date_from = datetime.strptime("2023-01-01", "%Y-%m-%d")
date_to = datetime.strptime("2023-01-31", "%Y-%m-%d")
attr = Attribution(AttributionModel.LINEAR_WITH_POSTVIEW, 1, True)


def test_to_json_base() -> None:
    payload = Payload("test", ["test"], date_from, date_to, GroupBy.ADS, attr, TypeReport.AGGREGATED)
    expected = '{"project": "test", "metrics": "test", "datetimeFrom": "2023-01-01", "datetimeTo": "2023-01-31", ' \
               '"groupBy": "ad_id", "type": "aggregated", "attribution": {"model_id": 10, "period": 1, ' \
               '"with_direct": true}}'
    real = payload.to_json()
    assert real == expected
