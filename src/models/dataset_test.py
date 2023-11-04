from pandas import read_csv
from great_expectations.dataset import PandasDataset

TRAINING_SOURCE_PATH = '../../data/Raw/train_sexist.csv'
VALIDATION_SOURCE_PATH = '../../data/Raw/dev_sexist.csv'
TESTING_SOURCE_PATH = '../../data/Raw/test_sexist.csv'

train = read_csv(TRAINING_SOURCE_PATH)
validation = read_csv(VALIDATION_SOURCE_PATH)
test = read_csv(TESTING_SOURCE_PATH)

train_dataset = PandasDataset(train)
validation_dataset = PandasDataset(validation)
test_dataset = PandasDataset(test)

# Definisci le aspettative
train_dataset.expect_table_columns_to_match_ordered_list(column_list=["ID", "text", "label_sexist"])
train_dataset.expect_column_values_to_not_be_null(column="label_sexist")
train_dataset.expect_column_values_to_be_unique(column="ID")
train_dataset.expect_column_values_to_be_of_type(column="text", type_="str" )

tags = ["sexist", "not sexist"]
train_dataset.expect_column_values_to_be_in_set(column="label_sexist", value_set=tags)

expectation_suite = train_dataset.get_expectation_suite(discard_failed_expectations=False)
print(train_dataset.validate(expectation_suite=expectation_suite, only_return_failures=True))
