def conv_num(num_str):
    '''
        Convert a string representation of an integer, float,
        or hexidecimal value to a numeric value.

        Args:
            num_str (str) String representation.

        Returns:
            int | float: the integer or float representation of the string.
    '''

    if not isinstance(num_str, str) or len(num_str) == 0:
        return None

    res = 0

    cur_index = 0
    is_decimal = False
    is_negative = False
    to_add = 0

    for c in num_str:

        invalid_negative = cur_index != 0 and c == "-"
        curX = c == "x" or c == "X"
        invalid_negative_X = is_negative and cur_index != 2 and curX
        invalid_postive_x = not is_negative and cur_index != 1 and curX

        if invalid_negative or invalid_negative_X or invalid_postive_x:
            return None

        elif c == "x" or c == "X":
            to_add = process_hex(num_str[cur_index + 1:])
            break

        elif c == ".":
            is_decimal = True
            to_add = process_decimal(num_str[cur_index + 1:])
            break

        elif c == "-":
            is_negative = True

        elif c in "0123456789":
            res = res * 10 + char_to_num(c)
        else:
            return None

        cur_index += 1

    if to_add is None:
        return None

    return process_final_result(is_negative=is_negative, is_decimal=is_decimal,
                                res=res+to_add)


def process_final_result(is_negative, is_decimal, res):
    '''
        Adds a decimal to the end of the number
        or makes number negative if needed.

        Args:
            is_negative (boolean): is the final result negative.
            is_decimal (boolean): is the final result a float.
            res (int): The value to process.

        Returns:
            int | float: the final result representation.
    '''
    if is_decimal:
        res = res + (0 * 10 ** -1)

    if is_negative:
        return res * -1
    else:
        return res


def process_hex(num_str):
    '''
        Converts a hexidecimal string to a
        decimal value.

        Args:
            num_str (str): the string representation of the value.

        Returns:
            int | None: the integer representation, or None if invalid.

    '''

    hex_digits = "0123456789ABCDEF"

    power = 0

    res = 0

    for c in reversed(num_str.upper()):
        if c not in hex_digits:
            return None
        res += hex_digits.index(c) * (16 ** power)
        power += 1

    return res


def process_decimal(num_str):
    '''
        Helper function to process the
        decimal portion of the string.

        Args:
            num_str (str): the string representation

        Returns:
            int | None: the integer representation, or None if invalid.
    '''

    power = 0
    res = 0

    for c in num_str:
        if c in "0123456789":
            res = res * 10 + char_to_num(c)
            power += 1

        else:
            return None

    return round(res * (10 ** (-1 * power)), power)


def char_to_num(c):
    '''
        Formula to convert a character to an integer value.

        Args:
            c (char): a character represenation of a digit.

        Returns:
            int: the integer representation of the character.
    '''
    return ord(c) - ord('0')


def my_datetime(num_sec):
    """
    Takes a time in seconds and determines the date corresponding to that
    time since the epoch.

    Args:
        num_sec (int: the number of seconds since epoch.

    Returns:
        str: The corresponding date in 'MM-DD-YYYY' format.
    """
    final_date = [1, 1, 1970]
    month_days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

    days_remaining = int(conv_num_to_days(num_sec))

    while days_remaining:
        if is_leap_year(final_date[2]):
            if days_remaining > 365:
                days_remaining -= 366
                final_date[2] += 1
            else:
                break
        else:
            if days_remaining >= 365:
                days_remaining -= 365
                final_date[2] += 1
            else:
                break

    if is_leap_year(final_date[2]):
        month_days[1] += 1

    cur_month = 0
    while days_remaining >= month_days[cur_month]:
        days_remaining -= month_days[cur_month]
        cur_month += 1
        final_date[0] += 1

    final_date[1] += days_remaining

    for i in range(0, 2):
        if len(str(final_date[i])) == 1:
            final_date[i] = f'0{final_date[i]}'

    return f'{final_date[0]}-{final_date[1]}-{final_date[2]}'


def conv_num_to_days(num_sec):
    """
    Converts seconds to days.

    Args:
        num_sec (int): Seconds that will be converted to days

    Returns:
        int: The conversion of num_sec to days
    """
    conv_factor = 24 * 60 * 60
    return num_sec // conv_factor


def is_leap_year(year):
    """
    Determines whether a given year is a leap year.

    Args:
        year (int): The year to check.

    Returns:
        bool: True if the year is a leap year, False otherwise.
    """
    if year % 4 == 0 and (year % 100 != 0 or year % 400 == 0):
        return True
    return False


def conv_endian(num, endian='big'):
    """
    Return the integer in hex in endian order.

    This function takes a negative or positive number
    and currently returns the value in hex format in
    big or little endian order.

    Args:
        num (str): Integer number.
        endian (str): Order of hex value.

    Returns:
        str: Hex value in endian order, or None if
        endian is not "big" or "little"
    """
    if not isinstance(num, int):
        return None

    if endian not in ["big", "little"]:
        return None

    hex_digits = "0123456789ABCDEF"
    hex_number = ""
    i = 0
    negative = False

    if num == 0:
        return "00"

    if num < 0:
        negative = True
        num = abs(num)

    while num > 0:
        hex_digit = hex_digits[num % 16]

        if i % 2 == 0 and i != 0:
            hex_number = hex_digit + " " + hex_number

        else:
            hex_number = hex_digit + hex_number
        num = num // 16
        i += 1

    if i % 2 != 0:
        hex_number = "0" + hex_number

    if endian == "little":
        hex_number = " ".join(hex_number.split()[::-1])

    if negative:
        hex_number = "-" + hex_number

    return hex_number
