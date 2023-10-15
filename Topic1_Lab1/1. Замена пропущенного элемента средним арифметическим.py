numbers = [2, -93, -2, 8, None, -44, -1, -85, -14, 90, -22, -90, -100, -8, 38, -92, -45, 67, 53, 25]

# TODO заменить значение пропущенного элемента средним арифметическим

index_of_missing_item = 4
sum_of_numbers = sum(numbers[:index_of_missing_item]) + sum(numbers[index_of_missing_item + 1:])
average = sum_of_numbers / len(numbers)
numbers[index_of_missing_item] = average

print("Измененный список:", numbers)
