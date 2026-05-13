import os
import re
from moviepy.editor import VideoFileClip

# Chemin du dossier contenant les vidéos
video_folder = 'E:/meldDatabase/MELD-RAW/MELD.Raw/test/output_repeated_splits_test'  # Remplace par le chemin vers ton dossier
audio_folder = 'E:/meldDatabase/MELD-RAW/MELD.Raw/test/audio'  # Remplace par le chemin où tu veux sauvegarder les audios

# Créer le dossier audio s'il n'existe pas
os.makedirs(audio_folder, exist_ok=True)

# Expression régulière pour filtrer les fichiers au format .mp4 avec le motif spécifique
pattern = re.compile(r'.*_dia\d+_utt\d+\.mp4$')

# Boucle sur les fichiers vidéo dans le dossier
for filename in os.listdir(video_folder):
    if pattern.match(filename):  # Vérifie si le nom du fichier correspond au motif
        video_path = os.path.join(video_folder, filename)
        audio_filename = filename.rsplit('.', 1)[0] + '.wav'  # Change l'extension en .wav
        audio_path = os.path.join(audio_folder, audio_filename)
        
        # Charger la vidéo et extraire l'audio
        with VideoFileClip(video_path) as video:
            audio = video.audio
            audio.write_audiofile(audio_path)
        
        print(f'Converti {filename} en {audio_filename}')
