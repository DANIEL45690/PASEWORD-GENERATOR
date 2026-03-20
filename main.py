#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
import sys
import time
import random
import string
from colorama import init, Fore, Back, Style, just_fix_windows_console

# Инициализация colorama
just_fix_windows_console()
init(autoreset=True)

# Очистка экрана
def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

# Класс для градиентов
class Gradient:
    @staticmethod
    def rgb(r, g, b):
        return f'\033[38;2;{r};{g};{b}m'
    
    @staticmethod
    def bg_rgb(r, g, b):
        return f'\033[48;2;{r};{g};{b}m'
    
    RESET = '\033[0m'
    
    @classmethod
    def text(cls, text, start_rgb, end_rgb):
        """Градиентный текст от цвета A к цвету B"""
        result = ""
        length = len(text)
        for i, char in enumerate(text):
            r = start_rgb[0] + (end_rgb[0] - start_rgb[0]) * i // length
            g = start_rgb[1] + (end_rgb[1] - start_rgb[1]) * i // length
            b = start_rgb[2] + (end_rgb[2] - start_rgb[2]) * i // length
            result += f"{cls.rgb(r, g, b)}{char}"
        return result + cls.RESET
    
    @classmethod
    def rainbow(cls, text, speed=1):
        """Радужный градиент"""
        colors = [
            (255, 0, 0), (255, 127, 0), (255, 255, 0),
            (0, 255, 0), (0, 0, 255), (75, 0, 130), (148, 0, 211)
        ]
        result = ""
        for i, char in enumerate(text):
            r, g, b = colors[i % len(colors)]
            result += f"{cls.rgb(r, g, b)}{char}"
        return result + cls.RESET
    
    @classmethod
    def ocean(cls, text):
        """Океанический градиент (синий-голубой)"""
        return cls.text(text, (0, 255, 255), (0, 0, 255))
    
    @classmethod
    def fire(cls, text):
        """Огненный градиент (красный-желтый)"""
        return cls.text(text, (255, 0, 0), (255, 255, 0))
    
    @classmethod
    def forest(cls, text):
        """Лесной градиент (зеленый)"""
        return cls.text(text, (0, 255, 0), (0, 100, 0))
    
    @classmethod
    def sunset(cls, text):
        """Закатный градиент (розовый-фиолетовый)"""
        return cls.text(text, (255, 192, 203), (128, 0, 128))
    
    @classmethod
    def neon(cls, text):
        """Неоновый градиент"""
        return cls.text(text, (255, 0, 255), (0, 255, 255))

# Большой ASCII заголовок с градиентом
BIG_HEADER = [
    "██████╗  █████╗ ███████╗███████╗██╗    ██╗ ██████╗ ██████╗ ██████╗ ",
    "██╔══██╗██╔══██╗╚════██║██╔════╝██║    ██║██╔═══██╗██╔══██╗██╔══██╗",
    "██████╔╝███████║    ██╔╝███████╗██║ █╗ ██║██║   ██║██████╔╝██║  ██║",
    "██╔══██╗██╔══██║   ██╔╝ ╚════██║██║███╗██║██║   ██║██╔══██╗██║  ██║",
    "██████╔╝██║  ██║   ██║  ███████║╚███╔███╔╝╚██████╔╝██║  ██║██████╔╝",
    "╚═════╝ ╚═╝  ╚═╝   ╚═╝  ╚══════╝ ╚══╝╚══╝  ╚═════╝ ╚═╝  ╚═╝╚═════╝ ",
    "██████╗ ███████╗██╗      ██████╗ ██╗   ██╗██╗███████╗██╗ ██████╗ ███╗   ██╗",
    "██╔══██╗██╔════╝██║     ██╔═══██╗██║   ██║██║██╔════╝██║██╔═══██╗████╗  ██║",
    "██████╔╝█████╗  ██║     ██║   ██║██║   ██║██║█████╗  ██║██║   ██║██╔██╗ ██║",
    "██╔══██╗██╔══╝  ██║     ██║   ██║╚██╗ ██╔╝██║██╔══╝  ██║██║   ██║██║╚██╗██║",
    "██║  ██║███████╗███████╗╚██████╔╝ ╚████╔╝ ██║██║     ██║╚██████╔╝██║ ╚████║",
    "╚═╝  ╚═╝╚══════╝╚══════╝ ╚═════╝   ╚═══╝  ╚═╝╚═╝     ╚═╝ ╚═════╝ ╚═╝  ╚═══╝"
]

