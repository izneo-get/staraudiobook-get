# staraudiobook-get
Ce script permet de récupérer un livre présent sur https://staraudiobook.com dans la limite des capacités de notre compte existant.

Il est évident que les fichiers ne doivent en aucun cas être conservées une fois la lecture terminée ou lorsque votre abonnement ne vous permet plus de les lire.


## Utilisation

### staraudiobook_get
**Utilisation en ligne de commande**  
```
staraudiobook_get.py [url]
```

- L'URL doit ressembler à :
```
https://staraudiobook.com/{titre}
``` 
On peut saisir plusieurs URLs (séparées par un espace).  
  
  
**Utilisation en mode interactif**  
```
staraudiobook_get.py
```
Une URL (ou une liste d'URLs séparées par un espace) est demandée.  
  
  
  
## Installation
### Prérequis
- Python 3.7+ (non testé avec les versions précédentes)
- pip
- Librairies SSL

#### Sous Windows
##### Python
Allez sur ce site :  
https://www.python.org/downloads/windows/  
et suivez les instructions d'installation de Python 3.

##### Pip
- Téléchargez [get-pip.py](https://bootstrap.pypa.io/get-pip.py) dans un répertoire.
- Ouvrez une ligne de commande et mettez vous dans ce répertoire.
- Entrez la commande suivante :  
```
python get-pip.py
```
- Voilà ! Pip est installé !
- Vous pouvez vérifier en tapant la commande :  
```
pip -v
```

##### Librairies SSL
- Vous pouvez essayer de les installer avec la commande :  
```
pip install pyopenssl
```
- Vous pouvez télécharger [OpenSSL pour Windows](http://gnuwin32.sourceforge.net/packages/openssl.htm). 

#### Sous Linux
Si vous êtes sous Linux, vous n'avez pas besoin de moi pour installer Python, Pip ou SSL...  

### Téléchargement
- Vous pouvez cloner le repo git :  
```
git clone https://github.com/izneo-get/staraudiobook-get.git
```
ou  
- Vous pouvez télécharger uniquement le binaire Windows (expérimental).  


### Configuration
(pour la version "script" uniquement)
```
pip install -r requirements.txt
```
