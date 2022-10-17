import time

go = True
list_of_data = []


def user_choose(input_data):
    global go
    if input_data == 0:
        load_file(list_of_data)
        print('Heippa!')
        go = False
    if input_data == 1:
        user_input_load = input('Anna merkintä:')
        list_data(user_input_load)
        print('Päiväkirja tallennettu')
    if input_data == 2:
        print('Merkinnät:')
        read_file()


def list_data(data):
    list_of_data.append(data)


def read_file():
    if len(list_of_data) == 0:
        try:
            with open('paivakirja.txt', 'r') as text:
                for x in text:
                    print(x[:-1])
                text.close()
        except:
            print("File not found")
    else:
        for x in list_of_data:
            print(x)


def load_file():
    with open('paivakirja.txt', 'w') as text:
        add_text = ''
        s = '\n'
        time_saver = ':::' + time.strftime("%X %x") + '\n'
        for x in list_of_data:
            add_text += x
            add_text += s
        add_text += time_saver
        text.write(add_text)
        text.close()



def main():
    while go:
        user_input = int(input('1 - lisää merkintä, 2 - lue merkinnät, 0 - lopeta: '))
        user_choose(user_input)


if __name__ == "__main__":
    main()
