from src.smartis_sdk.utils import clean_column_ids


def test_clean_column_ids():
    assert clean_column_ids([1, 2, 3], "field_").sort() == [1, 2, 3].sort()
    assert clean_column_ids(["field_1", "field_2", "field_3"], "field_").sort() == [1, 2, 3].sort()
    assert clean_column_ids(["field_1_2", "field_2_4", "field_3_6"], "field_").sort() == [1, 2, 3].sort()
    assert clean_column_ids(["field_1_2_11", "field_2_4_11", "field_3_6_11"], "field_").sort() == [1, 2, 3].sort()
    assert clean_column_ids(["cf_group_1_2_11", "field_2", "field_3"], "field_").sort() == [2, 3].sort()
