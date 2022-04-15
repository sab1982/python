money = float(input('Введите сумму вклада (рублей):'))
per_cent = {'ТКБ': 5.6, 'СКБ': 5.9, 'ВТБ': 4.28, 'СБЕР': 4.0}
banks = list(per_cent.keys())
percents = list(per_cent.values())
deposit = list()
deposit.append(int(money / 100 * float(percents[0])))
deposit.append(int(money / 100 * float(percents[1])))
deposit.append(int(money / 100 * float(percents[2])))
deposit.append(int(money / 100 * float(percents[3])))
print(f'\nДоход по депозиту составит:\n {banks[0]} банк - {deposit[0]} рублей (ставка {percents[0]} % годовых)'
      f'\n {banks[1]} банк - {deposit[1]} рублей (ставка {percents[1]} % годовых)'
      f'\n {banks[2]} банк - {deposit[2]} рублей (ставка {percents[2]} % годовых)'
      f'\n {banks[3]} банк - {deposit[3]} рублей (ставка {percents[3]} % годовых)\n')
print('Максимальная сумма, которую Вы можете заработать -', max(deposit), 'рублей')


