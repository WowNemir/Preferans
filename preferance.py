def calculate_results():
    print('Введите количество игроков:')

    n = int(input())
    players = {}
    for i in range(1, n+1): 
        
        print(f'Введите имя {i} игрока')
        
        name = input().strip()
        players[name] = {
        'rock': None,
        'bullet': None,
        'whists': {}
        }

    for name in players.keys():
        
        print(f'Введите гору игрока {name}')
        players[name]['rock'] = int(input())
        
        print(f'Введите пулю игрока {name}')
        players[name]['bullet'] = int(input())
        
        for enemy in players.keys()-{name}:
            print(f'Введите висты {name} на игрока {enemy}')
            players[name]['whists'][enemy] = int(input())

    min_rock = min([players[name]['rock'] for name in players.keys()])
    
    for name in players:
        players[name]['rock'] -= min_rock
    print([(name, players[name]['rock']) for name in players.keys()])

    for name in players.keys():
        diff_whists = players[name]['rock']*10/len(players)
        for enemy in players.keys()-{name}:
            players[enemy]['whists'][name] += diff_whists
    print(players)
    for name in players.keys():
        result = 0
        for enemy in players.keys()-{name}:
            result += players[name]['whists'][enemy] - players[enemy]['whists'][name]
            
        print(name, result)


if __name__ == '__main__':
    calculate_results()
