<div align="center">

![PalworldSaveToolsLogo](resources/PalworldSaveTools_Blue.png)

# PalworldSaveTools

**Une boîte à outils complète d'édition de fichiers de sauvegarde pour Palworld**

[![Téléchargements](https://img.shields.io/github/downloads/deafdudecomputers/PalworldSaveTools/total)](https://github.com/deafdudecomputers/PalworldTools/releases/latest)
[![Licence](https://img.shields.io/github/license/deafdudecomputers/PalworldSaveTools)](LICENSE)
[![Discord](https://img.shields.io/badge/Discord-Join_for_support-blue)](https://discord.gg/sYcZwcT4cT)
[![NexusMods](https://img.shields.io/badge/NexusMods-Download-orange)](https://www.nexusmods.com/palworld/mods/3190)

[Anglais](resources/readme/README.en_US.md) | [简体中文](resources/readme/README.zh_CN.md) | [Deutsch](resources/readme/README.de_DE.md) | [Español](resources/readme/README.es_ES.md) | [Français](resources/readme/README.fr_FR.md) | [Русский](resources/readme/README.ru_RU.md) | [日本語](resources/readme/README.ja_JP.md) | [한국어](resources/readme/README.ko_KR.md)

---

### **Download the standalone version from [GitHub Sorties](https://github.com/deafdudecomputers/PalworldSaveTools/releases/latest)**

---

</div>

## Table of Contents

- [Features](#fonctionnalités)
- [Installation](#installation)
- [Quick Start](#démarrage rapide)
- [Présentation des outils](#tools-overview)
- [Guides](#guides)
- [Troubleshooting](#dépannage)
- [Contributing](#contribution)
- [Licence](#licence)

---

## Features

### Fonctionnalité de base

| Fonctionnalité | Description |
| --------- | ------------- |
| ** Analyse de sauvegarde rapide ** | L'un des lecteurs de fichiers de sauvegarde les plus rapides disponibles |
| **Gestion des joueurs** | Afficher, modifier, renommer, changer de niveau, débloquer des technologies et gérer les joueurs |
| **Gestion de guilde** | Créez, renommez, déplacez des joueurs, débloquez des recherches en laboratoire et gérez des guildes |
| **Éditeur copain** | Éditeur complet pour les statistiques, les compétences, les IV, le rang, les âmes, le sexe, le boss/le bouton chanceux |
| **Outils du camp de base** | Exportez, importez, clonez, ajustez le rayon et gérez les bases |
| ** Visionneuse de carte ** | Base interactive et carte des joueurs avec coordonnées et détails |
| **Transfert de personnage** | Transférer des personnages entre différents mondes/serveurs (sauvegarde croisée) |
| **Enregistrer la conversion** | Convertir entre les formats Steam et GamePass |
| **Paramètres mondiaux** | Modifier les paramètres WorldOption et LevelMeta |
| **Outils d'horodatage** | Corrigez les horodatages négatifs et réinitialisez les temps des joueurs |

### Outils tout-en-un

La suite **All-in-One Tools** offre une gestion complète des sauvegardes :

- **Outils de suppression**
  - Supprimer Players, bases ou guildes
  - Supprimer les joueurs inactifs en fonction de seuils de temps
  - Supprimez les joueurs en double et les guildes vides
  - Supprimer les données non référencées/orphelines

- **Outils de nettoyage**
  - Supprimer les éléments invalides/modifiés
  - Supprimer les amis et passifs invalides
  - Corriger les copains illégaux (limiter les statistiques maximales légales)
  - Supprimer les structures invalides
  - Réinitialiser les tourelles anti-aériennes
  - Débloquez des coffres privés

- **Outils de guilde**
  - Reconstruire toutes les guildes
  - Déplacer les joueurs entre les guildes
  - Devenir chef de guilde de joueurs
  - Renommer les guildes
  - Niveau de guilde maximum
  - Débloquez toutes les recherches en laboratoire

- **Outils du lecteur**
  - Modifier les statistiques et les compétences des amis des joueurs
  - Débloquez toutes les technologies
  - Déverrouiller la cage de visualisation
  - Joueurs de niveau supérieur/vers le bas
  - Renommer les joueurs

- **Enregistrer les utilitaires**
  - Réinitialiser les missions
  - Réinitialiser les donjons
  - Corriger les horodatages
  - Réduisez les stocks surchargés
  - Générer des commandes PalDefender

### Outils supplémentaires

| Outil | Description |
| ------ | ------------- |
| **Modifier les amis joueurs** | Éditeur pal complet avec statistiques, compétences, IV, talents, âmes, rang et sexe |
| **SteamID Convertisseur** | Convertir les identifiants Steam en Palworld UIDs |
| **Correction de la sauvegarde de l'hôte** | Échangez des UID entre deux joueurs (par exemple, pour un échange d'hôte) |
| **Échanger le joueur UIDs** | Échangez des UID entre deux joueurs |
| **Injecteur à fente** | Augmenter les emplacements palbox par joueur |
| **Restaurer la carte** | Appliquer la progression de la carte déverrouillée sur tous les mondes/serveurs |
| ** Renommer le monde ** | Changer le nom du monde dans LevelMeta |
| **WorldOption Éditeur** | Modifier les paramètres et la configuration du monde |
| **LevelMeta Éditeur** | Modifier les métadonnées du monde (nom, hôte, niveau) |
| **Convertisseur de coordonnées** | Convertir les coordonnées dans le jeu |

---

## Installation

### Prérequis

**Pour autonome (Windows) :**
- Windows 10/11
- [Microsoft Visual C++ Redistributable](https://learn.microsoft.com/en-us/cpp/windows/latest-supported-vc-redist?view=msvc-170#latest-microsoft-visual-c-redistributable-version) (2015-2022)

**Pour une exécution à partir des sources (Linux ou développement) :**
- Python 3.10 ou supérieur
- pip (gestionnaire de paquets Python)

### Autonome (Windows - Recommandé)

1. Téléchargez la dernière version à partir de [GitHub Releases](https://github.com/deafdudecomputers/PalworldSaveTools/releases/latest)
2. Extraire le fichier zip
3. Exécutez `PalworldSaveTools.exe`

### Depuis la source (Linux ou pour le développement)

```bash
git clone https://github.com/deafdudecomputers/PalworldSaveTools.git
cd PalworldSaveTools
pip install -r requirements.txt
python start.py
```

---

## Quick Start

1. **Chargez votre sauvegarde**
   - Cliquez sur **Fichier → Charger l'enregistrement**
   - Accédez à votre dossier de sauvegarde Palworld
   - Sélectionnez `Level.sav`

2. **Explorez vos données**
   - Utilisez les onglets pour afficher Players, les guildes, les bases ou la carte.
   - Rechercher et filtrer pour trouver des entrées spécifiques

3. **Apporter des modifications**
   - Sélectionnez les éléments à modifier, supprimer ou modifier
   - Utilisez les menus contextuels pour des options supplémentaires

4. ** Enregistrez vos modifications **
   - Cliquez sur **Fichier → Enregistrer les modifications**
   - Les sauvegardes sont créées automatiquement

---

## Outils Présentation

### Outils tout-en-un (AIO)

L'interface principale pour une gestion complète des sauvegardes avec trois onglets :

**Players Onglet** - Afficher et gérer tous les joueurs sur le serveur
- Modifier les noms des joueurs, les niveaux et le nombre d'amis
- Supprimer les joueurs inactifs
- Afficher les guildes de joueurs et la dernière fois en ligne

**Onglet Guildes** - Gérer les guildes et leurs bases
- Renommer les guildes, changer de chef
- Afficher les emplacements et les niveaux de base
- Supprimer les guildes vides ou inactives

**Onglet Bases** - Afficher tous les camps de base
- Exporter/importer des plans de base
- Cloner des bases vers d'autres guildes
- Ajuster le rayon de base

### Visionneuse de cartes

Visualisation interactive de votre monde :
- Afficher tous les emplacements de base et les positions des joueurs
- Filtrer par guilde ou nom de joueur
- Cliquez sur les marqueurs pour des informations détaillées
- Générer des commandes `killnearestbase` pour PalDefender

### Transfert de personnage

Transférer des personnages entre différents mondes/serveurs (sauvegarde croisée) :
- Transférer un seul ou tous les joueurs
- Préserve les personnages, les amis, l'inventaire et la technologie
- Utile pour migrer entre la coopérative et les dedicated servers

### Correction de la sauvegarde de l'hôte

Échangez des UID entre deux joueurs :
- Transférer la progression d'un joueur à un autre
- Indispensable pour les transferts de host/co-op vers le serveur
- Utile pour échanger le rôle d'hôte entre les joueurs
- Utile pour les échanges de plates-formes (Xbox ↔ Steam)
- Résout les problèmes d'affectation hôte/serveur UID
- **Note:** Affected player must have a character created on the target save first

---

## Guides

### Enregistrer les emplacements des fichiers

**Hôte/Coop :**
```
%localappdata%\Pal\Saved\SaveGames\YOURID\RANDOMID\
```

**Serveur dédié :**
```
steamapps\common\Palworld\Pal\Saved\SaveGames\0\RANDOMSERVERID\
```

### Déverrouillage de la carte

<détails>
<summary>Cliquez pour développer les instructions de déverrouillage de la carte</summary>

1. Copiez `LocalData.sav` depuis `src\resources\`
2. Trouvez votre serveur/dossier de sauvegarde du monde
3. Remplacez le `LocalData.sav` existant par le fichier copié
4. Lancez le jeu avec une carte entièrement débloquée

> **Remarque :** Utilisez l'option **Outils → Restaurer la carte** dans PST pour appliquer la carte déverrouillée à TOUS vos mondes/serveurs à la fois avec des sauvegardes automatiques.

</détails>

### Hôte → Transfert de serveur

<détails>
<summary>Cliquez pour développer le guide de transfert d'hôte à serveur</summary>

1. Copiez les dossiers `Level.sav` et `Players` depuis la sauvegarde de l'hôte
2. Coller dans le dossier de sauvegarde dedicated server
3. Démarrer le serveur, créer un nouveau personnage
4. Attendez la sauvegarde automatique, puis fermez
5. Utilisez **Fix Host Save** pour migrer GUIDs
6. Copiez les fichiers et lancez

**Utilisation de Fix Host Save :**
- Sélectionnez le `Level.sav` dans votre dossier temporaire
- Choisissez l'**ancien personnage** (depuis la sauvegarde d'origine)
- Choisissez le **nouveau personnage** (que vous venez de créer)
- Cliquez sur **Migrer**

</détails>

### Échange d'hôte (changement d'hôte)

<détails>
<summary>Cliquez pour développer le guide d'échange d'hôte</summary>

**Arrière-plan:**
- L'hôte utilise toujours « 0001.sav » — même UID pour celui qui héberge
- Chaque client utilise une sauvegarde UID régulière unique (par exemple, `123xxx.sav`, `987xxx.sav`)

**Prérequis :**
Les deux joueurs (ancien hôte et nouvel hôte) doivent avoir leurs sauvegardes régulières générées. Cela se produit en rejoignant le monde de l'hôte et en créant un nouveau personnage.

**Mesures:**

1. **Assurez-vous que des sauvegardes régulières existent**
   - Le joueur A (ancien hôte) doit avoir une sauvegarde régulière (par exemple, `123xxx.sav`)
   - Le joueur B (nouvel hôte) doit avoir une sauvegarde régulière (par exemple, `987xxx.sav`)

2. ** Remplacez la sauvegarde de l'hôte de l'ancien hôte par une sauvegarde régulière **
   - Utilisez PalworldSaveTools **Fix Host Save** pour échanger :
   - `0001.sav` de l'ancien hôte → `123xxx.sav`
   - (Cela déplace la progression de l'ancien hôte de l'emplacement d'hôte vers son emplacement de joueur habituel)

3. ** Remplacez la sauvegarde régulière du nouvel hôte par la sauvegarde de l'hôte **
   - Utilisez PalworldSaveTools **Fix Host Save** pour échanger :
   - `987xxx.sav` du nouvel hôte → `0001.sav`
   - (Cela déplace la progression du nouvel hôte vers l'emplacement de l'hôte)

**Résultat:**
- Le joueur B est désormais l'hôte avec son propre personnage et ses amis dans « 0001.sav ».
- Le joueur A devient client avec sa progression d'origine dans `123xxx.sav`

</détails>

### Exportation/Importation de base

<détails>
<summary>Cliquez pour développer le guide d'exportation/importation de base</summary>

**Exportation d'une base :**
1. Chargez votre sauvegarde dans PST
2. Allez dans l'onglet Bases
3. Cliquez avec le bouton droit sur une base → Exporter la base
4. Enregistrer sous le fichier `.json`

**Importation d'une base :**
1. Accédez à l'onglet Bases ou à la visionneuse de carte de base.
2. Faites un clic droit sur la guilde dans laquelle vous souhaitez importer la base
3. Sélectionnez la base d'importation
4. Sélectionnez votre fichier `.json` exporté

**Clonage d'une base :**
1. Cliquez avec le bouton droit sur une base → Cloner la base
2. Sélectionnez la guilde cible
3. La base sera clonée avec un positionnement décalé

**Ajustement du rayon de base :**
1. Cliquez avec le bouton droit sur une base → Ajuster le rayon
2. Entrez un nouveau rayon (50% - 1000%)
3. Enregistrez et chargez la sauvegarde dans le jeu pour les structures à réaffecter

</détails>

---

## Troubleshooting

### "VCRUNTIME140.dll est introuvable"

**Solution:** Install [Microsoft Visual C++ Redistributable](https://learn.microsoft.com/en-us/cpp/windows/latest-supported-vc-redist?view=msvc-170#latest-microsoft-visual-c-redistributable-version)

### `struct.error` when parsing save

**Cause :** Format de fichier de sauvegarde obsolète

**Solution:**
1. Chargez la sauvegarde dans le jeu (mode Solo, Coop ou Serveur dédié)
2. Cela déclenche une mise à jour automatique de la structure
3. Assurez-vous que la sauvegarde a été mise à jour avec ou après le dernier patch du jeu.

### Le convertisseur GamePass ne fonctionne pas

**Solution:**
1. Fermez la version GamePass de Palworld
2. Attends quelques minutes
3. Exécutez le convertisseur Steam → GamePass
4. Lancez Palworld sur GamePass pour vérifier

---

## Construire à partir de la source

```bash
# Clone the repository
git clone https://github.com/deafdudecomputers/PalworldSaveTools.git

# Install dependencies
pip install -r requirements.txt

# Run the application
python start.py
```

Pour créer l'exécutable autonome, utilisez le script de construction :
```bash
python scripts/build.py
```

---

## Contributing

Les contributions sont les bienvenues ! N'hésitez pas à soumettre une Pull Request.

1. Forker le référentiel
2. Créez votre branche de fonctionnalités (`git checkout -b feature/AmazingFeature`)
3. Validez vos modifications (`git commit -m 'Add some AmazingFeature'`)
4. Push vers la branche (`git push origin feature/AmazingFeature`)
5. Ouvrir une demande de tirage

---

## Clause de non-responsabilité

**Utilisez cet outil à vos propres risques. Sauvegardez toujours vos fichiers de sauvegarde avant d'apporter des modifications.**

Les développeurs ne sont pas responsables de toute perte de données de sauvegarde ou des problèmes pouvant résulter de l'utilisation de cet outil.

---

## Soutien

- **Discord :** [Join us for support, base builds, and more!](https://discord.gg/sYcZwcT4cT)
- **GitHub Problèmes :** [Report a bug](https://github.com/deafdudecomputers/PalworldSaveTools/issues)
- **Documentation:** [Wiki](https://github.com/deafdudecomputers/PalworldSaveTools/wiki) *(Currently in development)*

---

## Licence

Ce projet est sous licence MIT License - voir le fichier [LICENSE](LICENSE) pour plus de détails.

---

## Remerciements

- **Palworld** developed by Pocketpair, Inc.
- Merci à tous les contributeurs et membres de la communauté qui ont contribué à améliorer cet outil

---

<div align="center">

**Réalisé avec ❤️ pour la communauté Palworld**

[⬆ Retour en haut](#palworldsavetools)

</div>
