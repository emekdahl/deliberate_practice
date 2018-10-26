"""
This is the journal module.
"""


import os


def load(name):
    """
    This method creates and loads a new journal.

    :param name: The base name of the journal to load.
    :return: A new journal structure populated with the file data.
    """
    data = []
    filename = get_full_pathname(name)

    if os.path.exists(filename):
        with open(filename) as file_input_stream:
            for entry in file_input_stream.readlines():
                data.append(entry.rstrip())

    return data

def save(name, journal_data):
    filename = get_full_pathname(name)
    print('.... saving to: {}'.format(filename))

    with open(filename, 'w') as file_output_stream:
        for entry in journal_data:
            file_output_stream.write(entry + '\n')


def get_full_pathname(name):
    filename = os.path.abspath(os.path.join('.', 'journals', name + '.jrl'))
    return filename


def add_entry(text, journal_data):
    journal_data.append(text)
