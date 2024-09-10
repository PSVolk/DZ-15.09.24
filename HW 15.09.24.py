import random
import threading


numbers = []

list_filled = False

lock = threading.Lock()

sum_result = 0
average_result = 0

def fill_list():
    global numbers, list_filled
    with lock:
        while len(numbers) < 10:
            numbers.append(random.randint(1, 100))
        list_filled = True

def calculate_sum():
    global sum_result, list_filled
    while not list_filled:
        continue
    with lock:
        sum_result = sum(numbers)
    print(f"The sum of the numbers is: {sum_result}")

def calculate_average():
    global average_result, list_filled
    while not list_filled:
        continue
    with lock:
        average_result = sum(numbers) / len(numbers)
    print(f"The average of the numbers is: {average_result}")


fill_list_thread = threading.Thread(target=fill_list)
calculate_sum_thread = threading.Thread(target=calculate_sum)
calculate_average_thread = threading.Thread(target=calculate_average)

fill_list_thread.start()
calculate_sum_thread.start()
calculate_average_thread.start()


fill_list_thread.join()
calculate_sum_thread.join()
calculate_average_thread.join()

print(f"The list of numbers is: {numbers}")
