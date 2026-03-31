# Smart Expense Tracker

A CLI-based AI application for intelligent personal expense classification and spending prediction, built in Python.

---

## What It Does

- **Add expenses** — enter an amount and description; the app automatically classifies it into a category (Food, Transport, Entertainment, Shopping, Health, Bills, or Other) using AI keyword matching
- **View expenses** — see all recorded expenses in a clean formatted table with dates and categories
- **Predict spending** — uses linear regression to forecast your next expense based on past patterns
- **Persistent storage** — all data is saved to a local JSON file and survives across sessions

---

## Project Structure

```
ai-expense-tracker/
├── main.py                  # Entry point — run this
├── cli/
│   └── menu.py              # CLI menu, user interaction, flow control
├── core/
│   ├── classifier.py        # Keyword-based AI expense classifier
│   └── predictor.py         # NumPy linear regression predictor
├── storage/
│   └── filehandler.py       # JSON file read/write, path resolution
├── utils/
│   └── validator.py         # Input validation (amount checks)
├── data/
│   └── expense.json         # Auto-created on first run
├── requirements.txt
└── README.md
```

---

## Requirements

- Python 3.8 or higher
- NumPy

No internet connection required. All data is stored locally.

---

## Setup and Installation

### Step 1 — Clone the repository

```bash
git clone https://github.com/aniket25bai11514/ai-expense-tracker.git
cd ai-expense-tracker
```

### Step 2 — (Optional) Create a virtual environment

```bash
python -m venv venv

# On Windows
venv\Scripts\activate

# On macOS / Linux
source venv/bin/activate
```

### Step 3 — Install dependencies

```bash
pip install -r requirements.txt
```

### Step 4 — Run the application

```bash
python main.py
```

---

## Usage

The app runs entirely in your terminal. After launching, you will see:

```
=== Smart Expense Tracker ===
1. Add Expense
2. View Expenses
3. Predict Spending
4. Help
5. Exit
```

### Adding an expense

```
Enter choice: 1
Enter amount (Rs): 250
Enter description: lunch at canteen
[Success] Added Rs. 250.00 under 'Food'.
```

The category is assigned automatically based on keywords in your description. No manual tagging needed.

### Viewing expenses

```
Enter choice: 2

#    Amount (Rs)  Date          Category        Description
--------------------------------------------------------------
1         250.00  2026-03-25    Food            lunch at canteen
2         120.00  2026-03-25    Transport       ola to college
3         499.00  2026-03-26    Shopping        amazon earphones
```

### Predicting next expense

```
Enter choice: 3
Predicted next expense: Rs. 412.67
```

Requires at least 2 recorded expenses. Prediction uses linear regression on the sequence of past amounts.

---

## Supported Expense Categories

| Category      | Example Keywords                              |
|---------------|-----------------------------------------------|
| Food          | food, lunch, dinner, zomato, swiggy, cafe     |
| Transport     | uber, ola, bus, metro, petrol, cab, flight    |
| Entertainment | movie, netflix, spotify, cinema, game         |
| Shopping      | amazon, flipkart, clothes, shoes, mall        |
| Health        | medicine, doctor, hospital, gym, pharmacy     |
| Bills         | electricity, rent, wifi, phone, recharge      |
| Other         | Anything that doesn't match above             |

---

## Technologies Used

- **Python 3.x** — core application language
- **NumPy** — linear regression for spending prediction
- **JSON** — lightweight local data persistence

---

## Error Handling

The application handles the following gracefully:

- Non-numeric or negative amount input
- Empty expense description
- Corrupt or missing JSON data file (starts fresh)
- Insufficient data for prediction (requires at least 2 records)
- Unexpected runtime errors at the menu level

---

## Author

**Aniket Sahu**  
Registration No: 25BAI11514  
B.Tech CSE (AI/ML) — VIT Bhopal University  

---

## License

Developed for academic purposes as part of CSA2001 — Fundamentals of AI and ML.