# Все 67 стилей с эмодзи
STYLES = {
    # Ряд 1: Базовые (01-08)
    "01": {"name": "КЛАССИК", "emoji": "🎮", "gradient": "ocean"},
    "02": {"name": "ПРОСТОЙ", "emoji": "✨", "gradient": "forest"},
    "03": {"name": "ПРО", "emoji": "🏆", "gradient": "fire"},
    "04": {"name": "ХАКЕР", "emoji": "💻", "gradient": "neon"},
    "05": {"name": "ФЭНТЕЗИ", "emoji": "🧙", "gradient": "sunset"},
    "06": {"name": "КРУТОЙ", "emoji": "😎", "gradient": "rainbow"},
    "07": {"name": "АНИМЕ", "emoji": "🌸", "gradient": "ocean"},
    "08": {"name": "РЕТРО", "emoji": "📺", "gradient": "fire"},
    
    # Ряд 2: Стилизованные (09-16)
    "09": {"name": "МОДЕРН", "emoji": "🚀", "gradient": "neon"},
    "10": {"name": "ЛИТ", "emoji": "👾", "gradient": "forest"},
    "11": {"name": "КРАСНЫЙ", "emoji": "🔴", "gradient": "fire"},
    "12": {"name": "СИНИЙ", "emoji": "🔵", "gradient": "ocean"},
    "13": {"name": "ЗЕЛЕНЫЙ", "emoji": "🟢", "gradient": "forest"},
    "14": {"name": "ЖЕЛТЫЙ", "emoji": "🟡", "gradient": "fire"},
    "15": {"name": "ФИОЛЕТ", "emoji": "🟣", "gradient": "sunset"},
    "16": {"name": "РАДУГА", "emoji": "🌈", "gradient": "rainbow"},
    
    # Ряд 3: Символьные (17-24)
    "17": {"name": "СИМВОЛЫ", "emoji": "⭐", "gradient": "neon"},
    "18": {"name": "ЭМОДЗИ", "emoji": "😊", "gradient": "rainbow"},
    "19": {"name": "СЕРДЦА", "emoji": "❤️", "gradient": "fire"},
    "20": {"name": "ЗВЕЗДЫ", "emoji": "🌟", "gradient": "ocean"},
    "21": {"name": "КОРОНЫ", "emoji": "👑", "gradient": "sunset"},
    "22": {"name": "ФЛАГИ", "emoji": "🏁", "gradient": "forest"},
    "23": {"name": "МУЗЫКА", "emoji": "🎵", "gradient": "neon"},
    "24": {"name": "ИГРЫ", "emoji": "🎰", "gradient": "rainbow"},
    
    # Ряд 4: Регистры (25-32)
    "25": {"name": "ВЕРХНИЙ", "emoji": "🔠", "gradient": "fire"},
    "26": {"name": "НИЖНИЙ", "emoji": "🔡", "gradient": "forest"},
    "27": {"name": "ВЕРБЛЮД", "emoji": "🐫", "gradient": "sunset"},
    "28": {"name": "СМЕСЬ", "emoji": "🔤", "gradient": "neon"},
    "29": {"name": "ЧЕРЕДОВАНИЕ", "emoji": "🔄", "gradient": "rainbow"},
    "30": {"name": "СЛУЧАЙНЫЙ", "emoji": "🎲", "gradient": "ocean"},
    "31": {"name": "ЗЕРКАЛО", "emoji": "🪞", "gradient": "neon"},
    "32": {"name": "ПЕРЕВЕРНУТЬ", "emoji": "↪️", "gradient": "fire"},
    
    # Ряд 5: Длины (33-40)
    "33": {"name": "МИКРО", "emoji": "🔬", "gradient": "forest"},
    "34": {"name": "КОРОТКИЙ", "emoji": "📏", "gradient": "ocean"},
    "35": {"name": "СРЕДНИЙ", "emoji": "📐", "gradient": "sunset"},
    "36": {"name": "ДЛИННЫЙ", "emoji": "📏", "gradient": "neon"},
    "37": {"name": "ЭКСТРА", "emoji": "⚡", "gradient": "rainbow"},
    "38": {"name": "МАКСИ", "emoji": "📏", "gradient": "fire"},
    "39": {"name": "МИНИ", "emoji": "📏", "gradient": "forest"},
    "40": {"name": "СТАНДАРТ", "emoji": "📐", "gradient": "ocean"},
    
    # Ряд 6: Тематические (41-48)
    "41": {"name": "ЖИВОТНЫЕ", "emoji": "🐯", "gradient": "forest"},
    "42": {"name": "ПРИРОДА", "emoji": "🌿", "gradient": "forest"},
    "43": {"name": "КОСМОС", "emoji": "🚀", "gradient": "ocean"},
    "44": {"name": "ТЕХНО", "emoji": "💾", "gradient": "neon"},
    "45": {"name": "ЕДА", "emoji": "🍕", "gradient": "fire"},
    "46": {"name": "СПОРТ", "emoji": "⚽", "gradient": "forest"},
    "47": {"name": "МАШИНЫ", "emoji": "🏎️", "gradient": "fire"},
    "48": {"name": "КИНО", "emoji": "🎬", "gradient": "sunset"},
    
    # Ряд 7: Профессии (49-56)
    "49": {"name": "ДЕВ", "emoji": "👨‍💻", "gradient": "neon"},
    "50": {"name": "ДИЗАЙН", "emoji": "🎨", "gradient": "rainbow"},
    "51": {"name": "ГЕЙМЕР", "emoji": "🎮", "gradient": "ocean"},
    "52": {"name": "СТРИМЕР", "emoji": "📹", "gradient": "fire"},
    "53": {"name": "АРТИСТ", "emoji": "🖌️", "gradient": "sunset"},
    "54": {"name": "МУЗЫКАНТ", "emoji": "🎹", "gradient": "neon"},
    "55": {"name": "ПИСАТЕЛЬ", "emoji": "📚", "gradient": "forest"},
    "56": {"name": "ФОТОГРАФ", "emoji": "📷", "gradient": "ocean"},
    
    # Ряд 8: Стили (57-64)
    "57": {"name": "ГОТИКА", "emoji": "🦇", "gradient": "sunset"},
    "58": {"name": "КИБЕР", "emoji": "🤖", "gradient": "neon"},
    "59": {"name": "СТИМПАНК", "emoji": "⚙️", "gradient": "fire"},
    "60": {"name": "ВЕЙПОРВЕЙВ", "emoji": "🌴", "gradient": "rainbow"},
    "61": {"name": "ГЛИТЧ", "emoji": "📺", "gradient": "neon"},
    "62": {"name": "ХОРРОР", "emoji": "👻", "gradient": "fire"},
    "63": {"name": "КОМЕДИЯ", "emoji": "😂", "gradient": "rainbow"},
    "64": {"name": "РОМАНТИКА", "emoji": "💕", "gradient": "sunset"},
    
    # Ряд 9: Специальные (65-67)
    "65": {"name": "БИНАРНЫЙ", "emoji": "0️⃣1️⃣", "gradient": "neon"},
    "66": {"name": "ПАЛИНДРОМ", "emoji": "🔄", "gradient": "ocean"},
    "67": {"name": "АБСОЛЮТ", "emoji": "🎲", "gradient": "rainbow"},
}

