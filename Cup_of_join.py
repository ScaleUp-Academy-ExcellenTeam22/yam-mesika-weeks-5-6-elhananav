def join(*lists, sep='-'):
    '''
    get unlimited number of lists and combined them into one list, seperated
    with the sep sign
    :param lists: lists wanted to be combined
    :param sep: separator between the lists
    :return: the combined list
    '''
    if not lists:
        return None
    joined_list = []
    for list1 in lists:
        joined_list += list1
        joined_list.append(sep)
    return joined_list[:-1]  # return without the last separator(not needed)

