def find_common_participants(first_group, second_group, separator=','):
    list_first_group = first_group.split(separator)
    list_second_group = second_group.split(separator)

    common_participants = list(set(list_first_group).intersection(list_second_group))
    common_participants.sort()
    return common_participants


participants_first_group = "Иванов|Петров|Сидоров"
participants_second_group = "Петров|Сидоров|Смирнов"

participants = find_common_participants(participants_first_group, participants_second_group)
print(f"Общие участники: {participants}.")