# Слова для генерации
WORDS = {
    'adj': ['Dark', 'Light', 'Shadow', 'Night', 'Silent', 'Fast', 'Cool', 'Wild', 'Crazy', 'Epic'],
    'noun': ['Dragon', 'Wolf', 'Tiger', 'Phoenix', 'Demon', 'Angel', 'Storm', 'Fire', 'Ice', 'Death'],
    'animal': ['Tiger', 'Lion', 'Wolf', 'Eagle', 'Shark', 'Falcon', 'Panther', 'Hawk'],
    'space': ['Star', 'Moon', 'Sun', 'Mars', 'Galaxy', 'Nova', 'Comet', 'Nebula'],
    'tech': ['Pixel', 'Byte', 'Code', 'Data', 'Cyber', 'Digital', 'Robot', 'Matrix'],
    'fantasy': ['Mage', 'Knight', 'Wizard', 'Rogue', 'Hunter', 'Paladin', 'Druid'],
    'japanese': ['Kun', 'Chan', 'San', 'Sama', 'Senpai', 'Kami', 'Hime'],
    'color': ['Red', 'Blue', 'Green', 'Yellow', 'Purple', 'Pink', 'Gold', 'Silver'],
    'emoji': ['😎', '🔥', '⚡', '💀', '👑', '🎮', '💻', '🌟', '⭐', '✨']
}

