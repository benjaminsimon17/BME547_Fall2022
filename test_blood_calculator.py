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


@pytest.mark.parametrize("LDL_input, expected",
                         [(200, "Very High"),
                          (170, "High"),
                          (140, "Borderline High"),
                          (120, "Normal")   
                         ])

def test_check_LDL(LDL_input, expected):
    from blood_calculator import check_LDL
    answer = check_LDL(LDL_input)
    assert answer == expected

@pytest.mark.parametrize("chol_input, expected",
                         [(250, "High"),
                          (210, "Borderline High"),
                          (190, "Normal")
                         ])

def test_check_chol(chol_input, expected):
    from blood_calculator import check_chol
    answer = check_chol(chol_input)
    assert answer == expected