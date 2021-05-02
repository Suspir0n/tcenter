def to_center(text, space, object=str()):
    """
    This function is reponsible for centralizing the text. accepted at least two vestments.
    :param text: receive any text, only string.
    :param space: receive any value, only numbers.
    :param object: receive any object, ex: - . = ~ < > _ | between others.
    :return: The text centralized.
    """
    try:
        if object == '':
            receive = f'{text:^{space}}'
        else:
            receive = f'{text:{object}^{space}}'
    except ValueError as err:
        return f'information value invalid, {err}'
    except TypeError as err:
        return f'The type value invalid, {err}'
    else:
        return receive