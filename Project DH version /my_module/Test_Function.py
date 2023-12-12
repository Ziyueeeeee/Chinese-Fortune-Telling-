"""
Testing for my functions and modules.
"""

import pytest
import my_module.Analyze_Element as ae
import my_module.Analyze_Fate as af
import my_module.Analyze_Zodiac as az
import my_module.Get_Natal_Chart as gnc

# Define fixtures
@pytest.fixture
def birth_data():
    return [2005, 9, 28, 3]

@pytest.fixture
def sex_data():
    return "Male"

@pytest.fixture
def pillar_data():
    return [['乙', '酉'], ['乙', '酉'], ['丁', '未'], ['癸', '卯']]

def test_gnc(birth_data):
    """
    Test the functions in the 'gnc' module for generating Chinese Heavenly Stems and Earthly Branches columns.

    This test function checks the output of four functions in the 'gnc' module, each generating a specific
    column based on the given birth information.

    Parameters:
    None

    Returns:
    None

    Raises:
    AssertionError: If any of the assertions fail.
    """
    assert gnc.combine_natal_chart(birth_data) == [['乙', '酉'], ['乙', '酉'], ['丁', '未'], ['壬', '寅']]
     

def test_ae(pillar_data):
    """
    Test the ElementAna class in the 'ae' module for generating element statistics.

    This test function checks if the ElementAna class can correctly generate element statistics
    based on the provided 'pillar' input.

    Parameters:
    pillar (list): A list representing a pillar in Chinese metaphysics, typically containing
                   information about Heavenly Stems and Earthly Branches.

    Returns:
    None

    Raises:
    AssertionError: If any of the assertions fail.
    """

    ae_object = ae.ElementAna(pillar_data)
    ae_object.obtain_element()
    assert type(ae_object.element_stat) == list
    assert len(ae_object.element_stat) == 5

def test_af(birth_data, sex_data):
    """
    Test the Fate class in the 'af' module for generating age and combined cycle information.

    This test function checks if the Fate class can correctly generate age and combined cycle information
    based on the provided 'birth' and 'sex' inputs.

    Parameters:
    birth (list): A list representing the birth information, typically containing year, month, day, and hour.
    sex (str): A string representing the gender of the individual ('M' for male, 'F' for female).

    Returns:
    None

    Raises:
    AssertionError: If any of the assertions fail.
    """
    af_object = af.Fate(birth_data, sex_data)
    af_object.get_age()
    af_object.get_combined_cycle()
    assert type(af_object.age) == list
    assert len(af_object.age) == 9

def test_af2():
    """
    Test the Fate class in the 'af' module for generating age and combined cycle information.

    This test function checks if the Fate class can correctly generate age and combined cycle information
    for a specific birth date and gender.

    Parameters:
    None

    Returns:
    None

    Raises:
    AssertionError: If any of the assertions fail.
    """
    af_object = af.Fate([2005, 9, 28, 5], "Male")
    af_object.get_age()
    af_object.get_combined_cycle()
    assert af_object.age == [3, 13, 23, 33, 43, 53, 63, 73, 83]
    assert af_object.combined_cycle == [[3, '甲申'], [13, '癸未'], [23, '壬午'], [33, '辛巳'], [43, '庚辰'], [53, '己卯'], [63, '戊寅'], [73, '丁丑'], [83, '丙子']]

def test_az(pillar_data):
    """
    Test the ZodiacAna class in the 'az' module for obtaining zodiac animal and zodiac comment.

    This test function checks if the ZodiacAna class can correctly obtain the zodiac animal
    and zodiac comment based on the provided input.

    Parameters:
    None

    Returns:
    None

    Raises:
    AssertionError: If any of the assertions fail.
    """
    az_object = az.ZodiacAna(pillar_data)
    az_object.obtain_zodiac_animal()
    az_object.obtain_zodiac_comment()
    assert az_object.zodiac == 'Rooster'
    assert type(az_object.zodiac_comment) == str