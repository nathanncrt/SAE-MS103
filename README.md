# **Configuration & Problèmes**
## **Les configurations réalisées** 

>**NB**: Dans ce document les commandes utilisées seront visibles en **_gras et italique_**.
## **I)** **Utilisateurs** :<br>
Pour les ajouts des utilisateurs demandés (ici nica0018 & admin).
<br><br> Nous devions prendre en compte que "admin" possède des droits d'utilisateurs (présent dans le groupe sudo ) et "nica0018" (présent dans le groupe invite).
<br> <br>
Commandes utilisées :<br>
> * Pour nica0018: <br>D'abord créer un groupe "invite" : **_sudo addgroup invite_.**<br> 
Ensuite créer l'utilisateur : **_sudo adduser nica0018 --uid 30451 --gid 100 --home /home/nica0018_** <br>
Enfin ajouter l'utilisateur dans le groupe souhaité : **_sudo adduser nica0018 invite_**<br><br> NB: A la suite de cette commande vous allez devoir rentrer différente information en rapport avec l'utilisateur (nom, mot de passe ...)<br><br>
>* Pour admin : Le groupe "sudo" est déjà présent sur la machine virtuelle donc on crée directement l'utilisateur en premier : **_sudo adduser admin  --uid 12389 --gid 100 --home /home/administrateur_**<br>
Puis ajouter l'utilisateur dans le groupe souhaité : **_sudo adduser admin sudo_** <br><br>
NB: A la suite de cette commande vous allez devoir rentrer différente information en rapport avec l'utilisateur (nom, mot de passe ...)

Problème : pas de problème rencontré pour cette partie.
## **II)** **Outils:**
* Python3 est déjà installé de base sur la VM, si l'on essaye de l'installer avec **_sudo apt install python3_** le terminal nous renvoie : (python3 est déjà la version la plus récente (3.8.2-0ubuntu2)
#### **II.1)** **Formateurs de code source :**<br>
* Installation avec "pip" de "blue" et "isort":
>1) isort : **_pip install isort_**
>2) blue : **_pip install blue_**<br>

Problème : il faut bien écrire la commande avec "pip ..." et non "sudo apt install ...". De plus, des problèmes d'éxécutions avec "black" ont été observé d'où l'utilisation de "isort".
<br>

#### **II.2)** **Analyseurs statiques de code** :<br>
* Installation de "pylint" et "pyflakes":
>1) pylint : **_sudo apt install pylint_**
>2) pyflakes : **_sudo apt install pyflakes_**

Problème : pas de problème rencontré sur cette partie.
<br>



#### **II.3)** **Outil de vérification d'annotations de type** :
* Installation de "mypy" :
>1) mypy: **_sudo apt install mypy_**<br>

Problème : pas de problème rencontré sur cette partie. <br>




#### **II.4)** **Outils de génération de documentation HTML à partir de docstrings :**
NB: Deux outils ont été installés mais ici nous allons uniquement observer le résulat de "pyment".
* Installation de "docformatter" et "pyment" : <br> 


>1) docformatter : **_pip install docformatter_**
>2) pyment : **_pip install pyment_** <br> 

Problème : comme nous avons pu l'observer  pour les formateurs de code source il faut bien penser à utiliser "pip ..." et non "sudo apt install ...".

#### **II.5)** **Cadriciel de tests unitaires** :
* Installation de "pytest" :
>1) pytest : **_pip install pytest_**<br> 

Problème : comme nous avons pu l'observer pour les formateurs de code source et les outils de génération, il faut bien penser à utiliser "pip ..." et non "sudo apt install ...".<br><br>

#### **II.6)** **Bibliothèque pygame :**
* Installation de "pygame" :
>1) pygame : **_sudo pip3 install pygame_** <br>

Problème : il a été nécéssaire de faire une recherche sur : "https://wiki.lereset.org/ateliers:pygamelab:installation" pour trouver la commande correcte. <br>
De plus un dossier est disponible avec un code pygame (non testé) et un fichier texte, dans les vérifications de la sae où vous trouverez un lien vers :
"https://www.cours-gratuit.com/tutoriel-python/tutoriel-python-comment-installer-et-utiliser-pygame", un site où vous est expliqué comment fonctionne pygame.

#### **II.7)** **Git et Meld :**
* Installation de "Git" :
>1) git : sudo apt install git <br>
>2) Vérification de la présence de git : **_git version_** (ici git version 2.25.1)
>3) meld : **_sudo apt install meld_**

* Initialisation du dépôt "Git":
>1) Tout d'abord créer un répertoire "git" : **_mkdir git_** <br>
>2) Ce placer dans ce dernier : **_cd git_** <br>
>3) Suivre "1.Configuration de Git", "2.Premier Dépôt", "3.Dépôt distant", "4.Branches" sur "https://iut-info.univ-reims.fr/users/nourrit/restricted/cours/git/tp01.html#configuration".
>4) Ajoutez enfin ce que vous souhaitez dans votre dépôt distant (ici nous allons déposser ce fichier, des captures d'écrans, des sorties de commandes ...)
<br>
<br>

Problème : ici une erreur survenue lors de l'installation de git (E: Le paquet « git » n'a pas de version susceptible d'être installée).Une solution a été trouvée sur le site (https://grafikart.fr/forum/21707).
Utilisation succesive des commandes : 
>* 1) **_sudo apt-get clean_**
>* 2) **_sudo apt-get update_**
>* 3) **_sudo apt-get install git_**

#### **II.8)** **Visual Studio Code et Extensions :**
* Installation de "Visual Studio Code":
>1) Visual Studio Code : **_sudo snap install code --classic_** 
>2) Pour les extensions il suffit de se rendre sur l'onglet "extensions" sur le logiciel et de rechercher les extensions que l'on souhaite installer.<br>

Problème : ici pour trouver la commande afin d'installer Visual Studio Code, il faut se rendre sur ce lien (https://doc.ubuntu-fr.org/visual_studio_code).
<br>
<br>
<br>
<br>
<br>

### **Ceci était la dernière partie de ce fichier "README". Merci de votre lecture !** 
### **NICART Nathan, étudiant en 1ère année de BUT Informatique à l'IUT RCC.**