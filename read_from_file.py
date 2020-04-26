import string
#import locale

#locale.setlocale(locale.LC_ALL, 'sv_SE')

# Diverse skräptecken

junk = string.punctuation + string.digits

def create_word_freq(orden):
    unika_ord = {}

    for ett_ord in orden:
        if ett_ord not in unika_ord:
            unika_ord[ett_ord] = 1
        else:
            unika_ord[ett_ord] += 1

    return unika_ord


def clean_and_convert(rad):
    clean = clean_line(rad)
    # print("Cleaned:", clean)
    clean = clean.lower()
    # print("Normaliserad:", clean)
    ord = clean.split()
    # print("Ord:", ord)


    return ord


def clean_line(rad):
    cleaned_line = ""
    for tkn in rad:
        if tkn not in junk:
            cleaned_line += tkn
    return cleaned_line


def skapa_frekvenslista(alla_ord):
    ny_lista = []
    for ett_ord in alla_ord:
        ny_lista.append((alla_ord[ett_ord], ett_ord))

    ny_lista.sort(reverse=True)
    print("De 50 mest frekventa orden")
    for i in range(50):
        print(ny_lista[i][0], ny_lista[i][1])

def read_file_to_list(filnamn):
    fp = open(filnamn, 'rt', encoding='utf-8')
    ord_lista = []
    for en_rad in fp:
        orden = clean_and_convert(en_rad)
        # print("Enrad", orden)
        ord_lista += orden
    return ord_lista

# Här startar huvudprogrammet


# print("Start")
# print("Junk:", junk)
# Generera en lista med ord, orden är normaliserade till gemener, "whitespace" och skräptecken borttagna
ord = read_file_to_list("froding.txt")

#print("LC=", locale.nl_langinfo(locale.MON_3)) # LC verkar funka

# Ta fram frekvensen för alla ord

#unika_ord = create_word_freq(ord)
#i = 0
#for nyckel in sorted(unika_ord, key=locale.strxfrm):
#    print(nyckel, "har frekvensen", unika_ord[nyckel])
#    i += 1

#print("Det fanns", i, "unika ord i boken")

#skapa_frekvenslista(unika_ord)
