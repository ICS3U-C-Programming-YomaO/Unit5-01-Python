#!/usr/bin/env python3
# Created By: Yoma Ozoh
# Date: November, 2025
# This program converts celsius to fahrenheit


def fahrenheit():
    # Display message
    print("Welcome to the celsius to fahrenheit converter!")

    # Get temperature in Celsius (negative numbers allowed)
    celsius = float(input("Enter the temperature in Celsius: "))
    # Convert Celsius to Fahrenheit
    fahrenheit = (9 / 5) * celsius + 32

    # Display the result
    print("Temperature in Fahrenheit:", fahrenheit)

    # Thank you message

    print("Thank you for using the program")


def main():

    fahrenheit()


if __name__ == "__main__":

    main()
