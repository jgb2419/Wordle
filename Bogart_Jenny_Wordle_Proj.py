import re


def prob_letters_first(cleaned_words):
    first_letters = {}
    second_letters = {}
    third_letters = {}
    fourth_letters = {}
    fifth_letters = {}
    # finds the probability of each of the letters in each of the positions
    for word in cleaned_words:
        if word[1] in first_letters:
            first_letters[word[1]] += 1
        else:
            first_letters[word[1]] = 1
    for word in cleaned_words:
        if word[2] in second_letters:
            second_letters[word[2]] += 1
        else:
            second_letters[word[2]] = 1
    for word in cleaned_words:
        if word[3] in third_letters:
            third_letters[word[3]] += 1
        else:
            third_letters[word[3]] = 1
    for word in cleaned_words:
        if word[4] in fourth_letters:
            fourth_letters[word[4]] += 1
        else:
            fourth_letters[word[4]] = 1
    for word in cleaned_words:
        if word[5] in fifth_letters:
            fifth_letters[word[5]] += 1
        else:
            fifth_letters[word[5]] = 1
    total = sum(first_letters.values())
    first_probs = {}
    second_probs = {}
    third_probs = {}
    fourth_probs = {}
    fifth_probs = {}
    for key in first_letters.keys():
        first_probs[key] = first_letters[key] / total
    for key in second_letters.keys():
        second_probs[key] = second_letters[key] / total
    for key in third_letters.keys():
        third_probs[key] = third_letters[key] / total
    for key in fourth_letters.keys():
        fourth_probs[key] = fourth_letters[key] / total
    for key in fifth_letters.keys():
        fifth_probs[key] = fifth_letters[key] / total
    word_probs = {}
    for word in cleaned_words:
        prob_letter1 = 0
        prob_letter2 = 0
        prob_letter3 = 0
        prob_letter4 = 0
        prob_letter5 = 0
        for letter in range(1, len(word) - 1):
            if letter == 1:
                prob_letter1 = first_probs[word[letter]]
            if letter == 2:
                prob_letter2 = second_probs[word[letter]]
            if letter == 3:
                prob_letter3 = third_probs[word[letter]]
            if letter == 4:
                prob_letter4 = fourth_probs[word[letter]]
            if letter == 5:
                prob_letter5 = fifth_probs[word[letter]]
        # finds the probability of the word based on each letter in each position
        prob_word = prob_letter1 + prob_letter2 + prob_letter3 + prob_letter4 + prob_letter5
        word_probs[word] = prob_word
    return word_probs


# forms bigram and trigram dictionary
def create_bigram_trigram_dict(word_list):
    # opens the txt file and reads each line in as a word

    #with open('solutions.txt') as file:
        #word_list = file.readlines()
    cleaned_words = []

    # loops through each word and converts them all to lowercase and adds ^ at the beginning and $ at the end
    for word in word_list:
        word = word.lower()
        cleaned_words.append(re.sub(r"[^a-zA-Z0-9]", '', word))
    for index in range(len(cleaned_words)):
        cleaned_words[index] = '^' + cleaned_words[index] + '$'
    # elimates words with double letters
    possible_words = []
    for word in cleaned_words:
        good_word = True
        # letters = word.split(word)
        for letter in word:
            if word.count(letter) > 1:
                good_word = False
        if good_word == True:
            possible_words.append(word)
    # finds each bigram and adds them to a dictionary or adds them to a dictionary or adds to the value count
    bigram_dict = {}
    for bigram_word in cleaned_words:
        for letter in range(len(bigram_word) - 1):
            bigram = bigram_word[letter:letter + 2]
            if bigram in bigram_dict:
                bigram_dict[bigram] += 1
            else:
                bigram_dict[bigram] = 1
    # finds each trigram and adds them to a dictionary or adds them to a dictionary or adds to the value count
    trigram_dict = {}
    for trigram_word in cleaned_words:
        for letter in range(len(trigram_word) - 2):
            trigram = trigram_word[letter:letter + 3]
            if trigram in trigram_dict:
                trigram_dict[trigram] += 1
            else:
                trigram_dict[trigram] = 1
    return bigram_dict, trigram_dict, possible_words


# add all the probabilities of each bigram in a word and finds the total probability of the word by dividing by the
# total number of bigrams in the word
def total_prob(word, bigram_probs, trigram_probs, indivi_letter_probs):
    transitions = max(len(word) - 1, 1)
    prob = bigram_probs[word[:2]]
    for i in range(1, len(word) - 1):
        bigram = word[i:i + 2]
        if bigram[0] != '^' or bigram[-1] != '$':
            prob += bigram_probs[bigram]
    bigram_prob = prob / transitions

    # finds the probability of each word based on the trigram
    trigram_transitions = max(len(word) - 1, 1)
    prob_trigram = trigram_probs[word[:3]]
    for i in range(1, len(word) - 2):
        trigram = word[i:i + 3]
        if trigram[0] != '^' and trigram[-1] != '$':
            prob_trigram += trigram_probs[trigram]
    trigram_prob = prob_trigram / trigram_transitions
    letters_prob = indivi_letter_probs[word]
    return bigram_prob + trigram_prob + letters_prob


# prints the statistical values calculated
def print_stats(bigram_dict, trigram_dict, indiv_letter_probs, cleaned_words):
    # finds the total number of bigrams and finds their probabilities of each one
    total_bigrams = sum(bigram_dict.values())
    bigram_probs = {}
    for bigram in bigram_dict:
        bigram_probs[bigram] = bigram_dict[bigram] / total_bigrams

    total_trigrams = sum(trigram_dict.values())
    trigram_probs = {}
    for trigram in trigram_dict:
        trigram_probs[trigram] = trigram_dict[trigram] / total_trigrams

    # creates a dictionary of every word and their probability
    word_chances = [(word, total_prob(word, bigram_probs, trigram_probs, indiv_letter_probs)) for word in cleaned_words]

    # orders each probability and sorts them based on ascending and descending order
    highest_chance_words = sorted(word_chances, key=lambda x: x[1], reverse=True)
    # finds the words with unique values that have the highest probaility
    print("\n20 words with the highest chance:")
    print(highest_chance_words[:20])
    letters_used = []
    words_to_use = []
    for word, chance in highest_chance_words:
        good_word = True
        for letter in word:
            if letter in letters_used:
                good_word = False
        if good_word == True:
            for letter in range(1, len(word) - 1):
                letters_used.append(word[letter])
            print(word, chance)
    for word in highest_chance_words:
        if 's' not in word[0] and 'l' not in word[0] and 'a' not in word[0] and 't' not in word[0] and 'e' not in word[
            0]:
            words_to_use.append(word)
    print(words_to_use[:20])
    words_to_use2 = []
    for word in words_to_use:
        if 'b' not in word[0] and 'r' not in word[0] and 'i' not in word[0] and 'n' not in word[0] and 'y' not in word[
            0]:
            words_to_use2.append(word)
    print(words_to_use2[:20])


def main():
    with open('solutions.txt') as file:
        word_list = file.readlines()
    bigram_dict, trigram_dict, cleaned_words = create_bigram_trigram_dict(word_list)
    indiv_letter_probs = prob_letters_first(cleaned_words)
    print_stats(bigram_dict, trigram_dict, indiv_letter_probs, cleaned_words)


if __name__ == '__main__':
    main()
