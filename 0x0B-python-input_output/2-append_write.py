'''Module provides function `append_write`.
'''


def append_write(filename='', text=''):
    '''Appends text `text` add the end of file `filename`.

    Args:
        filename (str): The file name
        text (str): The text to append.
    '''
    with open(filename, 'a', encoding='utf-8') as f:
        return f.write(text)
