import os
import random
import statistics
import sys
import psycopg2
import pip
import random

# Generate a random 4-digit binary number
binary_number = ""

for i in range(4):
    binary_number += random.choice("01")

# Convert binary to decimal
decimal_number = int(binary_number, 2)

print("Random binary number:", binary_number)
print("Decimal equivalent:", decimal_number)


monday = ["GREEN", "YELLOW", "GREEN", "BROWN", "BLUE", "PINK", "BLUE", "YELLOW", "ORANGE", "CREAM", "ORANGE", "RED", "WHITE", "BLUE", "WHITE", "BLUE", "BLUE", "BLUE", "GREEN"]

tuesday = [
    "ARSH", "BROWN", "GREEN", "BROWN", "BLUE",
    "BLUE", "BLEW", "PINK", "PINK", "ORANGE",
    "ORANGE", "RED", "WHITE", "BLUE", "WHITE",
    "WHITE", "BLUE", "BLUE", "BLUE"
]

wednesday = [
    "GREEN", "YELLOW", "GREEN", "BROWN", "BLUE",
    "PINK", "RED", "YELLOW", "ORANGE", "RED",
    "ORANGE", "RED", "BLUE", "BLUE", "WHITE",
    "BLUE", "BLUE", "WHITE", "WHITE"
]

thursday = [
    "BLUE", "BLUE", "GREEN", "WHITE", "BLUE",
    "BROWN", "PINK", "YELLOW", "ORANGE", "CREAM",
    "ORANGE", "RED", "WHITE", "BLUE", "WHITE",
    "BLUE", "BLUE", "BLUE", "GREEN"
]

friday = [
    "GREEN", "WHITE", "GREEN", "BROWN", "BLUE",
    "BLUE", "BLACK", "WHITE", "ORANGE", "RED",
    "RED", "RED", "WHITE", "BLUE", "WHITE",
    "BLUE", "BLUE", "BLUE", "WHITE"
]

all_colours = monday + tuesday + wednesday + thursday + friday

all_colours =[
        "BLUE" if colour == "BLEW"
    else "ASH" if colour == "ARSH"
    else colour
    for colour in all_colours
]

print("All colors:", all_colours)
print("Total number of colours:", len(all_colours))

 # 1. Mean colour: the colour whose frequency is closest to the mean frequency
 
frequency = {}
for colour in all_colours:
    if colour in frequency:
        frequency[colour] += 1
    else:
        frequency[colour] = 1
        
print("Colour frequency:")

for colour, count in frequency.items():
    print(colour, ":", count)
    
from collections import Counter

frequency = Counter(all_colours)

print("COLOUR FREQUENCIES")

for colour, count in frequency.items():
    print(colour, ":", count)

frequencies = list(frequency.values())

mean = sum(frequencies) / len(frequencies)
mean_colour = min(frequency, key=lambda c: abs(frequency[c] - mean))
print("Total shirts: %d | distinct colours: %d" % (total, len(frequency)))
print("Frequencies:", dict(frequency.most_common()))
print("\n1. Mean frequency = %.2f -> mean colour: %s (%d)"
      % (mean, mean_colour, frequency[mean_colour]))

# 2. Most worn colour

mode_colour = frequency.most_common(1)[0]

print("Most worn colour:", mode_colour[0])
print("Frequency:", mode_colour[1])

# 3. Median colour: sort colours by frequency (name breaks ties), take middle

median = statistics.median(frequencies)

print("Median frequency:", median)

 # 4. Variance of the frequencies
frequencies = list(frequency.values())
variance = statistics.pvariance(frequencies)

print("Variance:", variance)

   # 5. Probability of red
total_colours = len(all_colours)

red_frequency = frequency["RED"]

probability_red = red_frequency / total_colours

print("Number of RED entries:", red_frequency)

print("Probability of RED:", probability_red)

print("Probability percentage:", probability_red * 100, "%")

def save_to_postgres(freq):

    try:
        # Connect to PostgreSQL
        conn = psycopg2.connect(
            host="localhost",
            database="bincom",
            user="postgres",
            password="YOUR_PASSWORD",
            port="5432"
        )

        cursor = conn.cursor()

        # Create table
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS colour_frequency (
                colour VARCHAR(50) PRIMARY KEY,
                frequency INTEGER NOT NULL
            )
        """)

        # Insert colour frequencies
        for colour, count in freq.items():

            cursor.execute("""
                INSERT INTO colour_frequency (colour, frequency)
                VALUES (%s, %s)
                ON CONFLICT (colour)
                DO UPDATE SET frequency = EXCLUDED.frequency
            """, (colour, count))

        # Save changes
        conn.commit()

        print("Colours successfully saved to PostgreSQL!")

        cursor.close()
        conn.close()

    except Exception as e:
        print("Database error:", e)


# Example data
frequency = {
    "BLUE": 31,
    "WHITE": 16,
    "GREEN": 10,
    "ORANGE": 9,
    "RED": 9,
    "BROWN": 6,
    "YELLOW": 5,
    "PINK": 5,
    "CREAM": 2,
    "ASH": 1,
    "BLACK": 1
}

save_to_postgres(frequency)


def recursive_search(numbers, target, index=0):

    # Base case: End of list
    if index >= len(numbers):
        return -1

    # Check if number is found
    if numbers[index] == target:
        return index

    # Recursive call
    return recursive_search(numbers, target, index + 1)


# Main program
numbers = [10, 20, 30, 40, 50, 60, 70, 80]

print("List:", numbers)

target = int(input("Enter a number to search for: "))

result = recursive_search(numbers, target)

if result != -1:
    print("Number found at index:", result)
else:
    print("Number not found in the list.")


# Generate a random 4-digit binary number
binary_number = ""

for i in range(4):
    binary_number += random.choice("01")

# Convert binary to decimal
decimal_number = int(binary_number, 2)

print("Random binary number:", binary_number)
print("Decimal equivalent:", decimal_number)


# Initialise the first two Fibonacci numbers
a = 0
b = 1

total = 0

print("First 50 Fibonacci numbers:")

for i in range(50):

    print(a, end=" ")

    # Add current number to total
    total += a

    # Generate next Fibonacci number
    a, b = b, a + b

print("\n\nSum of first 50 Fibonacci numbers:", total)
