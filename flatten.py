def flatten(input):
    """Flatten a list which may have nested elements

    Args:
      input: list or integer to flatten

    Returns: a flat list of all integers or lists in the input

    """
    output = []
    if isinstance(input, list):
        for element in input:
            output.extend(flatten(element))
    elif isinstance(input, int):
        output = [input]
    else:
        raise ValueError('Input value ' + str(input) + ' is not a list or integer')
        
    return output

