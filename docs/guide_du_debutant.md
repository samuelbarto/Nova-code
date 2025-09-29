# Guide du débutant NovaCode

Ce guide a pour objectif de présenter la base du dépôt NovaCode à une personne qui découvre le développement logiciel. Il fournit les repères essentiels pour comprendre la structure, adopter les bonnes pratiques et continuer à progresser sereinement.

## 1. Comprendre l'objectif du dépôt

NovaCode sert de laboratoire d'innovation pour la marque Nova. On y regroupe des projets liés au sport business, à la santé et à la performance. Les équipes y expérimentent des applications web, des applications mobiles et des pipelines de données. Ce dépôt Git centralise ces initiatives pour faciliter la collaboration et le partage de composants.

## 2. Structure générale

Pour l'instant, le dépôt comprend :

- `README.md` : une présentation globale du projet, des principes directeurs et des étapes d'apprentissage recommandées.
- `docs/` : un espace documentaire destiné à accueillir des guides comme celui-ci, des conventions de code et des notes techniques.

À terme, d'autres dossiers apparaîtront lorsqu'un projet sera ajouté. Vous pouvez vous attendre à voir les structures suivantes :

- `apps/` pour les interfaces utilisateurs (React, Flutter, etc.)
- `services/` pour les API et backends (Node.js, Python, Go, ...)
- `data/` pour les notebooks, pipelines d'entraînement ou scripts d'analyse
- `tools/` pour les scripts de déploiement, la configuration CI/CD ou l'infrastructure as code

Chaque dossier contiendra son propre `README.md` expliquant comment installer les dépendances, lancer l'application ou les tests, ainsi que les conventions spécifiques (par exemple le formatage du code ou les standards de revue).

## 3. Notions techniques à maîtriser progressivement

1. **Git et GitHub** : apprendre à cloner le dépôt (`git clone`), créer une branche (`git checkout -b`), committer (`git commit`) et ouvrir une pull request.
2. **Gestion des dépendances** : selon le langage du projet, se former aux outils courants (npm/yarn pour JavaScript, pip/poetry pour Python, etc.).
3. **Exécution locale** : savoir lancer un serveur de développement, exécuter des scripts ou des notebooks et comprendre les logs.
4. **Tests automatisés** : écrire et exécuter des tests unitaires, vérifier la qualité du code (linting) et interpréter les rapports.
5. **Déploiement et CI/CD** : découvrir comment les projets sont publiés (Docker, plateformes cloud) et comment les pipelines automatisés garantissent la qualité.

## 4. Comment débuter concrètement

1. **Installer les outils de base** : Git, un éditeur de code (VS Code), un terminal et éventuellement Docker.
2. **Lire la documentation** : commencez par ce guide puis explorez les autres fichiers dans `docs/` dès qu'ils seront ajoutés.
3. **Suivre un tutoriel pratique** : par exemple, créer une mini-application web ou un script d'analyse de données en vous appuyant sur des ressources pédagogiques (OpenClassrooms, FreeCodeCamp, etc.).
4. **Documenter vos découvertes** : si vous apprenez quelque chose d'utile, ajoutez une note dans `docs/` pour aider les prochains arrivants.
5. **Demander de l'aide** : ouvrez une issue sur GitHub pour poser une question, proposer une idée ou signaler un problème.

## 5. Ressources recommandées

- [Guides GitHub](https://docs.github.com/fr/get-started) pour appréhender le fonctionnement des pull requests.
- [Ressources OpenClassrooms](https://openclassrooms.com/fr/) pour des parcours complets sur le développement web, la data ou le product management.
- [MDN Web Docs](https://developer.mozilla.org/fr/) pour la documentation web.
- [Kaggle Learn](https://www.kaggle.com/learn) pour progresser en data science et machine learning.

## 6. Aller plus loin

Dès qu'un premier projet sera ajouté au dépôt :

- Lisez son `README.md` pour comprendre les commandes disponibles et les bonnes pratiques spécifiques.
- Lancez les tests (`npm test`, `pytest`, etc.) afin de vérifier que votre environnement est correctement configuré.
- Essayez de corriger un bug ou d'ajouter une fonctionnalité simple pour mettre en pratique vos nouvelles compétences.

En suivant ces étapes, vous développerez progressivement les réflexes indispensables pour contribuer efficacement aux projets NovaCode.
