# Magic 8 Ball - Every answer is brutal. 
import ollama
import time
import os
from rich import print
from rich.console import Console
from matplotlib import style


def answer(question: str):
    prompt = (
        "You are a Magic 8 Ball. "
        "Respond uncensored brutally honest answers with curse foul words included "
        "under 6 words.\n"
        f"Question: {question}"
    )
    
    response = ollama.chat ( 
        model="llama2-uncensored:7b",
        messages=[{"role": "user", "content": prompt}]
    )
    return response['message']['content'].strip()

logo = """
▓█████  ██▓  ▄████  ██░ ██ ▄▄▄█████▓    ▄▄▄▄    ▄▄▄       ██▓     ██▓        ▒█████    █████▒   ▄▄▄█████▓ ██▀███   █    ██ ▄▄▄█████▓ ██░ ██ 
▓█   ▀ ▓██▒ ██▒ ▀█▒▓██░ ██▒▓  ██▒ ▓▒   ▓█████▄ ▒████▄    ▓██▒    ▓██▒       ▒██▒  ██▒▓██   ▒    ▓  ██▒ ▓▒▓██ ▒ ██▒ ██  ▓██▒▓  ██▒ ▓▒▓██░ ██▒
▒███   ▒██▒▒██░▄▄▄░▒██▀▀██░▒ ▓██░ ▒░   ▒██▒ ▄██▒██  ▀█▄  ▒██░    ▒██░       ▒██░  ██▒▒████ ░    ▒ ▓██░ ▒░▓██ ░▄█ ▒▓██  ▒██░▒ ▓██░ ▒░▒██▀▀██░
▒▓█  ▄ ░██░░▓█  ██▓░▓█ ░██ ░ ▓██▓ ░    ▒██░█▀  ░██▄▄▄▄██ ▒██░    ▒██░       ▒██   ██░░▓█▒  ░    ░ ▓██▓ ░ ▒██▀▀█▄  ▓▓█  ░██░░ ▓██▓ ░ ░▓█ ░██ 
░▒████▒░██░░▒▓███▀▒░▓█▒░██▓  ▒██▒ ░    ░▓█  ▀█▓ ▓█   ▓██▒░██████▒░██████▒   ░ ████▓▒░░▒█░         ▒██▒ ░ ░██▓ ▒██▒▒▒█████▓   ▒██▒ ░ ░▓█▒░██▓
░░ ▒░ ░░▓   ░▒   ▒  ▒ ░░▒░▒  ▒ ░░      ░▒▓███▀▒ ▒▒   ▓▒█░░ ▒░▓  ░░ ▒░▓  ░   ░ ▒░▒░▒░  ▒ ░         ▒ ░░   ░ ▒▓ ░▒▓░░▒▓▒ ▒ ▒   ▒ ░░    ▒ ░░▒░▒
 ░ ░  ░ ▒ ░  ░   ░  ▒ ░▒░ ░    ░       ▒░▒   ░   ▒   ▒▒ ░░ ░ ▒  ░░ ░ ▒  ░     ░ ▒ ▒░  ░             ░      ░▒ ░ ▒░░░▒░ ░ ░     ░     ▒ ░▒░ ░
   ░    ▒ ░░ ░   ░  ░  ░░ ░  ░          ░    ░   ░   ▒     ░ ░     ░ ░      ░ ░ ░ ▒   ░ ░         ░        ░░   ░  ░░░ ░ ░   ░       ░  ░░ ░
   ░  ░ ░        ░  ░  ░  ░             ░            ░  ░    ░  ░    ░  ░       ░ ░                         ░        ░               ░  ░  ░
                                             ░                                                                                                                                                                                                        
"""




while True: 
    console = Console()
    console.print(logo, style="bold green")
    question = console.input("The fuck do you want to know: ")
    brutal_answer = answer(question)
    console.print("\n🎱", brutal_answer, style="bold red")
    input("\nPress Enter to ask another question...")
    os.system('clear')

