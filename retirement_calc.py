def retirementAgeCalculate(birthYear, birthMonth):
    if birthYear < 1900:
        raise ValueError(f'Birth year "{birthYear}" must be no earlier than 1900')
    elif birthYear > 2021:
        raise ValueError(f'Birth year "{birthYear}" must be earlier than 2021')

    retirementAgeYear  = 65
    retirementAgeMonth = 0

    if   birthYear == 1938: retirementAgeMonth = 2
    elif birthYear == 1939: retirementAgeMonth = 4
    elif birthYear == 1940: retirementAgeMonth = 6
    elif birthYear == 1941: retirementAgeMonth = 8
    elif birthYear == 1942: retirementAgeMonth = 10

    elif birthYear >= 1943:
        retirementAgeYear += 1

        if   birthYear == 1955: retirementAgeMonth = 2
        elif birthYear == 1956: retirementAgeMonth = 4
        elif birthYear == 1957: retirementAgeMonth = 6
        elif birthYear == 1958: retirementAgeMonth = 8
        elif birthYear == 1959: retirementAgeMonth = 10

        elif birthYear >= 1960:
            retirementAgeYear += 1

    retirementMonth  = birthMonth + retirementAgeMonth
    retirementYear   = birthYear  + retirementAgeYear + (retirementMonth // 12)
    retirementMonth %= 12

    return [retirementAgeYear, retirementAgeMonth, retirementYear, retirementMonth]
