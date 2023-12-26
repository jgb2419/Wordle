## Wordle Predictor

## Description
This project determines the best Wordle starting word. It also enables users to input their guesses and predict the most
likely word based on this information.

## Installation

To use this project, follow these simple steps:

1. Ensure you have Python installed on your machine. If not, download and install it from [Python's official website](https://www.python.org/).

2. Clone the repository to your local machine:

    ```bash
    git clone https://github.com/jgb2419/Wordle
    ```

3. Navigate to the project directory:

    ```bash
    cd Wordle
    ```

4. Open a Python environment or script and import the required modules:

    ```python
    import re
    ```

5. You are now ready to use the project! Refer to the [Usage](#usage) section for information on how to get started.



## Usage

### 1. Generating a Starting Word

To generate a starting word using `Bogart_Jenny_Wordle_Starting_Word.py`, follow these steps:

1. Open a terminal or command prompt.

2. Navigate to the directory where the script is located:

    ```bash
    cd path/to/your/repository
    ```

   Replace `path/to/your/repository` with the actual path to your repository.

3. Run the script by executing the following command:

    ```bash
    python Bogart_Jenny_Wordle_Starting_Word.py
    ```

4. The script will output a randomly generated starting word. You can use this word as the initial word for your Wordle game.

### 2. Playing the Wordle Game

To play the Wordle game using `Bogart_Jenny_Guess.py`, follow these steps:

1. Open a terminal or command prompt.

2. Navigate to the directory where the script is located:

    ```bash
    cd path/to/your/repository
    ```

   Replace `path/to/your/repository` with the actual path to your repository.

3. Run the script by executing the following command:

    ```bash
    python Bogart_Jenny_Guess.py
    ```

4. The program will ask you for the number of yellow and green letters that you received after that guess. The program will then provide you with the next best guess
   
5. Continue inputting your guesses and results until the final word is reached. 

### Additional Information

- The `Bogart_Jenny_Guess.py` script interacts with the `Bogart_Jenny_Wordle_Starting_Word.py` script to get the initial word for the game. The `Bogart_Jenny_Guess.py` script assumes that your first guess is the starting word obtained from `Bogart_Jenny_Wordle_Starting_Word.py`

- The `solutions.txt` file contains possible words that may be used as the starting word. Feel free to explore and modify this file based on your preferences.

## Decision Function
The first cost function I used to split my decision tree was based on the position of the letters in the word. I grouped the words by the green letters I received. I put all of the letters that had the green letter in the correct place in the acceptable list and the words that didn’t have the correct letter in that place, I put in a different list. Then, I split the words based on the yellow letters I received. I split it based on if the word was in the word and not at the position given it went in the acceptable list, and words that did not contain the letter or did contain the letter but at the position given, we. Then, I split the list based on what grey letters I received. If the letter was in the word, I put it in one list and if the letter was not in the word, it would go in the acceptable list. Then, I used the same cost function as the first part of the wordle project to calculate which word to list from the acceptable word list. I calculated the probability of each bigram and trigram being in the word as well as the probability of each letter being in the word. I then added these together to get the total probability. I then selected the word with the highest probability.
