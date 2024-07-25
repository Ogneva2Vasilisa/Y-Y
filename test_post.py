from main import postt
from examples_json import *

def test_method_get1():
    li = postt(example_json)
    assert li[0] == 200, li[1]


def test_method_get2():
    li = postt(example_json_pet)
    assert li[0] == 200, li[1]


def test_method_get3():
    li = postt(bad_example_json_pet)
    assert li[0] != 200, li[1]
