import urllib

def getPage(url):
    try:
        return urllib.urlopen(url).readlines()
    except:
        print "Erro ao abrir o url"

stop = False
print ""

while stop == False:
    dont = False
    nome = "!"
    link = "https://dictionary.com/browse/"
    word = raw_input("Insira palavra a se procurar definicao: ")
    if word == "":
        stop = True
        word = " "
    link += word
    response = getPage(link)
    frase = word + " definition"

    for i in range(len(response)):
        if frase in response[i]:
            try:
                nome = response[i+1].split("definition, ")[1].split("See more")[0]
            except:
                dont = True
            if dont == False:
                print "\n",nome,"\n"

    if nome == "!" and stop == False:

        link = "https://dictionary.com/browse/"
        new_word = word[0].upper()+word[1:]
        link += new_word
        response = getPage(link)
        frase = new_word + " definition"

        for i in range(len(response)):
            if frase in response[i]:
                try:
                    nome = response[i+1].split("definition, ")[1].split("See more")[0]
                except:
                    dont = True
                if dont == False:
                    print "\n",nome,"\n"

        if nome == "!":
            print "\nErro ao achar definicao\n"
