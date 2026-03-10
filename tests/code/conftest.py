import pytest

from madewithml.data import CustomPreprocessor


@pytest.fixture
def dataset_loc():
    return "https://raw.githubusercontent.com/Shubhamharanale7/Made-With-ML/main/datasets/dataset.csv"


@pytest.fixture
def preprocessor():
    return CustomPreprocessor()
