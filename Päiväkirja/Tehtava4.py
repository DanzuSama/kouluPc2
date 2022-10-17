def hae_sanat(text):
    with open('sanat.txt', 'r') as file:
        for x in file:
            y = (x[:-1])
            for j in y:
                temp = ''
                if j != ';':
                    temp += j





print(hae_sanat('aaloe;subst-autio'))