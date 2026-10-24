⚡ Electricity Bill Calculator

A simple and beginner-friendly Electricity Bill Calculator developed using Python. This project calculates an electricity bill based on the number of units consumed and applies an additional 5% tax when the bill amount is ₹5,000 or more.

The project helps beginners understand conditional statements, user input, arithmetic operations, and basic billing calculations in Python.

✨ Features
⚡ Unit-Based Bill Calculation: Calculates the electricity bill according to the units entered.
💰 Different Rates: Applies different per-unit rates based on electricity consumption.
🧾 Tax Calculation: Adds 5% tax when the bill amount reaches ₹5,000 or more.
📊 Final Bill Display: Displays the electricity bill, applicable tax, and final amount.
✅ Input Validation: Checks for negative unit values and displays an invalid units message.
🐍 Beginner-Friendly: Uses basic Python concepts and conditional statements.
🛠️ Technologies Used
Programming Language: Python 3
Interface: Command-Line Interface (CLI)
📋 Electricity Rates

The program uses the following electricity rates:

Electricity Units	Rate Per Unit
0–100 units	₹10
101–200 units	₹15
201–300 units	₹20
Above 300 units	₹25

Tax Policy: An additional 5% tax is applied when the calculated bill amount is ₹5,000 or more.

Note: The program applies the selected rate to all units consumed, rather than using separate rates for each consumption slab.

📋 Requirements

To run this project, you need:

Python 3 installed on your computer.
A code editor or terminal.
🚀 How to Run the Project
Step 1: Clone the Repository
bash
git clone YOUR_GITHUB_REPOSITORY_URL

Step 2: Navigate to the Project Folder
bash
cd YOUR_PROJECT_FOLDER

Step 3: Run the Python Program

If your Python file is named electricity_bill.py, run:

bash
python electricity_bill.py


Depending on your system, you may need to use:

bash
python3 electricity_bill.py


Note: Replace the example repository URL, folder name, and Python filename with your actual project details.

💻 Example Output
text
===== Electricity Bill Calculator =====

Enter your units: 350

Rate 25 per units
Your total bill is 8750

Your bill is greater than 5000.
Now we add 5 percent tax services.

The amount of tax that we add is 437.5

Now your final total bill is 9187.5

Example Calculation

For 350 electricity units:

Electricity Units: 350
Rate Per Unit: ₹25
Electricity Bill: 350 × 25 = ₹8,750
Additional Tax: ₹8,750 × 5% = ₹437.50
Final Bill: ₹9,187.50
🎯 Learning Objectives

Through this project, I practiced the following Python concepts:

Variables and user input using input().
Type conversion using int().
Conditional statements using if, elif, and else.
Comparison and logical operators.
Arithmetic operations.
Percentage and tax calculations.
Basic input validation.
Displaying calculated results using print().
🔮 Future Improvements

In the future, this project can be improved by adding:

More accurate validation for invalid inputs.
Slab-based electricity bill calculations.
Additional taxes and service charges.
Support for decimal unit values.
A graphical user interface (GUI).
Monthly bill history and report generation.
Permanent storage of billing records.
👨‍💻 Author

Your Name

Aspiring Python Developer | Learning and Building Python Projects

GitHub: My GitHub Profile
📄 License

This project is created for educational purposes and to improve Python programming skills.
