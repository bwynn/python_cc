def count_words(filename):
    try:
        with open(filename) as f_obj:
            content = f_obj.read()
    except OSError:
        msg = "Sorry, the file " + filename + " does not exist."
        print(msg)
    else:
        # Count the approximate number of words in the file
        words = contents.split()
        num_words = len(words)
        print("The file " + filename + " has about " + str(num_words) + " words.")

filename = 'alice.txt'
count_words(filename)
