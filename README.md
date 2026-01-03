README Académique – Projet de Recherche Opérationnelle

Informations Générales
Université Libanaise Mauritanie
Filière : Sciences et Technologies
Module : Recherche Opérationnelle
Année académique : 2025 – 2026
Travail organisé par :

Rajaonson Randi Honenantsoa (ID: 12430009)

Ibtissam Ahmed Khalifa (ID : 12430037)

El Kebir Mohameden M’beirick (ID: 12430101)

Encadrant : Dr. Bennani

Objet du Projet

Ce travail s’inscrit dans le cadre du module de Recherche Opérationnelle et porte sur l’étude progressive et appliquée des problèmes d’optimisation liés au transport et à la logistique.

Le projet comprend trois axes principaux :

1. Optimisation du transport

2. Problème de tournées de véhicules (VRP), optimisation combinatoire et heuristiques

3. Application réelle : routage des camions d’eau

Chaque axe a été attribué à un membre du groupe conformément à la répartition présentée ci-dessous.

Répartition du Travail au Sein du Groupe

Thème 1 — Optimisation du Transport

Travail réalisé par : El Kebir

- Présentation théorique du problème de transport
- Définition des données (offres, demandes, matrice des coûts)
- Modélisation mathématique du problème
- Application des méthodes suivantes :
  • Méthode du coin Nord-Ouest
  • Méthode du moindre coût
  • Méthode MODI (vérification d’optimalité)
- Validation de la solution à l’aide d’un outil informatique (Python – PuLP)

Remarques méthodologiques :
- Les méthodes manuelles facilitent la compréhension progressive du problème.
- La méthode MODI est essentielle pour garantir l’optimalité.
- Pour les problèmes de grande taille, l’utilisation d’outils informatiques devient indispensable.
- 
Thème 2 — VRP, Optimisation Combinatoire et Heuristiques

Travail réalisé par : Ibtissam 
- Présentation théorique du problème de tournées de véhicules (VRP)
- Définition des données et contraintes
- Utilisation de deux approches :

Approche exacte (combinatoire) :
- Exploration exhaustive des tournées possibles
- Recherche de la solution optimale
- Garantie de minimalité du coût
Limite : temps de calcul élevé lorsque le nombre de clients augmente

Approche heuristique (méthode de Clarke & Wright – Savings) :
- Construction progressive des tournées
- Respect des contraintes de capacité
- Réduction du temps de calcul
- Solution proche de l’optimal

Comparaison des approches :
- Méthode combinatoire : optimale mais coûteuse en calcul
- Méthode heuristique : rapide, efficace et adaptée aux situations réelles
  
Thème 3 — Application Réelle : Routage des Camions d’Eau

Travail réalisé par : Randi

- Définition du contexte réel (dépôt, clients, demandes, capacité)
- Calcul des distances (euclidiennes)
- Application d’une méthode heuristique adaptée
- Construction et validation des tournées
- Vérification des contraintes de capacité
- Validation via un outil informatique (OR-Tools)

Remarques méthodologiques :
- L’heuristique garantit une solution faisable et opérationnelle.
- Elle offre un compromis entre performance et réalisme.
- L’outil informatique assure précision et fiabilité.
  
Synthèse Générale du Projet

Ce projet montre comment :
- un problème simple de transport peut évoluer vers un problème logistique complexe ;
- la modélisation mathématique aide à la prise de décision ;
- les méthodes exactes et heuristiques sont complémentaires ;
- les outils informatiques jouent un rôle essentiel dans l’optimisation moderne.

Le travail illustre la capacité de la Recherche Opérationnelle à :
- améliorer la planification,
- réduire les coûts,
- optimiser l’efficacité opérationnelle.
Conclusion Générale
La réalisation de ce projet a permis :
- de renforcer les connaissances théoriques du module ;
- de maîtriser les méthodes classiques du problème de transport ;
- de comprendre la complexité croissante du VRP ;
- d’utiliser des outils informatiques professionnels (PuLP, itertools, OR-Tools) ;
- de relier théorie et pratique à travers une application réelle.

Ce travail met en évidence la pertinence de la Recherche Opérationnelle dans la résolution efficace des problèmes de transport et de logistique.
