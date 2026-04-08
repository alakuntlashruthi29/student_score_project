# Step 1: Import libraries
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error, r2_score

# Step 2: Load dataset
from pandas.errors import EmptyDataError

def load_dataset():
    candidates = ["student_data.csv", "StudentsPerformance.csv"]
    last_error = None

    for path in candidates:
        try:
            df_candidate = pd.read_csv(path)
        except (EmptyDataError, FileNotFoundError) as e:
            print(f"Warning: \"{path}\" cannot be used ({e}). Trying next file.")
            last_error = e
            continue

        if df_candidate.empty:
            print(f"Warning: \"{path}\" is empty. Trying next file.")
            continue

        print(f"Loaded dataset from '{path}'.")
        return df_candidate

    raise FileNotFoundError(
        "No valid dataset found. Create a non-empty 'student_data.csv' or use 'StudentsPerformance.csv'."
    )


df = load_dataset()
print("Dataset Preview:\n", df.head())

# Step 3: Features and target
if set(["hours_studied", "sleep_hours", "attendance", "score"]).issubset(df.columns):
    X = df[["hours_studied", "sleep_hours", "attendance"]]
    y = df["score"]
elif set(["math score", "reading score", "writing score"]).issubset(df.columns):
    X = df[["reading score", "writing score"]]
    y = df["math score"]
    print("Using 'StudentsPerformance.csv' mapping: math score <- target, reading/writing <- features.")
else:
    raise ValueError(
        "Dataset has unsupported columns. Expected ['hours_studied','sleep_hours','attendance','score'] "
        "or ['math score','reading score','writing score'].")

# Step 4: Split data
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# Step 5: Train model
model = LinearRegression()
model.fit(X_train, y_train)

# Step 6: Predictions
y_pred = model.predict(X_test)

# Step 7: Evaluation
print("\nModel Performance:")
print("MAE:", mean_absolute_error(y_test, y_pred))
print("R2 Score:", r2_score(y_test, y_pred))

# Step 8: Predict new data
if set(["hours_studied", "sleep_hours", "attendance"]).issubset(df.columns):
    test_input = pd.DataFrame([[5, 7, 80]],
                              columns=["hours_studied", "sleep_hours", "attendance"])
    plot_x, plot_y = "hours_studied", "score"
    plot_title = "Study Hours vs Score"
    x_label, y_label = "Hours Studied", "Score"
else:
    test_input = pd.DataFrame([[75, 80]],
                              columns=["reading score", "writing score"])
    plot_x, plot_y = "reading score", "math score"
    plot_title = "Reading Score vs Math Score"
    x_label, y_label = "Reading Score", "Math Score"

prediction = model.predict(test_input)
print("\nPredicted Target:", prediction[0])

# Step 9: Visualization
plt.scatter(df[plot_x], df[plot_y])
plt.xlabel(x_label)
plt.ylabel(y_label)
plt.title(plot_title)
plt.show()