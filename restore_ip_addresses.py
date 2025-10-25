#
# https://leetcode.com/problems/restore-ip-addresses/description/
#
# USAGE:
#       python restore_ip_addresses.py 12340
#
import argparse

#
# GLOBALS
#
NUM_OCTETS = 4
OCTET_LENGTHS = [1, 2, 3]
PERIOD = "."
RUNTIME_TYPE_CHECK = False


#
# TYPE HINTS
#
Indexes = list[int]


#
# FUNCTIONS
#
def main():
    # get the arg
    ip_digits = get_first_arg()

    # get the list of its valid ips
    valid_ips = get_valid_ips(ip_digits)

    # print them out
    for ip in valid_ips:
        print(ip)


def get_valid_ips(ip_digits: str) -> list[str]:
    """Prints the valid permutations"""
    ip_digits_len = len(ip_digits)

    # gets a list of all possible indexes for the periods
    list_of_indexes = get_possible_period_indexes(ip_digits_len)

    # check each list of indexes. If it results in a valid IP, return it
    ret = []
    for indexes in list_of_indexes:
        ip_address = make_ip_address(ip_digits, indexes)
        if is_valid_ip(ip_address):
            ret.append(ip_address)

    return ret


def make_ip_address(digits: str, indexes: Indexes) -> str:
    """Inserts periods into the indexes of the digits string"""
    i = indexes[0]
    j = indexes[1]
    k = indexes[2]

    ret = digits

    ret = insert_char(ret, PERIOD, i + j + k)
    ret = insert_char(ret, PERIOD, i + j)
    ret = insert_char(ret, PERIOD, i)

    return ret


def get_possible_period_indexes(ip_digits_len: int) -> list[Indexes]:
    """Returns a list of all possible places to put three periods"""
    ret = []

    for i in OCTET_LENGTHS:
        for j in OCTET_LENGTHS:
            for k in OCTET_LENGTHS:
                # if its too long, skip it
                if i + j + k >= ip_digits_len:
                    continue

                ret.append([i, j, k])

    return ret


def insert_char(string: str, char: str, index: int) -> str:
    """Inserts a character at the specified index"""
    return string[:index] + char + string[index:]


def is_valid_ip(string: str) -> bool:
    """Returns True if its passed a valid IP. False otherwise"""

    if RUNTIME_TYPE_CHECK:
        if not isinstance(string, str):
            return False

    octets = string.split(PERIOD)
    if len(octets) != NUM_OCTETS:
        return False

    for octet in octets:
        if not is_valid_octet(octet):
            return False

    return True


def is_valid_octet(string: str) -> bool:
    """Returns true if this is a valid octet number"""

    # "01" is not valid
    if len(string) > 1 and string[0] == "0":
        return False

    try:
        number = int(string)
        return number >= 0 and number <= 255

    except ValueError:
        return False


def get_first_arg() -> str:
    """Returns the first command-line arg"""
    parser = argparse.ArgumentParser()
    parser.add_argument("first_arg", type=str, help="The first positional argument")
    args = parser.parse_args()
    return args.first_arg


if __name__ == "__main__":
    main()
