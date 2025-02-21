# Student-Management-System-POO

Ordre d'éxécution :
- Lancement du code 'Student Management Project.py'
  (un terminal python3 devrai s'ouvrir si python3 est installer sinon installer python3) (tuto plus bas)

- création d'un nouveau terminal bash

Dans ce terminal bash :
- Création d'un student : curl -X POST https://IP.du.server/students -H "Content-Type: application/json" -d '{"name": "Alice", "age": 20, "studentID": "U001"}
  (un message : "Student created successfully" devrait s'afficher)
  (On peut vérifier avec la commande : curl -X GET http://127.0.0.1:5000/students/U001)

- Création des grades pour le student : curl -X POST http://127.0.0.1:5000/students/U001/grades -H "Content-Type: application/json" -d '{"grades": [75, 85, 90]}'
  (un message "Grades added successfully" devrait s'afficher)

- Enfin pour afficher la moyenne on fait : curl -X GET http://127.0.0.1:5000/students/U001/average


Dans la commande (curl -X POST https://IP.du.server/students -H "Content-Type: application/json" -d '{"name": "Alice", "age": 20, "studentID": "U001"}) on peut changer :
- le nom après "name": "..."
- l'age après "age": ...
- l'id après "studentID": "..."


Dans la commande (curl -X GET http://127.0.0.1:5000/students/U001) :
- il faut changer l'id en fct de ce qu'on a mis précédemment

- pareil pour (curl -X POST http://127.0.0.1:5000/students/U001/grades) et (curl -X GET http://127.0.0.1:5000/students/U001/average)


!!! L'IP.du.serveur est donné lorque l'on lance le code dans le terminal python3



VOICI LA LISTE GLOBAL DES COMMANDES UTILISABLE DANS LE CODE : (les champs modifiable comme "name" son des exemples)

1. Ajouter un étudiant : curl -X POST http://127.0.0.1:5000/students \-H "Content-Type: application/json" \-d '{"studentID": "U001", "name": "John Doe", "age": 20, "level": "undergraduate"}'

2. Récupérer les détails d’un étudiant : curl -X GET http://127.0.0.1:5000/students/U001

3. Ajouter un cours : curl -X POST http://127.0.0.1:5000/courses -H "Content-Type: application/json" -d '{"courseCode": "C001", "courseName": "Mathematics", "creditHours": 3}'

4. Récupérer les détails d’un cours : curl -X GET http://127.0.0.1:5000/courses/C001

5. Inscrire un étudiant à un cours : curl -X POST http://127.0.0.1:5000/enrollments -H "Content-Type: application/json" -d '{"studentID": "U001", "courseCode": "C001"}'

6. Ajouter des notes à un étudiant : curl -X POST http://127.0.0.1:5000/students/U001/grades -H "Content-Type: application/json" -d '{"grades": [85, 90, 78]}'

7. Récupérer la moyenne d’un étudiant : curl -X GET http://127.0.0.1:5000/students/U001/average

---------
marche pas

8. Récupérer les cours d’un étudiant : curl -X GET http://127.0.0.1:5000/students/U001/courses

9. Supprimer un étudiant : curl -X DELETE http://127.0.0.1:5000/students/U001

10. Supprimer un cours : curl -X DELETE http://127.0.0.1:5000/courses/C001


VOICI UN TUTO DE CHATGPT POUR INSTALLER PYTHON3 ET FLASK :

1. Mettre à jour le système

Avant d'installer quoi que ce soit, mets à jour la liste des paquets :

sudo apt update && sudo apt upgrade -y

2. Installer Python 3 et pip

Ubuntu est généralement livré avec Python 3 préinstallé, mais pour s'assurer que tu as la dernière version :

sudo apt install python3 python3-pip -y

3. Vérifier l'installation

Après l'installation, vérifie les versions installées :

python3 --version
pip3 --version

4. Installer un environnement virtuel (optionnel mais recommandé)

Pour isoler ton projet et éviter les conflits entre dépendances :

sudo apt install python3-venv -y

Puis, crée un environnement virtuel dans ton projet :

python3 -m venv venv

Et active-le :

source venv/bin/activate

(Désactive avec deactivate quand tu as fini.)
5. Installer Flask et les dépendances de ton projet

Si tu utilises Flask pour ton API, installe-le avec :

pip install flask

Tu peux aussi ajouter d'autres dépendances comme :

pip install flask flask-restful

6. Exécuter ton application Flask

Si ton fichier principal s’appelle app.py, lance-le avec :

python3 app.py