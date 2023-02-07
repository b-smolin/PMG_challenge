from combine import getFileName, validateInput, ArgumentException
import pytest


def test_name_stripping1():
    name = "\\data\\household_cleaners.csv"
    assert getFileName(name) == "household_cleaners.csv"


def test_name_stripping2():
    name = "\\data\\clothing.csv"
    assert getFileName(name) == "clothing.csv"


def test_name_stripping3():
    name = "\\data\\files\\items\\contents\\IMPORTANTDATA.csv"
    assert getFileName(name) == "IMPORTANTDATA.csv"


def test_name_stripping_unix():
    name = "data/files/items/contents/stuff.csv"
    assert getFileName(name) == "stuff.csv"


def test_good_args1():
    args = ["combine.py", "data/accessories.csv"]
    args = validateInput(args)
    assert len(args) == 1 and args == ["data/accessories.csv"]


def test_good_args2():
    args = ["combine.py", "data/accessories.csv",
            "data/clothing.csv",
            "data/household_cleaners.csv"]
    args = validateInput(args)
    assert len(args) == 3 and args == ["data/accessories.csv",
                                       "data/clothing.csv",
                                       "data/household_cleaners.csv"]


def test_too_few_args():
    args = ["combine.py"]
    with pytest.raises(ArgumentException):
        validateInput(args)
