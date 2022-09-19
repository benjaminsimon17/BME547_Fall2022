import pytest

@pytest.mark.parametrize("HDL_input, expected",
                         [(85, "Normal"),
                          (45, "Borderline Low"),
                          (39, "Low")   
                         ])

def test_check_HDL(HDL_input, expected):
    from blood_calculator import check_HDL
    answer = check_HDL(HDL_input)
    assert answer == expected