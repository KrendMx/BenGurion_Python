import curses
import math

class CommandLineInterface:
    def __init__(self, nature):
        self.commands = {
            "info": self.display_data,
            'exit': self.exit_cli,
            'help': self.get_help,
            'add animal': self.add_animal,
            'set time': self.set_time,
            'add food': self.add_food,
            'reproduction': self.reproduction,
            'food animals': self.food_animals,
        }
        self.running = True
        self.nature = nature

    def start(self):
        curses.wrapper(self.main)

    def main(self, stdscr):
        curses.curs_set(1)
        curses.wrapper(lambda stdscr: print("Height:", stdscr.getmaxyx()[0], "Width:", stdscr.getmaxyx()[1]))
        stdscr.clear()
        self.stdscr = stdscr
        self.stdscr.refresh()
        self.input_window = curses.newwin(1, curses.COLS, curses.LINES - 1, 0)
        self.input_window.refresh()

        while self.running:
            self.input_window.clear()
            self.stdscr.addstr(curses.LINES - 2, 0, "Command: ")
            self.input_window.refresh()
            command = self.get_input()
            self.execute_command(command)

    def get_input(self):
        input_str = ""
        while True:
            key = self.input_window.getch()
            if key == curses.KEY_ENTER or key in [10, 13]:  # Enter key
                self.input_window.clear()
                return input_str
            elif key in [curses.KEY_BACKSPACE, 127, 8]:  # Backspace key
                input_str = input_str[:-1]
                self.input_window.clear()
                self.input_window.addstr(input_str)
                self.input_window.refresh()
            else:
                input_str += chr(key)
                self.input_window.addstr(chr(key))
                self.input_window.refresh()

    def execute_command(self, command):
        if command in self.commands:
            self.commands[command]()
        else:
            self.stdscr.addstr(curses.LINES - 3, 0, f"Unknown command: {command}")
            self.stdscr.refresh()
        
    def display_data(self):
        self.stdscr.clear() 
        self.stdscr.addstr(4, 4, f'Сейчас в системе еды: {self.nature.food}')
        self.stdscr.addstr(5, 4, f'Животные в системе')
        
        animals = self.nature.get_all_animals()
        
        for i in range(len(animals)):
            self.stdscr.addstr(6+i, 4 + 5, f'Животное {animals[i].id}  --- класс: {animals[i].__class__.__name__}; Охотник: {animals[i].hunter}; Сытость:{animals[i].fullness}%; Возраст:{animals[i].oldest}; Мужской пол: {animals[i].male}')
        self.stdscr.refresh() 
        self.stdscr.addstr(curses.LINES - 2, 4, "Press any key to continue...")  
        self.stdscr.refresh()
        self.stdscr.getch() 
        self.stdscr.clear()  
        self.stdscr.refresh()
    
    def set_time(self):
        pass
    
    def add_food(self):
        self.stdscr.clear()
        
        self.stdscr.addstr(5, 4, 'Введите количество еды числом')
        self.stdscr.refresh()
        
        type = self.get_input()
        self.input_window.refresh()
        self.stdscr.addstr(10, 4, type)
        
        self.nature.increase_food(int(type))
        
        self.stdscr.addstr(15, 4, f'Новое количество еды: {self.nature.food}')
        self.stdscr.refresh()
        
        self.input_window.clear()

        self.stdscr.addstr(curses.LINES - 2, 4, "Press any key to continue...")  
        self.stdscr.refresh()
        self.stdscr.getch() 
        self.stdscr.clear()  
        self.stdscr.refresh()
    
    def reproduction(self):
        self.stdscr.clear()

        animals = self.nature.get_all_animals()
        
        for i in range(len(animals)):
            self.stdscr.addstr(6+i, 4 + 5, f'Животное {animals[i].id}  --- класс: {animals[i].__class__.__name__}; Охотник: {animals[i].hunter}; Сытость:{animals[i].fullness}%; Возраст:{animals[i].oldest}; Мужской пол: {animals[i].male}')
        self.stdscr.addstr(8+len(animals), 4, f'Введите id животного 1')
        self.stdscr.refresh()

        id1 = self.get_input()
        self.stdscr.addstr(10+len(animals), 4, f'{id1}')
        self.stdscr.addstr(12+len(animals), 4, f'Введите id животного 2')
        self.stdscr.refresh()

        id2 = self.get_input()
        self.stdscr.addstr(14+len(animals), 4, f'{id2}')
        self.stdscr.addstr(18+len(animals), 4, f'Создаем животное...')

        self.stdscr.addstr(18+len(animals), 4, self.nature.model_inproduction(id1, id2))
        
        self.stdscr.refresh()
        
        self.stdscr.refresh()


        self.stdscr.addstr(curses.LINES - 2, 4, "Press any key to continue...")  
        self.stdscr.refresh()
        self.stdscr.getch() 
        self.stdscr.clear()  
        self.stdscr.refresh()


    
    def get_help(self):
        self.stdscr.clear()
        
        self.stdscr.addstr(4, 4, 'help - Список доступных комманд')
        self.stdscr.addstr(5, 4, 'info - Информация о системе')
        self.stdscr.addstr(6, 4, 'add animal *type* *age* *fullness* *male* - Добавляет животное в систему. Номер типа: 1 - воздушные, 2 - земные, 3 - морские. Возраст - любое число. Пища - любое число. Пол - Булевое значение')
        self.stdscr.addstr(7, 4, 'skip time - меняет время на тик вперед')
        self.stdscr.addstr(8, 4, 'add food *count* - Добавляет еду в систему')
        self.stdscr.addstr(9, 4, 'increase - Размножает двух особей или выводит ошибку в случае неудачи')
        
        self.stdscr.refresh() 
        self.stdscr.addstr(curses.LINES - 2, 0, "Press any key to continue...")  
        self.stdscr.refresh()
        self.stdscr.getch()
        self.stdscr.clear()  
        self.stdscr.refresh()

    def add_animal(self):
        self.stdscr.clear()
        
        self.stdscr.addstr(3, 4, 'Введите тип животного: 1, 2, 3')
        self.stdscr.refresh()
        
        type = self.get_input()
        self.input_window.refresh()
        self.stdscr.addstr(4, 4, type)
        self.stdscr.addstr(5, 4, 'Введите возраст')
        
        self.stdscr.refresh()
        
        age = self.get_input()
        self.input_window.refresh()
        self.stdscr.addstr(6, 4, age)
        self.stdscr.addstr(7, 4, 'Введите сытость животного числом')
        
        self.stdscr.refresh()
        
        fullness = self.get_input()
        self.input_window.refresh()
        self.stdscr.addstr(8, 4, fullness)
        self.stdscr.addstr(9, 4, 'Введите пол животного числом 1 - мужчина, 2 - женщина')
        
        self.stdscr.refresh()
        
        male = self.get_input()
        self.input_window.refresh()
        self.stdscr.addstr(10, 4, male)
        self.stdscr.addstr(11, 4, 'Животное охотник? 1 - да, 2 - нет')
                
        self.stdscr.refresh()
        
        hunter = self.get_input()
        self.input_window.refresh()
        self.stdscr.addstr(12, 4, hunter)
        self.stdscr.addstr(17, 4, 'Создаем животное')
        
        self.stdscr.refresh()
        
        i = self.nature.get_current_animal(self.nature.create_animal(int(type),int(age),int(fullness),int(male), int(hunter) == 1))
        
        self.stdscr.addstr(20, 4, "Животное создано:")  
        self.stdscr.addstr(22, 8, f'Животное {i.id}  --- класс: {i.__class__.__name__}; Охотник: {i.hunter}; Сытость:{i.fullness}%; Возраст:{i.oldest}; Мужской пол: {i.male}')

        self.stdscr.addstr(curses.LINES - 2, 4, "Press any key to continue...")  
        self.stdscr.refresh()
        self.stdscr.getch()
        self.stdscr.clear()  
        self.stdscr.refresh()
    
    def food_animals(self):
        self.stdscr.clear()

        self.nature.eating()
        
        self.stdscr.addstr(15, 4, 'Животные успешно покормлены')
        self.stdscr.refresh()
        
        self.stdscr.addstr(curses.LINES - 2, 4, "Press any key to continue...")  
        self.stdscr.refresh()
        self.stdscr.getch() 
        self.stdscr.clear()  
        self.stdscr.refresh()


        
    
    def exit_cli(self):
        self.running = False
