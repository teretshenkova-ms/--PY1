salary = 5000  # зарплата
spend = 6000  # траты
months = 10  # количество месяцев
increase = 0.03  # рост цен

need_money = 0  # количество денег, чтобы прожить 10 месяцев


for _ in range(months):
    need_money += spend - salary  # учёт доходов и расходов в текущем месяце
    spend *= 1 + increase  # увеличение расходов на следующий месяц

print(round(need_money))
