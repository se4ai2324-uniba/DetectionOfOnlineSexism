"""
Module: test_dataset_model_a
Description: This module contains functions for doing tests
on the task a dataset
Authors: Francesco Brescia
        Maria Elena Zaza
        Grazia Perna
"""
#pylint: disable=import-error
import os
from pandas import read_csv
from great_expectations.dataset import PandasDataset
import pytest

file_dir = os.path.dirname(__file__)

TRAINING_SOURCE_PATH = os.path.join(file_dir, '..//../data/Raw/train_sexist.csv')
VALIDATION_SOURCE_PATH = os.path.join(file_dir, '..//../data/Raw/dev_sexist.csv')
TESTING_SOURCE_PATH = os.path.join(file_dir, '..//../data/Raw/test_sexist.csv')

tags = ["sexist", "not sexist"]

def test_training_set(setup_training):
    """
    Module: test_training_set
    Description: This test checks expectations such as column order, 
    non-null values in the "label_sexist" column, unique values in the "ID" column,
    string type for "text" column, and adherence to a predefined set of values for "label_sexist"
    """
    train_dataset = PandasDataset(setup_training)

    train_dataset.expect_table_columns_to_match_ordered_list(
        column_list=["ID", "text", "label_sexist"])
    train_dataset.expect_column_values_to_not_be_null(column="label_sexist")
    train_dataset.expect_column_values_to_be_unique(column="ID")
    train_dataset.expect_column_values_to_be_of_type(column="text", type_="str")
    train_dataset.expect_column_values_to_be_in_set(column="label_sexist", value_set=tags)
    expectation_suite = train_dataset.get_expectation_suite(discard_failed_expectations=False)
    print(train_dataset.validate(expectation_suite=expectation_suite, only_return_failures=True))


def test_validation_set(setup_validation):
    """
    Module: test_validation_set
    Description: This test checks expectations such as column order, 
    non-null values in the "label_sexist" column, unique values in the "ID" column,
    string type for "text" column, and adherence to a predefined set of values for "label_sexist"
    """

    validation_dataset = PandasDataset(setup_validation)

    validation_dataset.expect_table_columns_to_match_ordered_list(
        column_list=["ID", "text", "label_sexist"])
    validation_dataset.expect_column_values_to_not_be_null(column="label_sexist")
    validation_dataset.expect_column_values_to_be_unique(column="ID")
    validation_dataset.expect_column_values_to_be_of_type(column="text", type_="str")
    validation_dataset.expect_column_values_to_be_in_set(column="label_sexist", value_set=tags)
    expectation_suite = validation_dataset.get_expectation_suite(discard_failed_expectations=False)
    print(validation_dataset.validate(
        expectation_suite=expectation_suite, only_return_failures=True))

def test_test_set(setup_test):
    """
    Module: test_test_set
    Description: This test checks expectations such as column order, 
    non-null values in the "label_sexist" column, unique values in the "ID" column,
    string type for "text" column, and adherence to a predefined set of values for "label_sexist"
    """

    test_dataset = PandasDataset(setup_test)

    test_dataset.expect_table_columns_to_match_ordered_list(
        column_list=["ID", "text", "label_sexist"])
    test_dataset.expect_column_values_to_not_be_null(column="label_sexist")
    test_dataset.expect_column_values_to_be_unique(column="ID")
    test_dataset.expect_column_values_to_be_of_type(column="text", type_="str")
    test_dataset.expect_column_values_to_be_in_set(column="label_sexist", value_set=tags)
    expectation_suite = test_dataset.get_expectation_suite(discard_failed_expectations=False)
    print(test_dataset.validate(expectation_suite=expectation_suite, only_return_failures=True))

@pytest.fixture
def setup_training():
    """
    Module: setup_dataset
    Description: This function sets up training
    dataset by reading a CSV file.
    """

    dataset = read_csv(TRAINING_SOURCE_PATH)

    return dataset

@pytest.fixture
def setup_validation():
    """
    Module: setup_dataset
    Description: This function sets up validation
    dataset by reading a CSV file.
    """

    dataset = read_csv(VALIDATION_SOURCE_PATH)

    return dataset


@pytest.fixture
def setup_test():
    """
    Module: setup_dataset
    Description: This function sets up test
    dataset by reading a CSV file.
    """

    dataset = read_csv(TESTING_SOURCE_PATH)

    return dataset

if __name__ == "__main__":

    pytest.main()
