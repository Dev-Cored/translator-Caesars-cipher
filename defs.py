from colorama import Fore, Back, Style
import os
import time
import string
from datetime import datetime

DEBUG_MODE = False

punctuation_string = string.punctuation
punctuation_list = list(punctuation_string)

en_alphabet = [chr(i) for i in range(ord('a'), ord('z')+1)]
ru_alphabet = [chr(i) for i in range(ord('а'), ord('я')+1)]


if DEBUG_MODE:
    print(f"ru - {ru_alphabet}")
    print(f"en - {en_alphabet}")

def clear_console():
    # Windows
    if os.name == 'nt':
        os.system('cls')
    # macOS и Linux
    else:
        os.system('clear')

def print_to_file(to_file: str, operation: int):
    folder_path = os.path.join(os.path.dirname(__file__), 'saves')
    if DEBUG_MODE:
        print(f"path - {folder_path}")
        print(f"text - {to_file}")

    if not os.path.exists(folder_path):
        os.makedirs(folder_path)

    if operation == 1:
        operation_type = "encripted"
    else:
        operation_type = "decripted"

    current_datetime = datetime.now().strftime("%H-%M-%S--%d-%m-%Y")

    file_name = f"{operation_type}-{current_datetime}.txt"

    file_path = os.path.join(folder_path, file_name)
    with open(file_path, 'w', encoding='utf-8') as file:
        file.write(to_file)
    print(f"Successfully saved by path - {file_path}")

def encrypt(to_file: float):
    clear_console()
    text_lang = int(input(Fore.MAGENTA + "Enter text language: \n1 -> English\n2 -> Russian\n"+Fore.YELLOW + ">"))

    if text_lang > 2 or text_lang < 1:
        print(Fore.RED + Style.BRIGHT + "Invalid language input. Try again." + Style.RESET_ALL)
        time.sleep(3)
        clear_console()
        pass
    else:

        text_to_encrypt = input(Fore.MAGENTA + "Enter text to encrypt: \n")
        text_to_encrypt = text_to_encrypt.lower()

        encrypt_code = int(input(Fore.MAGENTA + "\nEnter encrypt code: "))

        if text_lang > 2 or text_lang < 0:
            print(Fore.RED + Style.BRIGHT + "Invalid language input. Try again." + Style.RESET_ALL)
            time.sleep(3)
            pass

        elif text_lang == 1:
            text_list = list(text_to_encrypt)
            if DEBUG_MODE:
                print(text_list)
            encrypted_text = ""
            for letter in text_list:
                if letter in punctuation_list:
                    encrypted_text += letter
                else:
                    if letter == " ":
                        encrypted_text += " "
                    else:
                        let_id = en_alphabet.index(letter)
                        if let_id + encrypt_code > len(en_alphabet):
                            let_id = let_id - encrypt_code
                        if letter == " ":
                            encrypted_text += " "
                        encrypted_text += en_alphabet[let_id+encrypt_code-1]

            print(Fore.MAGENTA + "======================================================")
            print(f"Encrypted text with encrypt code {encrypt_code}: \n" + encrypted_text+"\n")
            if to_file:
                text = f"""
                ======================================================
                Text without encrypt: 
                
                 {text_to_encrypt}
                ======================================================
                Encrypted text with encrypt code {encrypt_code}: 
                
                 {encrypted_text}
                
                """
                print_to_file(text, 1)
            time.sleep(3)
            input("\nPress Enter to continue...")
            input(Fore.RED + "Second chance ;). Press Enter to continue...")
            clear_console()

        elif text_lang == 2:
            text_list = list(text_to_encrypt)
            if DEBUG_MODE:
                print(text_list)
            encrypted_text = ""
            for letter in text_list:
                if letter in ru_alphabet:
                    let_id = ru_alphabet.index(letter)
                    encrypted_index = (let_id + encrypt_code) % len(ru_alphabet)
                    encrypted_text += ru_alphabet[encrypted_index]
                else:
                    encrypted_text += letter

            print(Fore.MAGENTA + "======================================================")
            print(Fore.MAGENTA + f"Encrypted text with encrypt code {encrypt_code}: \n " + encrypted_text)
            if to_file:
                text = f"""
                ======================================================
                Text without encrypt: 

                 {text_to_encrypt}
                ======================================================
                Encrypted text with encrypt code {encrypt_code}: 

                 {encrypted_text}

                """
                print_to_file(text, 1)
            time.sleep(3)
            input("\nPress Enter to continue...")
            input(Fore.RED + "Second chance ;). Press Enter to continue...")
            clear_console()


def decrypt(to_file: float):
    clear_console()
    text_lang = int(input(Fore.MAGENTA + "Enter text language: \n1 -> English\n2 -> Russian\n"+Fore.YELLOW + ">"))

    if text_lang > 2 or text_lang < 1:
        print(Fore.RED + Style.BRIGHT + "Invalid language input. Try again." + Style.RESET_ALL)
        time.sleep(3)
        clear_console()
        pass
    else:

        text_to_decrypt = input(Fore.MAGENTA + "Enter text to decrypt: \n")
        text_to_decrypt = text_to_decrypt.lower()

        decrypt_code = int(input(Fore.MAGENTA + "\nEnter decrypt code: "))

        if text_lang == 1:
            text_list = list(text_to_decrypt)
            if DEBUG_MODE:
                print(text_list)
            decrypted_text = ""
            for char in text_to_decrypt:
                if char.isalpha():
                    if char in en_alphabet:
                        index = en_alphabet.index(char)
                        decrypted_index = (index - decrypt_code) % 26
                        decrypted_char = en_alphabet[decrypted_index+1]
                        decrypted_text += decrypted_char
                else:
                    decrypted_text += char

            print(Fore.MAGENTA + "======================================================")
            print(Fore.MAGENTA + f"Encrypted text with encrypt code {decrypt_code}: \n" + decrypted_text)
            if to_file:
                text = f"""
                ======================================================
                Text without decrypt: 

                 {text_to_decrypt}
                ======================================================
                Encrypted text with encrypt code {decrypt_code}: 

                 {decrypted_text}
                """
                print_to_file(text, 2)
            time.sleep(3)
            input("Press Enter to continue...")
            input(Fore.RED + "Second chance ;). Press Enter to continue...")
            clear_console()

        if text_lang == 2:
            text_list = list(text_to_decrypt)
            if DEBUG_MODE:
                print(text_list)
            decrypted_text = ""
            for char in text_to_decrypt:
                if char.isalpha():
                    if char in ru_alphabet:
                        index = ru_alphabet.index(char)
                        decrypted_index = (index - decrypt_code) % 33
                        decrypted_char = ru_alphabet[decrypted_index]
                        decrypted_text += decrypted_char
                else:
                    decrypted_text += char

            print(Fore.MAGENTA + "======================================================")
            print(Fore.MAGENTA + f"Encrypted text with encrypt code {decrypt_code}: \n" + decrypted_text)
            if to_file:
                text = f"""
                ======================================================
                Text without decrypt: 

                 {text_to_decrypt}
                ======================================================
                Encrypted text with encrypt code {decrypt_code}: 

                 {decrypted_text}
                """
                print_to_file(text, 2)
            time.sleep(3)
            input(Fore.MAGENTA + "Press Enter to continue...")
            input(Fore.RED + "Second chance ;). Press Enter to continue...")
            clear_console()