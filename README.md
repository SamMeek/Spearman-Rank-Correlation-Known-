📊 Spearman Rank Correlation Calculator

A simple **Streamlit** web application to calculate the **Spearman Rank Correlation Coefficient** from a CSV file containing two ranked variables A and B only.

![Python](https://img.shields.io/badge/Python-3.x-blue?logo=python)
![Streamlit](https://img.shields.io/badge/Streamlit-App-red?logo=streamlit)
![License](https://img.shields.io/badge/License-MIT-green)

---

Full webapp snaps:

### Upload CSV
1. <img width="1920" height="1080" alt="1" src="https://github.com/user-attachments/assets/1bacb6cc-59f4-4237-8d58-9bd0459ed087" />

### Select CSV File
2. <img width="1920" height="1080" alt="2" src="https://github.com/user-attachments/assets/4184562f-4a0d-452f-971d-49fda3e0193e" />

### Result
3. <img width="1920" height="1080" alt="3" src="https://github.com/user-attachments/assets/48014456-f910-4e7d-923a-10408ead2028" />

---

## ✨ Features

- Upload CSV files directly from your browser.
- Automatically reads the uploaded dataset.
- Displays the uploaded data.
- Calculates the **Spearman Rank Correlation Coefficient** using the mathematical formula.
- Clean and responsive Streamlit interface.
- No external statistical libraries required for the calculation.

---

## 📋 CSV Format

The CSV file must contain exactly **two columns** named:

| A | B |
|---|---|
| 9 | 4 |
| 3 | 2 |
|10 |10 |
| 4 | 7 |
| 6 | 5 |

Example:

```csv
A,   B
9,   4
3,   2
10, 10
4,   7
6,   5
5,   9
8,   8
1,   1
2,   3
7,   6
```

---

## 🧮 Formula Used

The application computes Spearman's Rank Correlation using:

 \(\rho = 1 - \frac{6 \sum d^2}{n(n^2 - 1)}\)

Where:

- **d** = Difference between the two ranks
- **n** = Number of observations

---

## 🚀 Installation

Clone the repository:

```bash
git clone https://github.com/yourusername/Spearman-Rank-Correlation.git
```

Move into the project directory:

```bash
cd Spearman-Rank-Correlation
```

Install dependencies:

```bash
pip install -r requirements.txt
```

---

## ▶️ Run the Application

```bash
streamlit run app.py
```

The application will open automatically in your browser.

---

## 📦 Requirements

```text
streamlit
pandas
numpy
```

Or install manually:

```bash
pip install streamlit pandas numpy
```

---

## ⚙️ How It Works

1. Launch the Streamlit application.
2. Upload a CSV file containing columns **A** and **B**.
3. The application displays the uploaded dataset.
4. It computes the squared differences between corresponding ranks.
5. The Spearman Rank Correlation Coefficient is calculated and displayed instantly.

---

## 📈 Example Output

```
Spearman Rank Correlation is: 0.67
```

---

## 🛠 Technologies Used

- Python
- Streamlit
- NumPy
- Pandas

---

## 📜 License

This project is licensed under the MIT License.

---

## 👤 Author

**Samapan Mondal**

GitHub: https://github.com/SamMeek

---

⭐ If you found this project useful, consider giving it a star!
