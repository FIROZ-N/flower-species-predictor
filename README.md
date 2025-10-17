````markdown
# Iris Species Predictor

A Streamlit web app that predicts the species of an Iris flower based on sepal and petal measurements using a trained Random Forest model.

---

## 🛠 Features

- Predicts the Iris species: **Setosa**, **Versicolor**, or **Virginica**.
- Simple and interactive web interface using Streamlit.
- Uses a pre-trained Random Forest Classifier for accurate predictions.

---

## 💻 Installation

1. **Clone the repository**:

```bash
git clone https://github.com/your-username/iris-species-predictor.git
cd iris-species-predictor
````

2. **Create a virtual environment (optional but recommended)**:

```bash
python -m venv venv
```

3. **Activate the virtual environment**:

* **Windows (PowerShell)**:

```powershell
venv\Scripts\Activate.ps1
```

* **Linux / MacOS**:

```bash
source venv/bin/activate
```

4. **Install dependencies**:

```bash
pip install -r requirements.txt
```

---

## 🚀 Usage

Run the Streamlit app:

```bash
streamlit run app.py
```

* Open the URL shown in the terminal (usually `http://localhost:8501`).
* Enter the **sepal length, sepal width, petal length, and petal width**.
* Click **Predict Species** to see the predicted Iris species.

---

## 📂 Project Structure

```
iris-species-predictor/
│
├─ app.py               # Streamlit app
├─ model/
│   └─ iris_model.pkl   # Pre-trained Random Forest model
└─ requirements.txt     # Python dependencies
```

---

## ⚙️ Dependencies

* Python 3.x
* Streamlit
* scikit-learn
* numpy
* pandas
* matplotlib
* seaborn

---

## 📝 Notes

* The model was trained on the **Iris dataset** from scikit-learn.
* Prediction output is mapped to the **actual species names** (`Setosa`, `Versicolor`, `Virginica`) for clarity.
* Streamlit form in `app.py` is used to take input values and display the prediction.

---

## 🔗 Author

**FIROZ MUHAMMED N** – [GitHub Profile](https://github.com/FIROZ-N)

```
```
