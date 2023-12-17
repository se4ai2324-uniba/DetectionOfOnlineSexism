"""
Module: test_dataset_model_a
Description: This module contains functions for doing tests
on the task a dataset
Authors: Francesco Brescia
        Maria Elena Zaza
        Grazia Perna
"""
#pylint: disable=import-error
from pandas import read_csv
from great_expectations.dataset import PandasDataset

TRAINING_SOURCE_PATH = 'data/Raw/train_sexist.csv'
VALIDATION_SOURCE_PATH = 'data/Raw/dev_sexist.csv'
TESTING_SOURCE_PATH = 'data/Raw/test_sexist.csv'

tags = ["sexist", "not sexist"]

def test_training_set(dataset):
    """
    Module: test_training_set
    Description: This test checks expectations such as column order, 
    non-null values in the "label_sexist" column, unique values in the "ID" column,
    string type for "text" column, and adherence to a predefined set of values for "label_sexist"
    """
    train_dataset = PandasDataset(dataset)

    train_dataset.expect_table_columns_to_match_ordered_list(
        column_list=["ID", "text", "label_sexist"])
    train_dataset.expect_column_values_to_not_be_null(column="label_sexist")
    train_dataset.expect_column_values_to_be_unique(column="ID")
    train_dataset.expect_column_values_to_be_of_type(column="text", type_="str")
    train_dataset.expect_column_values_to_be_in_set(column="label_sexist", value_set=tags)
    expectation_suite = train_dataset.get_expectation_suite(discard_failed_expectations=False)
    print(train_dataset.validate(expectation_suite=expectation_suite, only_return_failures=True))


def test_validation_set(dataset):
    """
    Module: test_validation_set
    Description: This test checks expectations such as column order, 
    non-null values in the "label_sexist" column, unique values in the "ID" column,
    string type for "text" column, and adherence to a predefined set of values for "label_sexist"
    """

    validation_dataset = PandasDataset(dataset)

    validation_dataset.expect_table_columns_to_match_ordered_list(
        column_list=["ID", "text", "label_sexist"])
    validation_dataset.expect_column_values_to_not_be_null(column="label_sexist")
    validation_dataset.expect_column_values_to_be_unique(column="ID")
    validation_dataset.expect_column_values_to_be_of_type(column="text", type_="str")
    validation_dataset.expect_column_values_to_be_in_set(column="label_sexist", value_set=tags)
    expectation_suite = validation_dataset.get_expectation_suite(discard_failed_expectations=False)
    print(validation_dataset.validate(
        expectation_suite=expectation_suite, only_return_failures=True))

def test_test_set(dataset):
    """
    Module: test_test_set
    Description: This test checks expectations such as column order, 
    non-null values in the "label_sexist" column, unique values in the "ID" column,
    string type for "text" column, and adherence to a predefined set of values for "label_sexist"
    """

    test_dataset = PandasDataset(dataset)

    test_dataset.expect_table_columns_to_match_ordered_list(
        column_list=["ID", "text", "label_sexist"])
    test_dataset.expect_column_values_to_not_be_null(column="label_sexist")
    test_dataset.expect_column_values_to_be_unique(column="ID")
    test_dataset.expect_column_values_to_be_of_type(column="text", type_="str")
    test_dataset.expect_column_values_to_be_in_set(column="label_sexist", value_set=tags)
    expectation_suite = test_dataset.get_expectation_suite(discard_failed_expectations=False)
    print(test_dataset.validate(expectation_suite=expectation_suite, only_return_failures=True))

if __name__ == "__main__":
    train = read_csv(TRAINING_SOURCE_PATH)
    validation = read_csv(VALIDATION_SOURCE_PATH)
    test = read_csv(TESTING_SOURCE_PATH)

    test_training_set(train)
    test_validation_set(validation)
    test_test_set(test)
