# calculator.py

def calculate_sum(numbers):
    """Calcula a soma de uma lista de números."""
    return sum(numbers)

def calculate_average(numbers):
    """Calcula a média de uma lista de números."""
    if not numbers:
        return 0
    return sum(numbers) / len(numbers)

def find_even_numbers(numbers):
    """Encontra números pares em uma lista."""
    return [num for num in numbers if num % 2 == 0]

if __name__ == "__main__":
    # Lista de exemplo
    numbers = [1, 2, 3, 4, 5, 6]

    print("Números:", numbers)
    print("Soma:", calculate_sum(numbers))
    print("Média:", calculate_average(numbers))
    print("Números pares:", find_even_numbers(numbers))
