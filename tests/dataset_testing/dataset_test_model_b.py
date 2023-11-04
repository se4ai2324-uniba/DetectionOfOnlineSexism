from pandas import read_csv
from great_expectations.dataset import PandasDataset

TRAINING_SOURCE_PATH = '../../data/Raw/train_category.csv'
VALIDATION_SOURCE_PATH = '../../data/Raw/dev_category.csv'
TESTING_SOURCE_PATH = '../../data/Raw/test_category.csv'

train = read_csv(TRAINING_SOURCE_PATH)
validation = read_csv(VALIDATION_SOURCE_PATH)
test = read_csv(TESTING_SOURCE_PATH)

train_dataset = PandasDataset(train)
validation_dataset = PandasDataset(validation)
test_dataset = PandasDataset(test)
tags = ["1. threats, plans to harm and incitement", "2. derogation", "3. animosity", "4. prejudiced discussions"]

# Definisci le aspettative
train_dataset.expect_table_columns_to_match_ordered_list(column_list=["ID", "text", "label_category"])
train_dataset.expect_column_values_to_not_be_null(column="label_category")
train_dataset.expect_column_values_to_be_unique(column="ID")
train_dataset.expect_column_values_to_be_of_type(column="text", type_="str")
train_dataset.expect_column_values_to_be_in_set(column="label_category", value_set=tags)
expectation_suite = train_dataset.get_expectation_suite(discard_failed_expectations=False)
print(train_dataset.validate(expectation_suite=expectation_suite, only_return_failures=True))

# Definisci le aspettative
validation_dataset.expect_table_columns_to_match_ordered_list(column_list=["ID", "text", "label_category"])
validation_dataset.expect_column_values_to_not_be_null(column="label_category")
validation_dataset.expect_column_values_to_be_unique(column="ID")
validation_dataset.expect_column_values_to_be_of_type(column="text", type_="str")
validation_dataset.expect_column_values_to_be_in_set(column="label_category", value_set=tags)
expectation_suite = validation_dataset.get_expectation_suite(discard_failed_expectations=False)
print(validation_dataset.validate(expectation_suite=expectation_suite, only_return_failures=True))

# Definisci le aspettative
test_dataset.expect_table_columns_to_match_ordered_list(column_list=["ID", "text", "label_category"])
test_dataset.expect_column_values_to_not_be_null(column="label_category")
test_dataset.expect_column_values_to_be_unique(column="ID")
test_dataset.expect_column_values_to_be_of_type(column="text", type_="str")
test_dataset.expect_column_values_to_be_in_set(column="label_category", value_set=tags)
expectation_suite = test_dataset.get_expectation_suite(discard_failed_expectations=False)
print(test_dataset.validate(expectation_suite=expectation_suite, only_return_failures=True))
