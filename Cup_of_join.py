def join(*lists: int, separator='-') -> list:
    """
    Get unlimited number of lists and combined them into one list, separated
    with the sep sign.
    :param lists: lists wanted to be combined
    :param separator: separator between the lists
    :return: the combined list
    """
    if not lists:
        return []
    joined_list = [str(list1) for list1 in lists]
    return list(separator.join(joined_list))


if __name__ == "__main__":
    print(join(1, 2, 3))
