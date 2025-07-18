from transliterate import get_available_language_codes
from transliterate import translit
from num2words import num2words
import re

text = """Ladies and gentlemen, I'm 78 years old and I finally 
got 15 minutes of fame once in a lifetime and I guess that this is mine. 
People have also told me to make these next few minutes escruciatingly 
embarrassing and to take vengeance of my enemies. Neither will happen.

More than 3 years ago I moved to Novo-Novsk, 
but worked on new Magnetic Storage for last 40. When I was 8...
"""

text_translit = translit(text, 'ru')
all_numbers = re.findall(r'\d+', text)

def num_to_words(num):
    result = ''
    for letter in num:
        word = f'{letter} - {translit(num2words(letter), 'ru')} \n'
        result += word
    return result

print(f'{text_translit}\n{num_to_words(all_numbers)}')