Power Curve Analysis Project

This project analyzes power output data from the activity.csv file and generates a power curve graph. The analysis involves sorting the power data in descending order using a custom bubble sort algorithm before plotting.

Project Structure

main.py: The main script that reads the data, sorts it using the bubble sort algorithm, and generates a power curve graph.
sort.py: Contains the implementation of the bubble sort algorithm used to sort power data.
load_data.py: A utility script to load data from a CSV file into a NumPy array.
activity.csv: The CSV file containing power output data. (Note: This file must be in the same directory as the scripts for the project to function correctly.)
Getting Started

Prerequisites
Ensure you have Python 3 installed on your system. You can download it from here.

This project also requires numpy and matplotlib. Instructions to install these are provided in the setup steps below.

Setup
Clone the repository to your local machine:
bash
Copy code
git clone <repository-url>
Navigate to the project directory:
bash
Copy code
cd <project-directory>
Create a virtual environment:
bash
Copy code
python3 -m venv venv
Activate the virtual environment:
On Windows:
bash
Copy code
.\venv\Scripts\activate
On macOS/Linux:
bash
Copy code
source venv/bin/activate
Install the required packages:
bash
Copy code
pip install numpy matplotlib
Running the Project

To execute the project and generate the power curve graph, run:

bash
Copy code
python main.py
After execution, the sorted power output data will be printed to the console, and a graph titled 'Power Curve' will be saved as power_curve.png in the project directory.

Contributing

Feel free to fork the repository and submit pull requests to contribute to the project.

License

This project is licensed under the MIT License - see the LICENSE file for details.

Remember to replace <repository-url> and <project-directory> with your actual repository URL and project directory name, respectively. Also, ensure you have a LICENSE file if you're referencing it in the README.
