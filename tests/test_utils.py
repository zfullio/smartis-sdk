from src.smartis_sdk.utils import clean_column_ids, ColumnType


def test_clean_column_ids():
    # Only integer ids
    assert clean_column_ids([1, 2, 3], ColumnType.CustomField).sort() == [1, 2, 3].sort()
    assert clean_column_ids([1, 2, 3], ColumnType.CustomFieldGroup).sort() == [1, 2, 3].sort()

    # Only  string ids with prefix
    assert clean_column_ids(["field_1", "field_2", "field_3"], ColumnType.CustomField).sort() == [1, 2, 3].sort()
    assert clean_column_ids(["field_cf_group_1", "field_cf_group_2", "field_cf_group_3"], ColumnType.CustomFieldGroup).sort() == [1, 2, 3].sort()

    # Only  string ids with 2 prefix
    assert clean_column_ids(["field_1_2", "field_2_3", "field_3_4"], ColumnType.CustomField).sort() == [1, 2, 3].sort()
    assert clean_column_ids(["field_cf_group_1", "field_cf_group_2", "field_cf_group_3"],
                            ColumnType.CustomFieldGroup).sort() == [1, 2, 3].sort()
    # Only  string ids with different prefix
    assert clean_column_ids(["field_cf_group_1", "field_2", "field_3", "field_cf_group_4"], ColumnType.CustomField).sort() == [2, 3].sort()
    assert clean_column_ids(["field_cf_group_1", "field_2", "field_3", "field_cf_group_4"], ColumnType.CustomFieldGroup).sort() == [1, 4].sort()