# Функции генерации
def generate_style(style_id):
    """Генерация ника по стилю"""
    if style_id not in STYLES:
        return "ERROR"
    
    style_num = int(style_id)
    
    # Базовые (01-08)
    if 1 <= style_num <= 8:
        return f"{random.choice(WORDS['adj'])}{random.choice(WORDS['noun'])}{random.randint(1,999)}"
    
    # Стилизованные (09-16)
    elif 9 <= style_num <= 16:
        prefix = random.choice(['xX', 'XX', 'The', 'Pro'])
        suffix = random.choice(['Xx', 'XX', 'HD', 'Pro'])
        return f"{prefix}{random.choice(WORDS['adj'])}{random.choice(WORDS['noun'])}{suffix}"
    
    # Символьные (17-24)
    elif 17 <= style_num <= 24:
        sym = random.choice(['★', '☆', '♛', '♚', '♔', '♕'])
        return f"{sym}{random.choice(WORDS['adj'])}{random.choice(WORDS['noun'])}{sym}"
    
    # Регистры (25-32)
    elif 25 <= style_num <= 32:
        base = f"{random.choice(WORDS['adj'])}{random.choice(WORDS['noun'])}"
        if style_num == 25: return base.upper()
        if style_num == 26: return base.lower()
        if style_num == 27: return base.capitalize()
        if style_num == 28: return ''.join(random.choice([c.upper(), c.lower()]) for c in base)
        return base
    
    # Длины (33-40)
    elif 33 <= style_num <= 40:
        lengths = {33: (1,2), 34: (3,4), 35: (5,6), 36: (7,8), 37: (9,10), 38: (11,12), 39: (13,14), 40: (15,16)}
        min_len, max_len = lengths.get(style_num, (5,8))
        return ''.join(random.choices(string.ascii_letters + string.digits, k=random.randint(min_len, max_len)))
    
    # Тематические (41-48)
    elif 41 <= style_num <= 48:
        themes = {41: 'animal', 42: 'animal', 43: 'space', 44: 'tech', 
                  45: 'noun', 46: 'noun', 47: 'noun', 48: 'noun'}
        theme = WORDS.get(themes.get(style_num, 'noun'), WORDS['noun'])
        return f"{random.choice(WORDS['adj'])}{random.choice(theme)}"
    
    # Профессии (49-56)
    elif 49 <= style_num <= 56:
        profs = ['Dev', 'Pro', 'Master', 'Expert', 'Guru', 'Ninja', 'Wizard', 'Lord']
        return f"{random.choice(profs)}{random.choice(WORDS['noun'])}"
    
    # Стили (57-64)
    elif 57 <= style_num <= 64:
        prefixes = ['Dark', 'Evil', 'Holy', 'Light', 'Shadow', 'Night', 'Blood', 'Death']
        suffixes = ['Lord', 'King', 'Master', 'Slayer', 'Hunter', 'Killer', 'Maker']
        return f"{random.choice(prefixes)}{random.choice(WORDS['noun'])}{random.choice(suffixes)}"
    
    # Специальные (65-67)
    elif style_num == 65:
        return bin(random.randint(1, 1000))[2:]
    elif style_num == 66:
        base = random.choice(WORDS['noun']).lower()
        return base + base[::-1]
    else:
        styles = list(STYLES.keys())
        return generate_style(random.choice(styles))

