import random
# import locale
from read_from_file import read_file_to_list


# locale.setlocale(locale.LC_ALL, 'sv_SE')

# Texgenereringen förutsätter en ordlista i följande format:
# ordlista( ord0(   ordet,  efterföljandeord(),
#                           efterföljandeordsförekomster())
#           ord1(   ordet,  efterföljandeord(),
#                           efterföljandeordsförekomster())
#           ord2(   ordet,  efterföljandeord(),
#                           efterföljandeordsförekomster())
#           ord3(   ordet,  efterföljandeord(),
#                           efterföljandeordsförekomster()))
# Där ordlista() är hela ordlistan.
#
# ord0(), ord1(), etc., är alla unika ord, som genom sin inkludering i listan ordlista() blir tilldelade nummer (index).
#
# "ordet" etc., är själva ordet som hör till listan ord0(), ord1(), etc..
#
# efterföljandeord() är en lista på nummer tillhörande de ord som representeras i listorna ord0(), ord1(), etc., och syns i respektive listas "ordet".
#
# efterföljandeordsförekomster() är en lista på hur många gånger ordet som representeras av numret med motsvarande index i efterföljandeord() förekommer efter"ordet".


def br():
    print("\n")

def textgenerering(textlängd, ordlista):
    genereradtext = list()
    while len(genereradtext) < textlängd:
        if len(genereradtext) == 0:
            genereradtext.append(ordlista[int(random.random() * len(ordlista))][0])
        else:
            genereradtext.append(ordgenerering(genereradtext[-1:], ordlista))
    return genereradtext


def ordgenerering(senasteordet, ordlista):
    for sublist in ordlista:
        if str(sublist[0]) == str(senasteordet[0]):
            return ordlista[weightedrandom(sublist)][0]

def weightedrandom(dictionary):
    rnd1 = random.random()
    rnd = int(rnd1 * sum(dictionary[2]))
    totalprobability = 0
    for i, weights in enumerate(dictionary[2]):
        totalprobability += weights
        if rnd <= totalprobability:
            return dictionary[1][i]


def ordinlist(uniktord, listaavord):
        try:
            listaavord.index(uniktord)
            return True
        except ValueError:
            return False


def notoutofbounds(index, lista):
    try:
        lista[index]
        return True
    except IndexError:
        return False


def intinput(texttobeprinted):
    while True:
        try:
            return int(input(texttobeprinted))
        except ValueError:
            {}


def ordlistegenerering(textinput):
    allaordiordning = read_file_to_list(textinput)
    unikaord = set(allaordiordning)
    genereradordlista = list()
    enkelordlista = list()

    for uniktord in unikaord:
        templista = uniktord, list(), list()
        genereradordlista.append(templista)
        enkelordlista.append(uniktord)

    for uniktord in genereradordlista:
        tempordiordning = list(allaordiordning)

        while ordinlist(uniktord[0], tempordiordning):
            if notoutofbounds(tempordiordning.index(uniktord[0]) + 1, tempordiordning):
                indexförnästaorditempordiordning = tempordiordning.index(uniktord[0]) + 1
                nästaord = tempordiordning[indexförnästaorditempordiordning]
                indexförnästaordigenereradordlista = enkelordlista.index(nästaord)

                if not ordinlist(indexförnästaordigenereradordlista, uniktord[1]):
                    uniktord[1].append(indexförnästaordigenereradordlista)
                    uniktord[2].append(1)

                elif ordinlist(indexförnästaordigenereradordlista, uniktord[1]):
                    uniktord[2][uniktord[1].index(indexförnästaordigenereradordlista)]+= 1
            tempordiordning = tempordiordning[indexförnästaorditempordiordning + 1:]
    return genereradordlista


print("Detta program använder markovkedjor för att generera nya dikter utifrån Gustav Frödings dikter.")
print("Var god vänta medans den kompletta markovkedjan genereras.")
print("Du kommer snart få välja längd och antal dikter.")
br()

textinput = "froding.txt"  # Texten från vilken ny text skall genereras, måste finnas i samma fil som denna.  MÅSTE VARA UTF-8 KODAD.
ordlista = ordlistegenerering(textinput)


print("Ordlista färdig.")
input("Tryck på valfri tangent för att fortsätta.")
br()
while True:
    antaldikter = intinput("Hur många dikter önskar du generera? ")
    textlängd = intinput("Hur lång vill du att varje dikt skall vara? ")
    br()

    diktnummer = 1
    while antaldikter > 0:
        print("Dikt " + str(diktnummer) + ": " + ' '.join(word for word in textgenerering(textlängd, ordlista)))
        diktnummer += 1
        antaldikter -= 1
    br()
    if input("Är du nöjd med dessa dikter? (ja/nej)") == "ja":
        br()
        break