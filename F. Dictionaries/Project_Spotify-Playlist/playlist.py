playlist = {
    'title': 'patagonia bus',
    'author': 'ronaldo',
    'songs': [
        {
            'title': 'song1',
            'artist': ['blue'],
            'duration': 2.5
        },
        {
            'title': 'song2',
            'artist': ['kitty', 'djcat'],
            'duration': 3.5
        },
        {
            'title': 'song3',
            'artist': ['garfield'],
            'duration': 5.25
        },
    ]
}

total_length = 0
for song in playlist['songs']:
    total_length += song['duration']
print(total_length)
