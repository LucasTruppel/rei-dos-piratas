dificuldade = {'1': 1200, '2': 900, '3': 600, '4': 400, '5': 200,}

mapa_matriz = [
['x','x','x','x','x','x','x','x','x','x','x','x','x','x','x','x','x','x','x','x','x','x','x','x','x','x','x','x','x','x','x','x','x','x','x','x','x','x','x','x','x','x'],
['x',' ',' ',' ',' ',' ',' ',' ',' ','x',' ','f','f',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ','r','r',' ','x',' ',' ',' ',' ',' ',' ',' ',' ','x'],
['x',' ',' ',' ',' ',' ',' ',' ','x',' ',' ',' ',' ',' ','r','r',' ',' ',' ',' ',' ',' ','c',' ','e','e',' ',' ',' ',' ',' ','r',' ','x',' ',' ',' ',' ',' ',' ',' ','x'],
['x',' ',' ',' ',' ',' ',' ','x',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ','e',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ','r',' ','x',' ',' ',' ',' ',' ',' ','x'],
['x',' ',' ',' ',' ',' ','x',' ',' ',' ',' ','a',' ','d',' ','d',' ','a',' ',' ',' ',' ',' ',' ',' ',' ',' ','e','b',' ',' ','r',' ',' ',' ','x',' ',' ',' ',' ',' ','x'],
['x',' ',' ',' ',' ','x',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ','a',' ','b',' ','e',' ',' ',' ',' ','r',' ',' ',' ',' ','x',' ',' ',' ',' ','x'],
['x',' ',' ',' ','x',' ','m',' ',' ','a',' ',' ',' ','f',' ',' ','c',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ','b',' ',' ','r','r',' ',' ',' ',' ','x',' ',' ',' ','x'],
['x',' ',' ','x',' ',' ',' ',' ','e',' ',' ',' ',' ','f',' ',' ',' ',' ',' ',' ','b',' ','m',' ',' ','a',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ','x',' ',' ','x'],
['x',' ','x',' ','a',' ','e','e',' ',' ',' ','b',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ','r','r',' ',' ',' ',' ',' ',' ',' ',' ','x',' ','x'],
['x','x',' ','e',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ','c',' ',' ',' ','a',' ',' ',' ','a',' ',' ',' ',' ',' ',' ',' ',' ','b',' ',' ',' ',' ',' ',' ','x','x'],
['x',' ','e',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ','a',' ',' ',' ','a',' ',' ',' ',' ',' ',' ',' ','a',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ','c',' ',' ',' ','x'],
['x',' ',' ',' ',' ','b',' ',' ',' ','a',' ','a',' ',' ',' ',' ',' ','r',' ',' ','a',' ',' ',' ','b',' ',' ',' ','a',' ',' ',' ','a',' ',' ',' ',' ',' ',' ',' ',' ','x'],
['x',' ',' ',' ',' ',' ',' ','b',' ',' ',' ',' ',' ',' ',' ',' ','r',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ','b',' ',' ',' ',' ','e',' ',' ','d',' ',' ','x'],
['x',' ',' ','c',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ','r',' ','x','x','x','x',' ',' ',' ',' ','r','r',' ',' ',' ',' ','e','e',' ',' ',' ',' ',' ',' ','x'],
['x',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ','d',' ',' ',' ',' ',' ','x',' ',' ',' ',' ','x',' ','r',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ','r',' ',' ','x'],
['x',' ',' ','c',' ',' ',' ','a',' ',' ',' ','e',' ','d',' ',' ',' ','x',' ',' ',' ',' ',' ',' ','x',' ','r','r',' ',' ',' ',' ',' ',' ',' ',' ','a',' ','r','r','r','x'],
['x',' ','e',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ','x',' ',' ',' ',' ',' ',' ',' ',' ','x',' ',' ','a',' ','a',' ',' ',' ',' ',' ',' ',' ',' ','f',' ','x'],
['x','e',' ','e','e',' ',' ','a',' ',' ',' ','b',' ',' ',' ','x',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ','x',' ','a',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ','f',' ','x'],
['x',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ','x',' ',' ',' ','x','x','x','x','x','x',' ',' ',' ','x',' ',' ',' ',' ',' ',' ','1',' ',' ',' ',' ',' ',' ','x'],
['x',' ','a',' ',' ',' ',' ',' ','a',' ','b',' ',' ','x',' ',' ',' ',' ','x','3',' ','4',' ','x',' ',' ',' ',' ','x','p',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ','x'],
['x',' ',' ',' ',' ',' ','r','r',' ',' ',' ',' ',' ','x',' ',' ',' ',' ','x',' ','t','t',' ','x',' ',' ',' ',' ','x',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ','x'],
['x',' ','r',' ',' ','r',' ',' ',' ',' ','e',' ',' ','x',' ',' ',' ',' ','x',' ',' ',' ',' ','x',' ',' ',' ',' ','x',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ','x'],
['x',' ',' ',' ','r',' ',' ',' ',' ',' ',' ',' ',' ','x',' ',' ',' ',' ','x',' ',' ',' ',' ','x',' ',' ',' ',' ','x',' ','a',' ',' ','a',' ',' ','a',' ','a',' ',' ','x'],
['x',' ',' ','r',' ',' ',' ','a',' ',' ',' ','a',' ',' ','x',' ',' ',' ','x','2',' ',' ','2','x',' ',' ',' ','x',' ','a',' ',' ','a',' ',' ','a',' ',' ','a',' ',' ','x'],
['x','r','r',' ',' ',' ',' ',' ','b',' ',' ',' ',' ',' ',' ','x',' ',' ',' ','x',' ',' ','x',' ',' ',' ','x','a',' ',' ','a',' ',' ','a',' ',' ','a',' ',' ','a',' ','x'],
['x',' ',' ',' ',' ',' ',' ',' ','e',' ',' ',' ',' ','a',' ',' ','x',' ',' ','x',' ',' ','x',' ',' ','x','f',' ',' ',' ',' ',' ',' ',' ',' ','a',' ','a',' ',' ',' ','x'],
['x',' ',' ',' ','a',' ',' ',' ',' ','b',' ',' ',' ',' ',' ',' ',' ','x',' ','x',' ',' ','x',' ','x','f',' ',' ',' ','f',' ',' ',' ',' ',' ',' ',' ','f',' ',' ',' ','x'],
['x',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ','x','x',' ',' ','x','x','f',' ',' ',' ',' ',' ','a',' ','a',' ',' ',' ','f','f',' ',' ',' ','x'],
['x',' ','m',' ','a',' ',' ',' ',' ',' ','a',' ','e','e','e',' ',' ',' ','a','x',' ',' ','x',' ',' ',' ',' ',' ','b',' ',' ',' ',' ',' ',' ',' ','f','f',' ',' ',' ','x'],
['x',' ',' ',' ',' ',' ',' ','c',' ',' ',' ',' ',' ',' ','a',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ','b',' ',' ',' ',' ','f','f',' ',' ','x'],
['x',' ','1',' ','b',' ',' ',' ',' ','f','f',' ',' ',' ',' ',' ',' ',' ','a',' ',' ',' ',' ',' ',' ','5',' ',' ','a',' ',' ',' ',' ',' ',' ',' ','a',' ',' ',' ',' ','x'],
['x',' ',' ',' ',' ','f','f','f',' ',' ',' ','f',' ',' ','b',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ','a',' ',' ',' ','f',' ',' ',' ',' ','x'],
['x','x',' ','a',' ','m',' ','f','f',' ',' ',' ','f',' ',' ',' ',' ',' ','a',' ','a',' ',' ',' ',' ',' ',' ',' ','a',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ','x','x'],
['x',' ','x',' ',' ',' ',' ',' ','f','f',' ',' ','f',' ',' ','a',' ',' ',' ',' ',' ',' ','a',' ','a',' ','a',' ',' ',' ',' ',' ','b',' ',' ',' ',' ','e',' ','x',' ','x'],
['x',' ',' ','x',' ','r',' ',' ',' ','f','f',' ',' ','f',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ','m',' ',' ','a',' ',' ',' ',' ',' ',' ','e','e',' ','x',' ',' ','x'],
['x',' ',' ',' ','x',' ','r',' ',' ',' ',' ',' ',' ','f',' ','a',' ','b',' ','b',' ',' ',' ',' ',' ',' ',' ','b',' ',' ',' ',' ',' ','e','e','e',' ','x',' ',' ',' ','x'],
['x',' ',' ',' ',' ','x',' ',' ',' ',' ','b',' ',' ','f',' ',' ',' ',' ',' ',' ',' ','b',' ','b',' ','b',' ',' ',' ',' ',' ',' ','e','e',' ',' ','x',' ',' ',' ',' ','x'],
['x',' ',' ',' ',' ',' ','x',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ','r','r',' ',' ',' ',' ',' ',' ',' ','e',' ',' ',' ','b',' ',' ','e',' ','x',' ',' ',' ',' ',' ','x'],
['x',' ',' ',' ',' ',' ',' ','x',' ',' ',' ',' ',' ','b',' ',' ',' ',' ','r','r','r',' ',' ',' ','a',' ',' ',' ',' ',' ',' ',' ','e',' ','x',' ',' ',' ',' ',' ',' ','x'],
['x',' ',' ',' ',' ',' ',' ',' ','x',' ','a',' ',' ',' ','b',' ',' ',' ','r',' ',' ','r','r','r',' ',' ',' ',' ','a',' ',' ',' ',' ','x',' ',' ',' ',' ',' ',' ',' ','x'],
['x',' ',' ',' ',' ',' ',' ',' ',' ','x',' ',' ',' ',' ',' ','r',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ','x',' ',' ',' ',' ',' ',' ',' ',' ','x'],
['x','x','x','x','x','x','x','x','x','x','x','x','x','x','x','x','x','x','x','x','x','x','x','x','x','x','x','x','x','x','x','x','x','x','x','x','x','x','x','x','x','x']
]
