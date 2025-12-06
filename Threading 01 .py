import os
import time
import threading

# Function to play the song
def play_song():
    print("song.mp3")

# Function to show lyrics
def show_lyrics():
    lyrics = [
        "🎶 Line 1: Tum hi ho...",
        "🎶 Line 2: Zindagi ab tum hi ho...",
        "🎶 Line 3: Chain bhi, mera dard bhi...",
        "🎶 Line 4: Meri aashiqui ab tum hi ho..."
    ]
    
    for line in lyrics:
        print(line)
        time.sleep(1)  # wait 3 seconds between lines

# Run both functions together
t1 = threading.Thread(target=play_song)
t2 = threading.Thread(target=show_lyrics)

t1.start()
t2.start()

t1.join()
t2.join()