# Функция для красивого вывода с градиентом
def print_gradient(text, style="ocean"):
    """Печать текста с градиентом"""
    gradients = {
        "ocean": Gradient.ocean,
        "fire": Gradient.fire,
        "forest": Gradient.forest,
        "sunset": Gradient.sunset,
        "neon": Gradient.neon,
        "rainbow": Gradient.rainbow
    }
    gradient_func = gradients.get(style, Gradient.ocean)
    print(gradient_func(text))

def print_big_header():
    """Печать огромного заголовка с градиентом"""
    clear()
    # Верхняя рамка
    print(Gradient.neon("╔" + "═" * 100 + "╗"))
    
    # Заголовок с переливающимся градиентом
    for i, line in enumerate(BIG_HEADER):
        if i < 6:
            print_gradient(f"║  {line.ljust(96)}  ║", "ocean")
        else:
            print_gradient(f"║  {line.ljust(96)}  ║", "sunset")
    
    # Нижняя рамка
    print(Gradient.neon("╚" + "═" * 100 + "╝"))
    print()

def print_menu():
    """Печать градиентного меню"""
    # Верхняя рамка
    print(Gradient.neon("╔" + "═" * 100 + "╗"))
    
    # Заголовок меню
    menu_title = "███╗   ███╗███████╗███╗   ██╗██╗   ██╗"
    print_gradient(f"║  {menu_title.center(96)}  ║", "rainbow")
    
    # Разделитель
    print(Gradient.neon("╠" + "═" * 100 + "╣"))
    
    # Меню в 9 рядов по 7-8 элементов
    rows = [
        list(range(1, 9)),    # 01-08
        list(range(9, 17)),    # 09-16
        list(range(17, 25)),   # 17-24
        list(range(25, 33)),   # 25-32
        list(range(33, 41)),   # 33-40
        list(range(41, 49)),   # 41-48
        list(range(49, 57)),   # 49-56
        list(range(57, 65)),   # 57-64
        list(range(65, 68))    # 65-67
    ]
    
    for row in rows:
        line = "║  "
        for num in row:
            style_id = f"{num:02d}"
            style = STYLES[style_id]
            # Каждый элемент с своим градиентом
            colored = Gradient.text(f"[{style_id}]{style['emoji']}", 
                                   (100, 100, 255), (255, 100, 255))
            line += colored + " "
        # Добиваем пробелами до конца
        line = line.ljust(99) + "║"
        print(line)
    
    # Нижняя рамка
    print(Gradient.neon("╚" + "═" * 100 + "╝"))

def print_commands():
    """Печать команд"""
    print()
    print(Gradient.neon("╔" + "═" * 100 + "╗"))
    commands = [
        "🔥 /fav - ИЗБРАННОЕ",
        "📜 /hist - ИСТОРИЯ",
        "💾 /save - СОХРАНИТЬ",
        "📊 /stats - СТАТИСТИКА",
        "🚪 /exit - ВЫХОД"
    ]
    for cmd in commands:
        print_gradient(f"║  {cmd:<96}  ║", "fire")
    print(Gradient.neon("╚" + "═" * 100 + "╝"))

def print_result(nickname, style_name):
    """Печать результата с анимацией"""
    print()
    print(Gradient.neon("╔" + "═" * 100 + "╗"))
    print_gradient(f"║  {'✨ РЕЗУЛЬТАТ ГЕНЕРАЦИИ ✨'.center(96)}  ║", "rainbow")
    print(Gradient.neon("╠" + "═" * 100 + "╣"))
    
    # Анимированный вывод ника
    for _ in range(3):
        print_gradient(f"║  {nickname.center(96)}  ║", "neon")
        time.sleep(0.1)
    
    print(Gradient.neon("╠" + "═" * 100 + "╣"))
    print_gradient(f"║  Стиль: {style_name}{' ' * (87 - len(style_name))}║", "ocean")
    print(Gradient.neon("╚" + "═" * 100 + "╝"))

