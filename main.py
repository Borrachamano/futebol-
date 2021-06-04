time = list()
dados = dict()
gols = list()

while True:
	dados.clear()
	gols.clear()
	dados['nome'] = str(input('Nome: '))
	total = int(input(f'Total de partidas jogadas por {dados["nome"]}: '))
	for p in range(0, total):
		gols.append(int(input(f'Quntoa gols marcados na {p+1} partida? ')))
	dados['gols'] = gols[:]
	dados['total'] = sum(gols)
	time.append(dados.copy())
	while True:
		opc = str(input('Deseja continuar? (S/n): ')).strip().upper()
		if opc in 'SN':
			break
		print('Opção invalida. Tente novamente.')
	if opc == 'N':
		break

print('-' * 40)

print('cod', end=' ')
for k in dados.keys():
	print(f'{k:<15}', end='')

print()

print('-' * 40)

for p, j in enumerate(time):
	print(f'{p:>3}', end=' ')
	for v in j.values():
		print(f'{str(v):<15}', end='')
	print()

print('-' * 40)

while True:
	jog = int(input('Mostrat dados de qual jogador? (999 para sair): '))
	if jog == 999:
		break
	print('-' * 40)
	if jog >= 0 and jog < len(time):
		print(f'	- Dados do jogador {time[jog]["nome"]}: ')
		for p, g in enumerate(time[jog]['gols']):
			print(f'	- Na {p+1}* partida fez {g} gols.')
	else:
		print('Esse jogador não foi cadastrado.')
	print('-' * 40)

print('-' * 40)

print('<<< Encerrado >>>')

