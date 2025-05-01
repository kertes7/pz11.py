# task 1

def high_scores(grades_list):
    high = [g for g in grades_list if g > 70]
    return high, len(high)

if __name__ == "__main__":
    grades_list = [85, 60, 90, 70, 55, 100, 40, 78]
    high_list, total_high = high_scores(grades_list)
    print("Оцінки > 70:", high_list)
    print("Кількість високих оцінок:", total_high)

#task 2


def filter_items_by_length(items, min_length=5):
    filtered = [item for item in items if len(item) >= min_length]
    return filtered, len(filtered)

if __name__ == "__main__":
    shopping_list = ["молоко", "хліб", "масло", "яйця", "сир", "яблука"]
    long_list, count_long = filter_items_by_length(shopping_list)
    print("Товари з назвою ≥5 символів:", long_list)
    print("Кількість таких товарів:", count_long)


#task 3

# duplicates.py

def find_duplicates_in_list(sequence):
    seen = set()
    dupes = set()
    for element in sequence:
        if element in seen:
            dupes.add(element)
        else:
            seen.add(element)
    return list(dupes)

if __name__ == "__main__":
    numbers = [1, 2, 3, 4, 3, 2, 5, 6, 5, 7]
    repeated = find_duplicates_in_list(numbers)
    print("Повторювані числа:", repeated)
