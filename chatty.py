import random

zufallsantworten=["Oh, wirklich", "Interessant ...", "Das kann man so sehen", "Ich verstehe ..."]

reaktionsantworten = {"essen": "Ich habe leider keinen Geschmackssinn",
                      "isst": "Ich habe leider keinen Geschmackssinn",
                      "wetter": "Ich liebe es wenn die Sonne auf mich scheint, ich darf aber keinen Sonnenbrand bekommen.",
                      "filme": "Die auswahl an Filmen ist heutzutage unendlich groß"
                      "buch" "Ich lese sehr viel über alles" 
                        }

print("Herzlich Willkommen bei deinem persönlichen Chatbot")
print("Mein Name ist Chatty, lass uns zusammen etwas Spaß haben!")
print("Worüber würdest du heute gern reden?")
print("")

nutzereingabe = ""
while nutzereingabe != "bye":
    nutzereingabe = ""
    while nutzereingabe == "":
        nutzereingabe = input("Ihre Frage/Antwort: ")
        
    nutzereingabe = nutzereingabe.lower()
    nutzerwoerter = nutzereingabe.split()
    
    intelligenteAntworten = False
    for einzelwoerter in nutzerwoerter:
        if einzelwoerter in reaktionsantworten:
            print(reaktionsantworten[einzelwoerter])
            intelligenteAntworten = True
    if intelligenteAntworten == False:
        print(random.choice(zufallsantworten))
        
    print("")

print("Einen schönen Tag wünsche ich Dir. Bis zum nächsten Mal")