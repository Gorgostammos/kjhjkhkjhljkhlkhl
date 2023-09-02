

while True:
    navn = input('Skriv inn navn ditt? ')
    etterNavn = input('Skriv inn etternavn ditt? ')
    alder = int(input('hvor gammel er du? '))
    if alder > 18:
        print()
        print(f'hei {navn.title()} {etterNavn.title()}')
        print()

        stude1 = 'Dataenginjør '
        stude2 = 'Lærer'
        stude3 = 'Informasjonsystemer'

        print(f' 1: {stude1}\n 2: {stude2}\n 3: {stude3}\n')

        studie = input("hva studer du? ")


        if studie == 'Dataenginjør':
            print()
            print(f'{stude1}')
            print()
            datastudieaar = int(input('hvilket år er du på? '))
            if datastudieaar == 1:
                fagaar1 = {
                    1: "Prog1",
                    2: "Database",
                    3: '.net'
                }
                print(fagaar1)
            elif datastudieaar == 1:
                fagaar2 = {
                    1: "Prog2",
                    2: "OS",
                    3: 'Kotlin'
                }
                print(fagaar2)
            elif datastudieaar == 3:
                fagaar3 = {
                    1: "Js",
                    2: "C++",
                    3: 'Big data'
                }
                print(fagaar3)

        else:
            print('du er for ungh')

        user = str(input('vil du forsette? '))
        if user == 'Yes':
            continue
        elif user == 'No':
            print('Takk! ')
            break
        else:
            print('Du må velge Yes eller No')
            user = str(input('vil du forsette? '))
            if user == 'Yes':
                continue
            elif user == 'No':
                print('Takk! ')
                break


