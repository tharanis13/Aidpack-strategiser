ReliefPack: Maximizing Aid Delivery
Project Overview
The ReliefPack project implements the 0/1 Knapsack Problem to optimize the distribution of disaster relief supplies using a helicopter with a weight capacity of 1000 kg. The project aims to select the best combination of supplies to maximize the total value while adhering to the weight constraint. This approach helps in efficiently allocating resources during disaster relief operations.

Problem Statement
A relief organization needs to transport various supplies to a disaster area using a helicopter that has a maximum weight capacity of 1000 kg. Each supply item has a specific weight and value. The challenge is to select the combination of items that maximizes the total value of supplies without exceeding the weight limit of the helicopter.

Objective
Develop an algorithm to efficiently select the optimal combination of disaster relief supplies.
Maximize the total value of the selected items while staying within the weight limit of 1000 kg.
Ensure the most critical items are prioritized for delivery.
Features
Dynamic Programming (DP) solution to solve the 0/1 Knapsack Problem.
Efficient backtracking to identify the selected items for transport.
Clear display of selected items, total weight, and total value.
Installation
Clone the Repository:

bash
Copy code
git clone https://github.com/your-username/ReliefPack.git
cd ReliefPack
Install Dependencies (Python 3.x is required): If you're using a virtual environment, activate it. Then, install the necessary packages:

bash
Copy code
pip install -r requirements.txt
(Note: This project doesn't have any external dependencies, so this step can be skipped.)

Run the Code: To run the knapsack algorithm, simply execute the Python script:

bash
Copy code
python knapsack.py
Code Structure
knapsack.py: Contains the implementation of the 0/1 Knapsack Algorithm.
README.md: This file, providing project documentation.
Example Output
less
Copy code
Selected Items:
- Tents (Weight: 400, Value: 70)
- Medicine (Weight: 100, Value: 40)
- Food (Weight: 300, Value: 60)
- Water (Weight: 200, Value: 50)

Total Weight: 1000
Total Value: 220
Usage
Modify the list of items and their respective weights and values within the knapsack.py file.
Update the capacity variable to reflect different weight limits if needed.
Run the script to find the optimal selection of items.
