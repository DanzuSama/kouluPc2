user_input = str(input('Kenelle teos omistetaan: '))
user_input_text_name = str(input('Mihin kirjoitetaan: '))

#writing file
x = (f'Hei {user_input}, toivomme viihtyisiä hetkiä python-kurssimateriaalin parissa! Terveisin mooc.fi-tiimi')
try:
    with open(user_input_text_name, 'w') as text:
        text.write(x)
except:
    print("File not found")


