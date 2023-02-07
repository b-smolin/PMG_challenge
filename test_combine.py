from combine import getFileName, validateInput, ArgumentException, BadFilePathException
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


def test_good_args3():
    args = ["combine.py", "data/accessories.csv",
        "data/clothing.csv",
        "data/household_cleaners.csv",
        "data/smalltest.csv",
        "data/smallertest.csv"]
    args = validateInput(args)
    assert len(args) == 5 and args == ["data/accessories.csv",
        "data/clothing.csv",
        "data/household_cleaners.csv",
        "data/smalltest.csv",
        "data/smallertest.csv"]


def test_too_few_args():
    args = ["combine.py"]
    with pytest.raises(ArgumentException):
        validateInput(args)


def test_bad_filename():
    args = ["combine.py", "data/accessories.csv" , "data/doesntexist.csv",
        "data/smallertest.csv"]
    with pytest.raises(BadFilePathException):
        args = validateInput(args)


def test_wrong_filetype():
    args = ["combine.py", "data/notacsv.txt"]
    with pytest.raises(TypeError):
        validateInput(args)
