def main():

    operation = True # allows the user to exit the translator ("loop") depending on whether they choose "y" or "n". 

    print("Welcome to the English to Chinese Translator!")

    # Stores English words as keys and Chinese translations as values.
    english_chinese_dict = {} 

    # Builds the translator dictionary from the text file before asking the user for sentences.
    with open("english_chinese_dict.txt", "r", encoding="utf-8") as file:

        for line_text in file:

            line_text = line_text.strip()

            # Removes a trailing comma so dictionary lines can be split cleanly.
            if line_text[-1] == ",":

                line_text = line_text[:-1]

            if ":" in line_text:
                key_line_text, value_line_text = line_text.split(":", 1)

                key = key_line_text.strip()

                value = value_line_text.strip()

                english_chinese_dict[key] = value

    # Keeps track of word frequency across all sentences entered during this run.
    total_word_frequency = {}

    while operation:

        eng_sentence = input("\nEnter an English sentence: ")

        # Keeps asking until the user enters text instead of only numbers.
        while eng_sentence.isdigit():

            print("Please input a sentence without numeric values!")

            eng_sentence = input("Enter an English sentence: ")

        translation = translate(eng_sentence, english_chinese_dict)

        print(f"\nTranslation: {translation}")

        current_freq = print_word_frequency(eng_sentence)

        # Adds this sentence's word counts into the running total.
        for word, count in current_freq.items():

            if word in total_word_frequency:

                total_word_frequency[word] += count
            else:
                total_word_frequency[word] = count

        print("\nWord Frequency:")

        for word, count in total_word_frequency.items():
            print(f"\n{word}: {count}")

        again = input("\nWould you like to translate another sentence? (y/n): ").lower()

        while again != "y" and again != "n":

            again = input("Would you like to translate another sentence? (y/n): ").lower()

        if again == "y":

            operation = True

        elif again == "n":

            print("\nThank You For Using My Translator!")

            operation = False


def translate(sentence, dictionary):

    words = sentence.lower().split()  # makes it lower to compensate for case insensitivity

    result = []  # translated words in sync order

    # Unknown words become question marks so the output keeps the same word order.
    for eng_word in words:
        if eng_word in dictionary:
            result.append(dictionary[eng_word])
        else:
            result.append("?")

    return " ".join(result)


def print_word_frequency(sentence):

    words = sentence.lower().split()

    word_frequency = {}

    # Counts each word in the current sentence before returning the dictionary.
    for word in words:

        if word in word_frequency:
            word_frequency[word] += 1
        else:
            word_frequency[word] = 1

    return word_frequency


main()
