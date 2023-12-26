# imports Part 1 of the Wordle assignment
import Bogart_Jenny_Wordle_Starting_Word.py as wordle
import re

"""
Creates a list of possible words based on what resuls Wordle returns and then finds the most probable word based on this
list
@:param cleaned_word: List of possible words based on what word was guessed and the previously guessed words
@:param word: the word that was guessed
@:return: returns the most probable word and the 
"""
def chose_word(cleaned_words, word):
    # creates a list of letters that occur multiple times in one word
    double_letters = re.findall(r'(\w)\w*\1', word)
    print(double_letters)
    # calls new_words function to create a new list of possible words based on the output from Wordle
    new_word_list = new_words(cleaned_words, word, 1, double_letters, 0)
    # creates a dictionary of bigrams and trigrams and the number of times they occur in the list of words
    bigram_dict, trigram_dict, cleaned_words = wordle.create_bigram_trigram_dict(new_word_list)
    # calculates the probability of an individual letter occurring
    indiv_letter_probs = wordle.prob_letters_first(new_word_list)
    # finds the total number of bigrams
    total_bigrams = sum(bigram_dict.values())
    # finds the probability of each bigram and stores in a dictionary
    bigram_probs = {}
    for bigram in bigram_dict:
        bigram_probs[bigram] = bigram_dict[bigram] / total_bigrams
    # finds the total number of trigrams
    total_trigrams = sum(trigram_dict.values())
    trigram_probs = {}
    # finds the probability of each trigram and stores in a dictionary
    for trigram in trigram_dict:
        trigram_probs[trigram] = trigram_dict[trigram] / total_trigrams
    # calculates the chance of eaCh word by taking into consideration the probability of bigrams, the probability of
    # trigrams, and the probability of each individual letter
    word_chances = [(word, wordle.total_prob(word, bigram_probs, trigram_probs, indiv_letter_probs)) for word in
                    new_word_list]
    # sorts the list by ascending probability
    highest_chance_words = sorted(word_chances, key=lambda x: x[1], reverse=True)
    possible_word = highest_chance_words[0][0]
    # if the possible word contains a double letter, it chooses the next most probable word
    if len(re.findall(r'(\w)\w*\1', possible_word)) != 0:
        possible_word = highest_chance_words[1][0]

    # print(highest_chance_words[0][0])
    # returns the word with the highest probability as well as the new list of words that are possible based on what
    # Wordle outputs
    return possible_word, new_word_list

"""
the new list of possible words baseed on if the letters are green, yellow or grey. It starts at the first 
letter (pos=0) and iterates through all of the letters, creating branches of the decision tree each time
@:param word_list original list 
of possible words @:param word the word guessed 
@:param pos the index of the letter we are looking at 
@:param double_letters the list of letters that occur multiple times in the word 
@:param count the count of letters we have 
already looked at """
def new_words(word_list, word, pos, double_letters, count):
    # if the end of the word is reached, return the new list of possible words
    if count >= 5:
        return word_list
    # end of the word is not reached
    else:
        # asks the user if a certain letter is correct and stores the input
        print("was letter ", count + 1,
              "correct?\nEnter 0 if letter is green\nEnter 1 if the letter is yellow\nEnter 2 "
              "if the letter is grey")
        inp = int(input())
        # if the letter is green (correct)
        if inp == 0:
            print("here")
            # loops through all words and adds the words from the original list that have the same letter in the same
            # position as the word given
            new_wds = [wd for wd in word_list if wd[pos] == word[pos]]
        # if the letter is yellow (right letter wrong spot)
        elif inp == 1:
            # loops through all words and adds words from the original list that have that letter but not in the
            # specified position
            new_wds = [wd for wd in word_list if word[pos] in wd and wd[pos] != word[pos]]
        # if the letter is grey (not in the word)
        else:
            # Checks if the letter in the specified position is a double letter
            if word[pos] not in double_letters:
                # adds all words from original list that don't contain that letter
                new_wds = [wd for wd in word_list if word[pos] not in wd]
            else:
                # if the letter is a double letter, it takes out all words in the original list that have that letter
                new_wds = [wd for wd in word_list if wd.count(word[pos]) < 2]
        # prints the possible words based on that input
        print("possible words: ", new_wds)
        # runs the function again, this time in the new branch (the new list of words) with the new best word
        # selected, now looking at the next letter
        return new_words(new_wds, word, pos + 1, double_letters, count + 1)


def main():
    # opens the txt file and stores it in the words variable
    f = open("solutions.txt", "r")
    words = f.readlines()
    # sets the starting word to slate, which I found to be the best starting word in part 1 of the project
    word = "slate"
    # makes sure all words are lower case and have a ^ at the start and $ at the end
    cleaned_words = []
    for w in range(len(words)):
        words[w] = words[w].lower()
        cleaned_words.append(words[w][0:-1])
    for index in range(len(cleaned_words)):
        cleaned_words[index] = '^' + cleaned_words[index] + '$'
    new_wd_lst = cleaned_words
    # makes sure the starting word is in the same format as the cleaned words list
    new_wd = '^' + word + '$'
    # asks the user if they got the word, if they did, the loop stops
    while input("did you get the word? y/n: ") != "y":
        # uses the chose_word function to choose the best new word and also returns all the possible words left in
        # that leaf node, based on the previous words guessed
        new_wd, new_wd_lst = chose_word(new_wd_lst, new_wd)
        print(new_wd)


if __name__ == '__main__':
    main()
