money_capital = 20000  # Подушка безопасности
salary = 5000  # Ежемесячная зарплата
spend = 6000  # Траты за первый месяц
increase = 0.05  # Ежемесячный рост цен

count_months = 0

while money_capital + salary >= spend:
    count_months += 1
    if count_months != 1:
        spend *= (1.0 + increase)

    money_capital -= spend - salary


print("Количество месяцев, которое можно протянуть без долгов:", count_months)
