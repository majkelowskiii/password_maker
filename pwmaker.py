from secrets import randbelow
from random import shuffle
from sys import argv


class PasswordMaker(object):

    def create_password(self, no_char, no_capital, no_symbols):
        
        password = []
        symbols = ['!', '@', '#', '$', '%', '&', '*', '?']

        while(no_char > 0):
            if no_capital > 0:
                password.append(chr(randbelow(25) + 65)) #equivalent of randint(65,90)
                no_capital -= 1

            elif no_symbols > 0:
                password.append(symbols[randbelow(len(symbols)-1)])
                no_symbols -= 1
            else:
                password.append(chr(randbelow(25) + 97)) #equivalent of randint(97,122)
                
            no_char -= 1

        shuffle(password)

        return ''.join(password)


    def input_number(self, description, max_number):

        number = ''

        while(not(number.isdigit()) or int(number) > max_number):
            print()
            number = input(f'Insert number of {description}. Number must be lower than {max_number}: ')

            if number.isdigit():
                if int(number) > max_number:
                    print(f'Inserted number cannot be greater than {max_number}. Please insert again.')
                else:
                    return int(number)
            else:
                print(f'Please insert a digit that is lower than {max_number}.')


    def mainloop(self):
        no_char = self.input_number('characters', 50)
        no_capital = self.input_number('capital letters', no_char)
        no_symbols = self.input_number('symbols', no_char-no_capital)

        print()
        print(f'Generating password with {no_char} characters, \nfrom which {no_capital} are capital letters and {no_symbols} are symbols.')

        generated_password = self.create_password(no_char, no_capital, no_symbols)

        print('Please find you password below. \nYou can also copy it from \'generated_password.txt\' in script directory.')
        print(generated_password)
        print()
        
        with open('generated_password.txt', 'w') as file:
            file.write(generated_password)


if __name__ == "__main__":
    pw = PasswordMaker()
    pw.mainloop()