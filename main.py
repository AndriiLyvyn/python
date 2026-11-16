#
#
#
# # Piersze zadanie
# print("Cześć, Python!")
# print("Witamy na studiach!")
# print("To moje pierwsze ćwiczenie")
#
# # Zadanie drugie
# name = "Andrii"
# age = 25
# city = "Warszawa"
#
# print(name)
# print(age)
# print(city)
#
# city = "Kraków"
#
# print(city)
#
#
# # Zadanie trzecie
# course_name = "Wprowadzenie do Pythona dla Data Science"
# student_count = 20
# temperature = 21.5
# class_started = True
#
# print(course_name, type(course_name))
# print(student_count, type(student_count))
# print(temperature, type(temperature))
# print(class_started, type(class_started))
#
#
#
# # Zadanie czwarte
# a = 17
# b = 5
#
# print("Suma:", a + b)
# print("Różnica:", a - b)
# print("Iloczyn:", a * b)
# print("Iloraz:", a / b)
# print("Dzielenie całkowite:", a // b)
# print("Reszta z dzielenia:", a % b)
#
#
# # Zadanie piąte
# temperature_c = 22
#
# temperature_f = temperature_c * 9 / 5 + 32
#
# print("Temperatura w stopniach Celsjusza:", temperature_c, "°C")
# print("Temperatura w stopniach Fahrenheita:", temperature_f, "°F")
#
# temperature_c = 0
#
# temperature_f = temperature_c * 9 / 5 + 32
#
# print("Nowa temperatura w stopniach Celsjusza:", temperature_c, "°C")
# print("Nowa temperatura w stopniach Fahrenheita:", temperature_f, "°F")
#
# # Zadanie szuste
#
# name = input("Podaj swoje imię: ")
# age = int(input("Podaj swój wiek: "))
#
# print("Cześć,", name + "!")
# print("Masz,", age, "lat.")
#
#
# # Zadanie 7
#
# city = "Warsaw"
#
# print(city)
# print(len(city))
# print(city.upper())
# print(city.lower())


#  # Zadanie 8
#
# label = "  Temperature  "
# print(label)
# text=f"Registered variable: {label.strip()}"
#
# print(text)

#  # Zadanie 9

# temperatures = [18, 20, 19, 22, 21]
#
# print(temperatures)
# print(len(temperatures))

#  # Zadanie 10

# temperatures = [18, 20, 19, 22, 21]
# print(temperatures)
# print(f"First measurement {temperatures[0]} ")
# print(f"Second measurement {temperatures[1]} ")
# print(f"Last measurement {temperatures[-1]} ")
#
# temperatures[1]=23
# print(temperatures)

#  # Zadanie 11

# scores = [12, 15, 14, 18]
# scores = [12, 15, 14, 18]
#
#
# scores.append(16)
#
# print(scores)
#
# print(scores[:3])
#
# print(scores[-2:])
#
# print(scores[1:3])

#  # Zadanie 12

#
# study_hours = [2, 3, 1, 4, 5]
#
#
# total = sum(study_hours)
#
#
# minimum = min(study_hours)
#
#
# maximum = max(study_hours)
#
#
# average = total / len(study_hours)
#
# print("Total study time:", total)
# print("Minimum value:", minimum)
# print("Maximum value:", maximum)
# print("Average study time:", average)

#  # Zadanie 13

# observed_temperature = 24
# target_temperature = 22
#
# print(observed_temperature> target_temperature)
# print(observed_temperature< target_temperature)
# print(observed_temperature== target_temperature)
# print(observed_temperature>= target_temperature)


# #  # Zadanie 14
# scores = [49, 50, 80, 90]
#
# for x in scores:
#     if(x>50):
#         print("Good job:)",x)
#     else:
#         print("Try again :(" ,x)
#

#  # Zadanie 15
# temperatures = [5, 10, 24, 25]
#
#
# for temperature in temperatures:
#     if temperature < 10:
#         print(temperature, "- Cold")
#     elif temperature >= 10 and temperature < 25:
#         print(temperature, "- Moderate")
#     else:
#         print(temperature, "- Warm")

#  # Zadanie 16

# humidity_values = [-5, 0, 65, 100, 120]
#
# for humidity in humidity_values:
#     if humidity >= 0 and humidity <= 100:
#         print(humidity, "- Poprawny pomiar")
#     else:
#         print(humidity, "- Niepoprawny pomiar")



