def flatten(input, output=None):
    """Flatten a list which may have nested elements using tail recursion, just for fun, even though python doesn't support it

    Args:
      input: list or integer to flatten

    Returns: a flat list of all integers or lists in the input

    """
    output = output or []

    if isinstance(input, int):
        output.append(input)
        return output

    if isinstance(input, list):
        # collect any and all "plain" integers from the beginning of the list and add them to output
        is_element_a_list = False
        while len(input) > 0:
            element = input.pop(0)
            if isinstance(element, int):
                output.append(element)
            else:
                is_element_a_list = True # we'll still verify later, this just handles "last element was list" problem
                break

        if not is_element_a_list and len(input) == 0:
            # we've reached the end of our recursion
            return output

        # Since element wasn't an integer, it had better be a list.
        if not isinstance(element, list):
            raise ValueError('Input value ' + str(element) + ' is not a list or integer')

        # element is now the first non-integer from input, and input contains all elements after element (exclusive of element).
        # By extending element with input, we have flattened element in the greater context.
        element.extend(input)
        return flatten(element, output) 

