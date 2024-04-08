# Power Curve Analysis Project

This project analyzes power output data from the `activity.csv` file and generates a power curve graph. The analysis involves sorting the power data in descending order using a custom bubble sort algorithm before plotting.

## Project Structure

- `main.py`: The main script that reads the data, sorts it using the bubble sort algorithm, and generates a power curve graph.
- `sort.py`: Contains the implementation of the bubble sort algorithm used to sort power data from High to low.
- `load_data.py`: A utility script to load data from a CSV file into a NumPy array.
- `activity.csv`: The CSV file containing power output data. (Note: This file must be in the same directory as the scripts for the project to function correctly.)

## Getting Started

### Prerequisites

Ensure you have Python 3 installed on your system. You can download it from [here](https://www.python.org/downloads/).

This project also requires `numpy` and `matplotlib`. Instructions to install these are provided in the setup steps below.

### Setup

1. Clone the repository to your local machine:

```bash
git clone (https://github.com/AlexKometer/Leistungskurve_1)
