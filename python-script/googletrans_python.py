from googletrans import Translator, LANGUAGES
from colorama import Fore
from time import sleep
from tabulate import tabulate
import arabic_reshaper
from bidi.algorithm import get_display

language_1 = [key for key in LANGUAGES]
language_2 = [value for value in LANGUAGES.values()]

# send supported lanuages to file
with open(r"C:\Users\AMIR\python\google-translate\supported_languages.txt", "w", encoding="UTF-8") as support:
    for language in LANGUAGES:
        support.write(f"{language} : {LANGUAGES[language]}\n")

def translate_text(src, dest, text):
    """
    Translate the text
    Args:
        src (str): The language of the text entered by the user
        dest (str): The language into which the text will be translate
        text (str): The translated
    """
    translator = Translator()
    translated = translator.translate(text, src=src, dest=dest)
    print(src, dest)
    # resharped text
    resharped_text_orgin = arabic_reshaper.reshape(translated.origin)
    resharped_text = arabic_reshaper.reshape(translated.text)
        
    converted_origin_text = get_display(resharped_text_orgin)
    converted_text = get_display(resharped_text)

    translate_table = tabulate([[converted_origin_text, converted_text]], headers=["Main text", "Translated text"], tablefmt="double_grid")
    print(translate_table)
    sleep(2)
    
    
while True:
    options = ["Translate", "Supported languages", "Guide to using the project", "Exit"]
    number = 1
    for option in options:
        print(f"[{Fore.RED + str(number) + Fore.RESET}] {option}")
        number += 1
    
    choose_option = input("Sample: 2\nEnter an option: ").capitalize()
    if choose_option in ["1", "Translator"]:
        
        first_language = input("Enter the language in which you write your text: ")
        second_language = input("Enter the language you want your text to be transalte into: ")
    
        if first_language in [*language_1, *language_2] and second_language in [*language_1, *language_2]:
            if first_language in language_1 or second_language in language_1:
                try:
                    first_language = LANGUAGES[first_language]
                    second_language= LANGUAGES[second_language]
                except:
                    pass 
                    
            your_text = input("Enter your text: ")
            translate_text(first_language, second_language, your_text)
           
        else:
            print(f"{Fore.RED + 'The entered languages are incorrect...Enter valid language.' + Fore.RESET}")
            sleep(1)
                
    elif choose_option in ["2", "Support languages"]:
        with open(r"C:\Users\AMIR\python\google-translate\supported_languages.txt", "r", encoding="UTF-8") as languages:
            print(languages.read())
            sleep(2)
            
    elif choose_option in ["3", "Guide to using the project"]:
        with open(r"C:\Users\AMIR\python\google-translate\README.md", encoding="UTF-8") as project_info:
            print(project_info.read(), "\n")
            sleep(2)
    
    elif choose_option in ["4", "Exit"]:
        break
    
    else:
        print(f"{Fore.RED + 'Invalid value...enter number option !' + Fore.RESET}\n")
    print()