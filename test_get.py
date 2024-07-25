from main import gett
from main import gett2_find


def test_method_get1():
    li = gett("findByStatus", 'pending')
    assert li[0] == 200, li[1]


def test_method_get2():
    li = gett("findByStatus", 'available')
    assert li[0] == 200, li[1]


def test_method_get3():
    li = gett("findByStatus", 'sold')
    assert li[0] == 200, li[1]


def test_method_get4():
    li = gett("findByStatus", 'sold', 'available')
    assert li[0] == 200, li[1]


# страница открывается,
# но она пустая, хотя по документации должна быть ошибка
def test_method_get5():
    li = gett("findByStatus", '2345')
    assert li[0] != 200, li[1]


def test_method_get6():
    li = gett2_find('user', 'string')
    assert li[0] == 200, li[1]


def test_method_get7():
    li = gett2_find('user', 'string1')
    assert li[0] != 200, li[1]


def test_method_get8():
    li = gett2_find('pet', '1')
    assert li[0] == 200, li[1]


def test_method_get9():
    li = gett2_find('pet', '9223372036854726638')
    assert li[0] == 200, li[1]


def test_method_get10():
    li = gett2_find('pet', '12aaaaabbb')
    assert li[0] != 200, li[1]


def test_method_get10():
    li = gett2_find('pet', '111111111111111111111111111111111111111111111111111111111111111111111111111111111111'
                                 '111111111111111111111111111111111111111111111111111111111111111')
    assert li[0] != 200, li[1]