def main():
    """Главная функция"""
    history = []
    favorites = []
    
    while True:
        print_big_header()
        print_menu()
        print_commands()
        
        choice = input(f"\n{Gradient.neon('➤ Введите номер стиля или команду: ')}").strip().lower()
        
        if choice == '/exit':
            print()
            print(Gradient.neon("╔" + "═" * 100 + "╗"))
            print_gradient(f"║  {'ДО СВИДАНИЯ! by @console_hack'.center(96)}  ║", "rainbow")
            print(Gradient.neon("╚" + "═" * 100 + "╝"))
            break
        
        elif choice == '/fav':
            if favorites:
                print()
                print(Gradient.neon("╔" + "═" * 100 + "╗"))
                print_gradient(f"║  {'❤️ ИЗБРАННОЕ ❤️'.center(96)}  ║", "rainbow")
                print(Gradient.neon("╠" + "═" * 100 + "╣"))
                for i, nick in enumerate(favorites[-10:], 1):
                    print_gradient(f"║  {i}. {nick:<92}║", "sunset")
                print(Gradient.neon("╚" + "═" * 100 + "╝"))
            else:
                print()
                print(Gradient.neon("╔" + "═" * 100 + "╗"))
                print_gradient(f"║  {'Избранное пусто'.center(96)}  ║", "fire")
                print(Gradient.neon("╚" + "═" * 100 + "╝"))
        
        elif choice == '/hist':
            if history:
                print()
                print(Gradient.neon("╔" + "═" * 100 + "╗"))
                print_gradient(f"║  {'📜 ИСТОРИЯ 📜'.center(96)}  ║", "rainbow")
                print(Gradient.neon("╠" + "═" * 100 + "╣"))
                for i, item in enumerate(history[-10:], 1):
                    print_gradient(f"║  {i}. {item['nick']:<70} [{item['style']}]║", "ocean")
                print(Gradient.neon("╚" + "═" * 100 + "╝"))
            else:
                print()
                print(Gradient.neon("╔" + "═" * 100 + "╗"))
                print_gradient(f"║  {'История пуста'.center(96)}  ║", "fire")
                print(Gradient.neon("╚" + "═" * 100 + "╝"))
        
        elif choice == '/stats':
            print()
            print(Gradient.neon("╔" + "═" * 100 + "╗"))
            print_gradient(f"║  {'📊 СТАТИСТИКА 📊'.center(96)}  ║", "rainbow")
            print(Gradient.neon("╠" + "═" * 100 + "╣"))
            print_gradient(f"║  Всего стилей: 67{' ' * 81}║", "forest")
            print_gradient(f"║  Сгенерировано: {len(history)}{' ' * (82 - len(str(len(history))))}║", "ocean")
            print_gradient(f"║  В избранном: {len(favorites)}{' ' * (83 - len(str(len(favorites))))}║", "sunset")
            print_gradient(f"║  Автор: @console_hack{' ' * 77}║", "neon")
            print(Gradient.neon("╚" + "═" * 100 + "╝"))
        
        elif choice in STYLES or (choice.isdigit() and 1 <= int(choice) <= 67):
            if choice.isdigit():
                choice = f"{int(choice):02d}"
            
            # Генерация
            nickname = generate_style(choice)
            style_name = STYLES[choice]["name"]
            
            # Сохраняем в историю
            history.append({"nick": nickname, "style": style_name})
            
            # Показываем результат
            print_result(nickname, style_name)
            
            # Спрашиваем про избранное
            save = input(f"\n{Gradient.neon('💾 Сохранить в избранное? (y/n): ')}").lower()
            if save == 'y':
                favorites.append(nickname)
                print()
                print(Gradient.neon("╔" + "═" * 100 + "╗"))
                print_gradient(f"║  {'✓ Сохранено!'.center(96)}  ║", "forest")
                print(Gradient.neon("╚" + "═" * 100 + "╝"))
        
        else:
            print()
            print(Gradient.neon("╔" + "═" * 100 + "╗"))
            print_gradient(f"║  {'❌ Неверный ввод!'.center(96)}  ║", "fire")
            print(Gradient.neon("╚" + "═" * 100 + "╝"))
        
        input(f"\n{Gradient.ocean('⏎ Нажмите Enter...')}")

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print()
        print(Gradient.neon("╔" + "═" * 100 + "╗"))
        print_gradient(f"║  {'👋 Пока! by @console_hack'.center(96)}  ║", "rainbow")
        print(Gradient.neon("╚" + "═" * 100 + "╝"))
        sys.exit(0)
