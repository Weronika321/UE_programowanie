def if_even(number: int) -> bool:
    return number % 2 == 0


result_2 = if_even(2)

print("Liczba parzysta" if result_2 else "Liczba nieparzysta")

result_3 = if_even(3)

print("Liczba parzysta" if result_3 else "Liczba nieparzysta")
