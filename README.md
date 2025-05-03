# Téléchargeur Multimédia - Par Symeon

Ce projet vous permet de télécharger des vidéos et des musiques depuis plusieurs plateformes comme YouTube et SoundCloud. Il propose également des options pour télécharger uniquement l'audio ou la vidéo, ou bien les deux et les fusionner automatiquement. Ce script utilise `yt-dlp` pour gérer les téléchargements.

## Fonctionnalités

- **Téléchargement vidéo depuis YouTube** : Vous pouvez choisir la qualité de la vidéo et ajouter l'audio si nécessaire.
- **Téléchargement audio depuis SoundCloud** : Téléchargez les morceaux au format MP3 avec les métadonnées.
- **Fusion des formats vidéo et audio** : Si un format vidéo sans audio est téléchargé, le script vous propose de fusionner l'audio et la vidéo.
- **Interface en ligne de commande** : Simple et rapide, avec des options pour sélectionner la source et les formats de téléchargement.

## Prérequis

- Python 3.x
- `yt-dlp` : outil en ligne de commande pour télécharger des vidéos/audio.
- `ffmpeg` : utilisé pour fusionner l’audio et la vidéo.

## Installation

1. Clonez ce projet ou téléchargez le fichier ZIP :

```bash
git clone https://github.com/Symeon-createur/YouTube-SoundCloud-Downloader
cd YouTube-SoundCloud-Downloader
```

2. Installez les dépendances Python :

```bash
pip install -r requirements.txt
```

3. Installez `ffmpeg` :

- **Windows** :
  - Téléchargez la version statique ici : [https://www.gyan.dev/ffmpeg/builds/](https://www.gyan.dev/ffmpeg/builds/)
  - Extrayez l'archive.
  - Ajoutez le chemin du dossier `bin` à la variable d’environnement `PATH`.

- **Linux** :

```bash
sudo apt update && sudo apt install ffmpeg
```

- **macOS** (avec Homebrew) :

```bash
brew install ffmpeg
```

4. Lancez le script :

```bash
python install_and_run.py
```

## Commandes principales

1. **Télécharger une vidéo YouTube :** Entrez l'URL de la vidéo YouTube, choisissez la qualité de la vidéo, et optionnellement fusionnez l'audio.
2. **Télécharger une playlist SoundCloud :** Entrez l'URL de la playlist, et le script téléchargera tous les morceaux au format MP3 avec leurs métadonnées.
3. **Visitez mon GitHub :** Pour plus de projets et de mises à jour, consultez mon [GitHub](https://github.com/Symeon-createur).

## Aide

- Si vous rencontrez des problèmes, n'hésitez pas à consulter la [documentation de yt-dlp](https://github.com/yt-dlp/yt-dlp) pour plus d'informations.
- Pour toute autre question, vous pouvez ouvrir un problème sur [GitHub](https://github.com/Symeon-createur/YouTube-SoundCloud-Downloader/issues).

### Par Symeon
