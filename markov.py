from random import choice


def open_and_read_file(file_path):
    """Takes file path as string; returns text as string.

    Takes a string that is a file path, opens the file, and turns
    the file's contents as one string of text.
    """

    # Chain open() to create file object, then read() to create string.
    contents = open(file_path).read()

    return contents


def make_chains(text_string):
    """Takes input text as string; returns _dictionary_ of markov chains.

    A chain will be a key that consists of a tuple of (word1, word2)
    and the value would be a list of the word(s) that follow those two
    words in the input text.

    For example:

        >>> make_chains("hi there mary hi there juanita")
        {('hi', 'there'): ['mary', 'juanita'], ('there', 'mary'): ['hi'], ('mary', 'hi': ['there']}
    """

    chains = {}

    # Split text_string on whitespace, creating list of words.
    words = text_string.split()

    # Iterate over indices. Use a range of 2 less than number of words (i.e.,
    # len(list)) so that our final key-value pair is made from the last three
    # words.

    for i in range(len(words)-2):

        # Make a tuple to use as a key.
        bigram = ( words[i], words[i+1] )

        # Check whether the key we just made exists in chains. If not,
        # add it, and set its value to [].
        chains[bigram] = chains.get(bigram, [])

        # Update the key's value to be the word that follows this occurance of
        # the key. ".append" works in place; don't need to use "=".

        chains[bigram].append(words[i+2])

    return chains


def make_text(chains):
    """Takes dictionary of markov chains; returns random text."""

    text = ""

    # Choose a random key to start with.
    key = choice(chains.keys())

    # Add words from first key to text string.
    text = text + key[0] + ' ' + key[1]

    # Set state variable for loop
    writing = True

    # Write the poem
    while writing:

        # Randomly choose next word from key's value list
        next_word = choice(chains[key])

        # Add next word to text string
        text = text + ' ' + next_word

        # Create next key
        key = ( key[1], next_word )

        # Check whether created key exists in passed dictionary.
        # If it doesn't, stop writing.
        if not key in chains:
            break

    return text


input_path = "green-eggs.txt"

# Open the file and turn it into one long string
input_text = open_and_read_file(input_path)

# Get a Markov chain
chains = make_chains(input_text)

# Produce random text
random_text = make_text(chains)

print random_text
