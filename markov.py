from random import choice


def open_and_read_file(file_path):
    """Takes file path as string; returns text as string.

    Takes a string that is a file path, opens the file, and turns
    the file's contents as one string of text.
    """

    # Chains open() to create file object, then read() to create string.
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

    #Iterate over indices. Use a range of 1 less than number of words
    #because len(list) gives 1 more than maximum index of list.
    for i in range(len(words)-1):

        #Make a tuple to use as a key.
        bigram = ( words[i], words[i+1] )

        #Check whether the key we just made exists in chains. If not,
        #add it, and set its value to [].
        chains[bigram] = chains.get(bigram, [])

        #Test whether we can access a word two indices after current word.
        #If we can, bind that word to a new variable and append it to the
        #current key's value.
        try:
            new_word = words[i+2]
            chains[bigram].append(new_word)

        #If we can't access that index, leave the loop. 
        except IndexError:
            break

    return chains


def make_text(chains):
    """Takes dictionary of markov chains; returns random text."""

    text = ""

    # your code goes here

    return text


input_path = "green-eggs.txt"

# Open the file and turn it into one long string
input_text = open_and_read_file(input_path)

# Get a Markov chain
chains = make_chains(input_text)

# Produce random text
# random_text = make_text(chains)

# print random_text
