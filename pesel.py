def pesel2str(pesel: int) -> str:
    """Function returns pesel as a string, adding 0s at the beginning if needed"""
    ret = str(pesel)
    while len(ret) < 11:
        ret = "0" + ret
    return ret


def get_birthday_from_pesel(pesel: str) -> str:
    """Function returns what year you were born"""
    year = int(pesel[:2])
    month = int(pesel[2:4])

    if month > 20:
        year += 2000
    else:
        year += 1900

    return f"Rok urodzenia to {year}"


def get_gender_from_pesel(pesel: str) -> str:
    """Function returns gender"""
    number = int(pesel[9])
    if number % 2 == 1:
        return "Płeć studenta: Mężczyzna"
    else:
        return "Płeć studenta: Kobieta"


def validate_pesel(pesel: str) -> bool:
    """Function returns True if your PESEL is valid"""
    if len(pesel) != 11 or not pesel.isdigit():
        return False 

    digits = [int(i) for i in pesel]

    weights = [1, 3, 7, 9, 1, 3, 7, 9, 1, 3]

    checksum = sum(w * d for w, d in zip(weights, digits[:10]))
    checksum = (10 - (checksum % 10)) % 10

    return checksum == digits[-1]

