money_capital = 10000
salary = 5000
spend = 6000
increase = 0.05

month = 0  # количество месяцев, которое можно прожить

current_sum = money_capital

while current_sum >= 0:
    month_begin_sum = current_sum - spend  # остаток после трат в начале месяца
    if month_begin_sum >= 0:
        current_sum = month_begin_sum + salary  # остаток после зачисления зарплаты в конце месяца
        spend *= (1 + increase)
        month += 1
    else:
        current_sum = month_begin_sum

print(month)
