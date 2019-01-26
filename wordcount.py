# put your code here.

def count_words(filename):
    word_counts = {}

    file = open(filename)

    for line in file:
        line = line.rstrip()
        line_words = line.split(" ")

        for word in line_words:
            word_counts[word] = word_counts.get(word, 0) + 1



    file.close()

    return word_counts

print(count_words("twain.txt"))