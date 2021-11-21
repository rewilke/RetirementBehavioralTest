Feature: Retirement Age Testing
  As a human,
  I want to find my retirement age,
  So I can plan ahead for my future.

  Scenario Outline: Calculating a retirement age for someone born on a given year
    Given a birth year of <birth_year> is entered
    When the retirement age is calculated
    Then the retirement year is <retirement_year> and the retirement month is <retirement_month>

    Examples: Birth Years and Retirement Ages
      | birth_year | retirement_year | retirement_month |
      | 1900       | 65              | 0                |
      | 1937       | 65              | 0                |
      | 1938       | 65              | 2                |
      | 1939       | 65              | 4                |
      | 1940       | 65              | 6                |
      | 1941       | 65              | 8                |
      | 1942       | 65              | 10               |
      | 1943       | 66              | 0                |
      | 1954       | 66              | 0                |
      | 1955       | 66              | 2                |
      | 1956       | 66              | 4                |
      | 1957       | 66              | 6                |
      | 1958       | 66              | 8                |
      | 1959       | 66              | 10               |
      | 1960       | 67              | 0                |
      | 2021       | 67              | 0                |

  Scenario: Calculating a retirement age for someone born before 1900
    Given a birth year of 1899 is entered
    When the retirement age is calculated
    Then a ValueError is thrown

  Scenario: Calculating a retirement age for someone born after 2021
    Given a birth year of 2022 is entered
    When the retirement age is calculated
    Then a ValueError is thrown
