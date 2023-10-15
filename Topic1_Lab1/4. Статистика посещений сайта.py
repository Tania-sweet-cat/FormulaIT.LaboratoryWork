users = ['user1', 'user2', 'user3', 'user1', 'user4', 'user2']

# TODO Добавьте словарь и замените в нем нулевые значения статисчикой посещений

visit_statistics = {
    "Общее количество": 0,
    "Уникальные посещения": 0
}
all_visits = len(users)
unique_visits = len(set(users))

visit_statistics["Общее количество"] = all_visits
visit_statistics["Уникальные посещения"] = unique_visits

print(visit_statistics)