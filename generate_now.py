import os
import random
import json

# Ścieżki do plików
genre_file = "genre.txt"
lyrics_folder = "../prompt_egs"

# Załaduj dane z JSON
with open("top_200_tags.json", "r", encoding="utf-8") as file:
    tags = json.load(file)

# Funkcja do losowania gatunku i cech muzycznych
def generate_random_genre():
    genres = random.sample(tags["genre"], 1)  # Jeden losowy gatunek
    instruments = random.sample(tags["instrument"], random.randint(3, 5))  # 3 do 5 instrumentów
    moods = random.sample(tags["mood"], 1)  # Jeden losowy nastrój
    gender = random.sample(tags["gender"], 1)  # Jedna losowa płeć
    timbre = random.sample(tags["timbre"], 1)  # Jedno losowe brzmienie

    return " ".join(genres + instruments + moods + gender + timbre)

# Funkcja do losowania pliku z tekstem piosenki
def get_random_lyrics_file():
    lyrics_files = [f for f in os.listdir(lyrics_folder) if f.endswith(".txt")]
    return os.path.join(lyrics_folder, random.choice(lyrics_files))

# Główna pętla wykonująca się 10 razy
for i in range(10):
    # Tworzenie losowego pliku genre.txt
    with open(genre_file, "w", encoding="utf-8") as f:
        f.write(generate_random_genre())

    # Pobranie losowego pliku lyrics.txt
    lyrics_file = get_random_lyrics_file()

    # Uruchomienie komendy
    os.system(f"python infer.py --cuda_idx 0 --stage1_model m-a-p/YuE-s1-7B-anneal-en-cot "
              f"--stage2_model m-a-p/YuE-s2-1B-general --genre_txt {genre_file} --lyrics_txt {lyrics_file} "
              f"--run_n_segments 2 --stage2_batch_size 4 --output_dir ../output --max_new_tokens 3000 "
              f"--repetition_penalty 1.1")
