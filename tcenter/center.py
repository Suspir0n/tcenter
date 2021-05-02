def to_center(title, space, object=str()):
    """
    This function is reponsible for centralizing the title. accepted at least two vestments.
    :param title: receive any title, only string.
    :param space: receive any value, only numbers.
    :param object: receive any object, ex: - . = ~ < > _ | between others.
    :return: The text centralized.
    """
    try:
        if object == '':
            receive = f'{title:^{space}}'
        else:
            receive = f'{title:{object}^{space}}'
    except ValueError as err:
        return f'information value invalid, {err}'
    except TypeError as err:
        return f'The type value invalid, {err}'
    else:
        return receive