# #   Zadanie 17
# allowed_categories = ["low", "medium", "high"]
#
# category = input("Wpisz kategorię: ")
#
# category = category.strip().lower()
#
# if category in allowed_categories:
#     print("Kategoria jest dozwolona")
# else:
#     print("Kategoria nie jest dozwolona")


# temperatures = [18, 20, 19, 22, 21]
#
# for tem in temperatures:
#     print("Temperatures -", tem)


# for number in range(1, 11):
#     square = number *number
#     print(number, "Kwadrat:", square)

# #   Zadanie 18
# sales = [10, 15, 8, 12, 5]
#
# total = 0
#
# for sale in sales:
#     total = total + sale
#
# average = total / len(sales)
#
# print("Suma sprzedaży:", total)
# print("Średnia sprzedaży:", average)


# #   Zadanie 19
# temperatures = [18, 25, 21, 27, 19, 25]
#
# count = 0
#
# for temperature in temperatures:
#     if temperature > 24:
#         count = count + 1
#
# print("Liczba temperatur większych niż 24:", count)


# #   Zadanie 20
#
# measurements = [12, -1, 15, 0, -3, 18]
#
# clean_measurements = []
#
# for measurement in measurements:
#     if measurement >= 0:
#         clean_measurements.append(measurement)
#
# print("Lista pierwotna:", measurements)
# print("Lista oczyszczona:", clean_measurements)
#
# average = sum(clean_measurements) / len(clean_measurements)
#
# print("Średnia:", average)



# #   Zadanie 21
# measurements = []
#
# while True:
#     measurement = int(input("Podaj pomiar (-1 kończy): "))
#
#     if measurement == -1:
#         break
#
#     measurements.append(measurement)
#
# print("Zebrane pomiary:", measurements)
# print("Liczba pomiarów:", len(measurements))
#
# if len(measurements) > 0:
#     average = sum(measurements) / len(measurements)
#     print("Średnia:", average)
# else:
#     print("Nie wprowadzono żadnych pomiarów")


# def greet_student(name):
#     return "Witaj, " + name + "!"
#
#
# greeting1 = greet_student("Jan")
# greeting2 = greet_student("Anna")
#
# print(greeting1)
# print(greeting2)



# def celsius_to_fahrenheit(celsius):
#     fahrenheit = celsius * 9 / 5 + 32
#     return fahrenheit
#
#
# print(celsius_to_fahrenheit(0))
# print(celsius_to_fahrenheit(20))
# print(celsius_to_fahrenheit(100))


# def calculate_mean(values):
#     if len(values) > 0:
#         mean = sum(values) / len(values)
#         return mean
#     else:
#         return None
#
#
# print(calculate_mean([2, 4, 6]))
# print(calculate_mean([5]))
# print(calculate_mean([]))

# values = [4, 9, 2, 11, 9]
# threshold = 8
#
# def values_above(values, threshold):
#     result = []
#
#     for value in values:
#         if value > threshold:
#             result.append(value)
#
#     return result
#
#
# print(values_above(values,threshold))


# def summarize(values):
#     if len(values) > 0:
#         result = {
#             "count": len(values),
#             "minimum": min(values),
#             "maximum": max(values),
#             "mean": sum(values) / len(values)
#         }
#     else:
#         result = {
#             "count": 0,
#             "minimum": None,
#             "maximum": None,
#             "mean": None
#         }
#
#     return result
#
#
# # Testowanie funkcji
# numbers1 = [3, 7, 5, 9]
# numbers2 = []
#
# summary1 = summarize(numbers1)
# summary2 = summarize(numbers2)
#
# print(summary1)
# print("Liczba elementów:", summary1["count"])
#
# print(summary2)
# print("Liczba elementów:", summary2["count"])


# def count_responses(responses):
#     counts = {
#         "yes": 0,
#         "no": 0,
#         "maybe": 0
#     }
#
#     for response in responses:
#         if response == "yes":
#             counts["yes"] += 1
#         elif response == "no":
#             counts["no"] += 1
#         elif response == "maybe":
#             counts["maybe"] += 1
#
#     return counts
#
#
# # Testowanie funkcji
# responses = ["yes", "no", "yes", "maybe", "no", "yes"]
#
# print(count_responses(responses))
# print(count_responses([]))