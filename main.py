#################################################################################################
#░▒▓███████▓▒░░▒▓█▓▒░░▒▓█▓▒░      ░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓███████▓▒░▒▓████████▓▒░ 
#░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░      ░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░ ░▒▓█▓▒░     
#░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░      ░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░ ░▒▓█▓▒░     
#░▒▓█▓▒░░▒▓█▓▒░░▒▓██████▓▒░       ░▒▓████████▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░ ░▒▓█▓▒░     
#░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░      ░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░ ░▒▓█▓▒░     
#░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░      ░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░ ░▒▓█▓▒░     
#░▒▓███████▓▒░░▒▓█▓▒░░▒▓█▓▒░      ░▒▓█▓▒░░▒▓█▓▒░░▒▓██████▓▒░░▒▓█▓▒░░▒▓█▓▒░ ░▒▓█▓▒░                                                                                                     #                                                                                    #
#################################################################################################

import requests

cible = input("Cible --> ")

cible = cible.strip(' ')

url = ['https://www.instagram.com/', 'https://x.com/',
       'https://www.reddit.com/user/', 'https://www.tiktok.com/',
       'https://www.facebook.com/', 'https://vimeo.com/',
       'https://www.deviantart.com/', 'https://badoo.com/fr/profile/',
       'https://en.gravatar.com/', 'https://disqus.com/by/']

with open('rapport_enquete.txt', 'w', encoding="utf-8") as f:
    for i in url :
        resultat = f"{i}{cible}"
        try :
            headers = {'user-agent':'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:147.0) Gecko/20100101 Firefox/147.0'}
            r = requests.get(resultat, headers=headers,timeout=5)
            if r.status_code == 200:
                f.write(resultat + "\n")
            else :
                continue
        except :
            print("Erreur : site inaccessible")


print("Enquête terminée. Rapport sauvegardé dans rapport_enquete.txt")        

