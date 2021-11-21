from pytest_bdd import scenarios, given, when, then, parsers
from retirement_calc import retirementAgeCalculate

scenarios('retirement.feature')

@given(parsers.parse('a birth year of {birth_year:d} is entered'), target_fixture="age")
def birth_year_entered(birth_year):
    assert isinstance(birth_year, int)
    return dict(birth=(birth_year, 0))

@when('the retirement age is calculated')
def retirement_age_calculated(age):
    birth_age = age["birth"]
    try:
        age["retirement"] = retirementAgeCalculate(birth_age[0], birth_age[1])
    except ValueError:
        age["retirement"] = None

@then(parsers.parse('the retirement year is {retirement_year:d} and the retirement month is {retirement_month:d}'))
def retirement_age_verify(age, retirement_year, retirement_month):
    retirement_age = age["retirement"]
    assert retirement_age[0] == retirement_year and retirement_age[1] == retirement_month

@then('a ValueError is thrown')
def retirement_age_error(age):
    assert age["retirement"] is None
