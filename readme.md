# LITreview

 L'objectif de ce projet est de mettre en place un site permettant aux utilisateurs de demander et de poster des critiques sur des oeuvres littéraires.



## Table of Contents
- [LITreview](#LITreview)
  - [Table of Contents](#table-of-contents)
  - [Installation](#Installation)
  - [Informations générales](#Informations-générales)
  - [Project Status](#project-status)


## Installation
 
 Vous pouvez télécharger l'archive zip et l'extraire dans le dossier ou vous desirez installer le projet.
 Alternativement,vous pouvez installer le projet dans le dossier désiré avec la commande:
 ```
 git clone https://github.com/ClemRoy/litreview.git
 ```
   Une fois cette étape accompli,déplacez vous dans le dossier litreview a l'aide de :
 ```
 cd litreview
 ```
   Vous pouvez désormais créer un environement virtuel avec:
 ```
 python -m venv env
 ```
 puis l'activer avec:
 ```
 env/scripts/activate
 ```
 La prochaine étape consiste a installer les dépéndance a l'aide de:
 ```
 pip install -r requirements.txt
 ```
 enfin vous pouvez lancer le serveur de développement avec:
 ```
 python manage.py runserver
 ```

## Informations générales

 Une fois le projet installé et le serveur de developpement lancé,vous pouvez accéder au site via l'adresse:
 ```
 http://127.0.0.1:8000/
 ```
   Vous accéderez directement a la page de login,qui vous proposera de vous connecter,ce que vous pouvez faire avec le compte login:admin; mdp: 1234 ) ou en créant un nouveau compte.

 Une fois cette étape franchie vous accederez aux différentes fonctionalitées du site permettant de suivre les autres utilisateurs,de demander des critiques sur un livre,de poster des critiques en réponses, de créer une demande et une critique en même temps,de modifier le contenu dont vous êtes l'auteur,et de fournir a l'utilisateur un feed comprenant ses publications et celle des utilisateurs qu'il suit.
 
  La base de donnée contient 4 autres utilisateurs que vous pouvez suivre en rentrant leurs noms (user1,user2,user3,user4) dans le champ prévu a cet effet.

## Project Status

 Project is: _completed_