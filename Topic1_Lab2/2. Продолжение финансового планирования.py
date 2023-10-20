salary = 5000  # Ежемесячная зарплата
spend = 6000  # Траты за первый месяц
months = 10  # Количество месяцев, которое планируется протянуть без долгов
increase = 0.03  # Ежемесячный рост цен

money_capital = 0.0

for count_months in range(1, months + 1):
    if count_months != 1:
        spend *= (1.0 + increase)

    money_capital += spend - salary

print(f"Подушка безопасности, чтобы протянуть {months} месяцев без долгов:", round(money_capital))
