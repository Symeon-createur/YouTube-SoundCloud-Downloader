import os
import subprocess
import json
import shlex
import requests
from mutagen.mp3 import MP3
from mutagen.id3 import ID3, TIT2, TPE1, APIC

def check_yt_dlp():
    try:
        subprocess.run(["yt-dlp", "--version"], check=True, stdout=subprocess.DEVNULL)
        return True
    except FileNotFoundError:
        print("❌ yt-dlp n'est pas installé. Installe-le d'abord.")
        return False

def get_format_list(url):
    command = ['yt-dlp', '-F', url]
    result = subprocess.run(command, capture_output=True, text=True)
    print(result.stdout)
    return result.stdout

def extract_formats(output):
    formats = {}
    for line in output.splitlines():
        if line.strip().startswith('format') or not line.strip() or 'RESOLUTION' in line:
            continue
        parts = line.strip().split()
        if len(parts) >= 2 and parts[0].isdigit():
            format_id = parts[0]
            resolution = [s for s in parts if 'p' in s]
            if resolution and int(resolution[0].replace('p', '')) >= 720:
                formats[format_id] = ' '.join(parts[1:])
    return formats

def download_youtube_video(url, output_folder="downloads"):
    output = get_format_list(url)
    formats = extract_formats(output)
    
    if not formats:
        print("❌ Aucun format pertinent (720p ou plus) trouvé.")
        return
    
    print("📺 Formats vidéo disponibles :")
    for fid, desc in formats.items():
        print(f"{fid}: {desc}")
    
    video_format = input("🎞️ Entrez l'ID du format vidéo souhaité : ").strip()
    
    if 'video only' in formats.get(video_format, ''):
        print("🔇 Format vidéo sans audio détecté.")
        print("\n📢 Liste des formats audio disponibles :\n")
        for fid, desc in formats.items():
            if 'audio only' in desc:
                print(f"{fid}: {desc}")
        audio_format = input("\n🎧 Choisis un format audio à fusionner : ").strip()
        command = [
            "yt-dlp", "-f", f"{video_format}+{audio_format}",
            "-o", f"{output_folder}/%(title)s.%(ext)s", url
        ]
    else:
        command = [
            "yt-dlp", "-f", video_format,
            "-o", f"{output_folder}/%(title)s.%(ext)s", url
        ]

    try:
        subprocess.run(command, check=True)
        print("✅ Téléchargement terminé avec succès !")
    except subprocess.CalledProcessError:
        print("❌ Une erreur est survenue pendant le téléchargement.")

def download_soundcloud_playlist(playlist_url, output_folder="downloads"):
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    command = f'yt-dlp --extract-audio --audio-format mp3 -o "{output_folder}/%(title)s.%(ext)s" --write-info-json {playlist_url}'
    
    try:
        subprocess.run(shlex.split(command), check=True)
        print("✅ Téléchargement terminé !")
        add_metadata_to_mp3(output_folder)
    except subprocess.CalledProcessError as e:
        print(f"❌ Erreur : {e}")

def add_metadata_to_mp3(folder):
    for file in os.listdir(folder):
        if file.endswith(".json"):
            json_path = os.path.join(folder, file)
            mp3_file = json_path.replace(".info.json", ".mp3")
            if not os.path.exists(mp3_file):
                continue

            with open(json_path, "r", encoding="utf-8") as f:
                metadata = json.load(f)

            title = metadata.get("title", "Inconnu")
            artist = metadata.get("uploader", "Artiste inconnu")
            cover_url = metadata.get("thumbnail", "")

            print(f"🎵 Ajout des métadonnées : {title} - {artist}")

            audio = MP3(mp3_file, ID3=ID3)
            audio.tags = ID3()
            audio.tags.add(TIT2(encoding=3, text=title))
            audio.tags.add(TPE1(encoding=3, text=artist))

            if cover_url:
                try:
                    response = requests.get(cover_url)
                    if response.status_code == 200:
                        audio.tags.add(APIC(
                            encoding=3, mime="image/jpeg", type=3,
                            desc="Cover", data=response.content
                        ))
                        print("🖼️ Pochette ajoutée !")
                except Exception as e:
                    print(f"⚠️ Erreur pochette : {e}")
            audio.save()
            print(f"✅ Métadonnées ajoutées à {title}\n")

if __name__ == "__main__":
    if not check_yt_dlp():
        exit()

    print("=== Sélection de la source ===")
    print("1. 📺 Télécharger depuis YouTube")
    print("2. 🎧 Télécharger une playlist SoundCloud")
    choix = input("Entrez votre choix (1 ou 2) : ").strip()

    if choix == "1":
        url = input("Entrez l'URL de la vidéo YouTube : ")
        dossier = input("Nom du dossier de destination (défaut = downloads) : ") or "downloads"
        download_youtube_video(url, dossier)

    elif choix == "2":
        url = input("Entrez l'URL de la playlist SoundCloud : ")
        dossier = input("Nom du dossier de destination (défaut = downloads) : ") or "downloads"
        download_soundcloud_playlist(url, dossier)

    else:
        print("❌ Choix non valide.")
