def make_album(artist, title):
    return {"artist": artist, "title": title}

while True:
    print("\nMasukkan informasi album (ketik 'q' untuk keluar):")
    artist = input("Nama Artis: ")
    if artist.lower() == 'q':
        break
    title = input("Judul Album: ")
    if title.lower() == 'q':
        break
    
    album = make_album(artist, title)
    print("Album yang dibuat:", album)