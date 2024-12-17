# Python program for a math artifact
# Includes mean, median, mode calculator, visuals, and box-and-whisker plots

import numpy as np
import matplotlib.pyplot as plt
from collections import Counter

def calculate_statistics(data):
    """Calculates mean, median, and mode for the given data."""
    mean = np.mean(data)
    median = np.median(data)
    mode_data = Counter(data)
    mode = [key for key, val in mode_data.items() if val == max(mode_data.values())]
    
    return mean, median, mode

def display_statistics(mean, median, mode):
    """Displays the calculated statistics."""
    print("\n--- Statistics ---")
    print(f"Mean: {mean:.2f}")
    print(f"Median: {median}")
    print(f"Mode: {mode}")

def create_box_and_whisker_plot(data):
    """Creates and displays a box-and-whisker plot for the data."""
    plt.figure(figsize=(6, 4))
    plt.boxplot(data, vert=False, patch_artist=True, boxprops=dict(facecolor='lightblue'))
    plt.title("Box-and-Whisker Plot")
    plt.xlabel("Values")
    plt.show()

def create_histogram(data):
    """Creates and displays a histogram for the data."""
    plt.figure(figsize=(6, 4))
    plt.hist(data, bins=10, color='skyblue', edgecolor='black')
    plt.title("Histogram")
    plt.xlabel("Values")
    plt.ylabel("Frequency")
    plt.show()

def main():
    """Main program to handle user input and display results."""
    print("Welcome to the Math Artifact Tool!")
    
    # Get data from user
    user_input = input("Enter your data as a comma-separated list: ")
    data = list(map(float, user_input.split(',')))
    
    # Calculate statistics
    mean, median, mode = calculate_statistics(data)
    display_statistics(mean, median, mode)

    # Display visuals
    while True:
        print("\nChoose an option for visualization:")
        print("1. Box-and-Whisker Plot")
        print("2. Histogram")
        print("3. Exit")
        choice = input("Enter your choice (1/2/3): ")

        if choice == '1':
            create_box_and_whisker_plot(data)
        elif choice == '2':
            create_histogram(data)
        elif choice == '3':
            print("Exiting the program. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
