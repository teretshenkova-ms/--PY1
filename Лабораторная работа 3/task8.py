money_capital = 10000
salary = 5000
spend = 6000
increase = 0.05

month = 0  # количество месяцев, которое можно прожить


money_capital += - spend  # сначала списываются расходы
while money_capital >= 0:
    money_capital += salary  # потом зачисляется зарплата
    month += 1  # месяц прожит! новый месяц начался
    spend *= 1 + increase  # в новом месяце расходы возрастают
    money_capital -= spend  # списание расходов в новом месяце

print(month)
