per_cent = {'ТКБ': 5.6, 'СКБ': 5.9, 'ВТБ': 4.28, 'СБЕР': 4.0}
amount = float(input("Введите сумму"))
deposit = [rate*(amount/100) for rate in per_cent.values()]
deposit_max=max(deposit)
print(deposit)
print ("Максимальная сумма, которую вы можете заработать", deposit_max)
