salary = 5000  # зарплата
spend = 6000  # траты
months = 10  # количество месяцев
increase = 0.03  # рост цен

need_money = 0  # количество денег, чтобы прожить 10 месяцев

for month in range(months):
    need_money += spend  # остаток для трат в начале месяца
    need_money -= salary  # остаток после зачисления зарплаты в конце месяца
    spend *= (1 + increase)

print(round(need_money))
