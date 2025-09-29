# Nova-code

NovaCode est un environnement de développement dédié aux projets liés au sport business et à l’innovation digitale. L’objectif est de tester, prototyper et automatiser des solutions (web, mobile et data) pour soutenir la marque Nova et explorer de nouvelles applications dans le sport, la santé et la performance.

## Structure générale du dépôt

À ce stade, le dépôt se concentre sur la mise en place de l'environnement de travail et ne contient qu'un socle documentaire. Cette base est volontairement légère afin de permettre aux équipes de définir progressivement les composants techniques dont elles ont besoin.

| Chemin | Description |
|--------|-------------|
| `README.md` | Vue d'ensemble du projet et repères pour comprendre l'objectif de NovaCode. |
| `docs/` | Documentation complémentaire (guides d'onboarding, conventions à venir, notes de conception). |

En fonction des projets (site web, application mobile, pipelines data), de nouveaux dossiers viendront structurer le dépôt, par exemple :

- `apps/` pour les applications clientes (web ou mobile) qui partagent un même design system ;
- `services/` pour les API ou microservices métiers ;
- `data/` pour les notebooks, pipelines et scripts d'automatisation ;
- `tools/` pour les scripts utilitaires ou l'infrastructure as code.

Ces dossiers n'existent pas encore mais constituent un cadre de référence pour organiser les futurs développements.

## Principes importants à connaître

1. **Modularité** : chaque domaine (produit digital, data, automatisation) doit pouvoir évoluer indépendamment tout en partageant des composants communs (UI, services, modèles).
2. **Automatisation** : l'objectif de NovaCode est de faciliter l'expérimentation rapide. Les scripts d'installation, de tests et de déploiement (CI/CD) devront être centralisés dans `tools/` à mesure qu'ils seront créés.
3. **Documentation continue** : tout nouveau projet ou module doit arriver avec un dossier `README.md` local décrivant son but, sa stack technologique, la manière de le lancer et les conventions utilisées.
4. **Qualité et mesure** : les projets liés à la performance sportive manipulent des données sensibles. Les tests automatisés, la traçabilité des transformations et la conformité RGPD seront des axes de travail prioritaires.

## Repères pour la suite de l'apprentissage

Pour un profil néophyte, voici un parcours recommandé :

1. **Comprendre Git et GitHub** : savoir cloner le dépôt, créer des branches et ouvrir des pull requests.
2. **Installer l'environnement** : se familiariser avec l'utilisation de conteneurs (Docker) ou d'environnements virtuels selon la technologie choisie.
3. **Explorer un premier projet** : lorsqu'un sous-dossier (`apps/`, `services/` ou `data/`) sera ajouté, lire son `README` pour comprendre les dépendances et lancer les tests.
4. **Contribuer à la documentation** : enrichir les guides dans `docs/` en partageant les bonnes pratiques, conventions de code, et checklist de revue.
5. **Mettre en place des tests** : dès que des composants apparaissent, ajouter des tests unitaires et, si nécessaire, des tests d'intégration pour sécuriser les expérimentations.

La section [Guide du débutant](docs/guide_du_debutant.md) détaille ces étapes et propose des ressources pour monter en compétence progressivement.

## Ressources utiles

- [Git - Documentation officielle](https://git-scm.com/doc)
- [Docker - Guide de démarrage](https://docs.docker.com/get-started/)
- [RGPD et données sportives](https://www.cnil.fr/fr/sport-donnees-personnelles-et-rgpd) pour se sensibiliser aux obligations légales.

Ce dépôt a vocation à évoluer rapidement : n'hésitez pas à proposer des améliorations via des issues ou des pull requests.
