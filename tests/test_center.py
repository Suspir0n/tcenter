from tcenter.center import to_center

def test_to_center_happy_way():
    receive_valid_one = to_center('Olá Mundo', 20)
    receive_valid_two = to_center('Olá Mundo', '20')
    receive_valid_three = to_center('Olá Mundo', 20, '=')
    assert receive_valid_one
    assert receive_valid_two
    assert receive_valid_three


def test_to_center_happ_say():
    receive_invalid = to_center('Olá Mundo', 'a')
    assert receive_invalid


