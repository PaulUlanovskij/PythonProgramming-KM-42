import csv
import unicodedata
with open("Ado.csv", 'w', encoding="utf-8") as file:
    fieldnames = ["Song", "Year"]
    songs = [
        "初夏 - Shoka",
        "愛して愛して愛して - Aishite Aishite Aishite",
        "オールナイトレディオ - All Night Radio",
        "DIGNITY",
        "ギラギラ - Gira Gira",
        "神っぽいな - God-ish",
        "いばら - Ibara",
        "うっせぇわ - Usseewa",
        "ルル - RuLe",
        "逆光 (ウタ from ONE PIECE FILM RED)",
    ]
    years = [
        2024,
        2023,
        2024,
        2024,
        2022,
        2022,
        2023,
        2022,
        2024,
        2022,
    ]

    writer = csv.DictWriter(file, fieldnames=fieldnames)
    writer.writeheader()
    for elem in zip(songs, years):
        writer.writerow({'Song': elem[0], 'Year': elem[1]})

with open("Ado.csv", 'r', encoding="utf-8") as file:
    print(file.name)
    reader = csv.DictReader(file)
    max_song_length = 0

    song_length_diffs = []
    for line in reader:
        song = line['Song']

        real_length = sum(1+(unicodedata.east_asian_width(c) in "WF")
                          for c in song)
        song_length_diffs.append(len(song) - real_length)

        if max_song_length < real_length:
            max_song_length = real_length

    offsets = [max_song_length + 2, 0]
    for (header, offset) in zip(reader.fieldnames, offsets):
        print("{:<{}}".format(header, offset), end=' ')
    print()

    file.seek(0)
    reader.__next__()

    for (line, len) in zip(reader, song_length_diffs):
        print("{:<{}} : {}".format(line['Song'],
              max_song_length + len, line['Year']))
