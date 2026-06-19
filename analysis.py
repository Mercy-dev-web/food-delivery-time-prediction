import pandas as pd

df = pd.read_csv("Food_delivery.csv")

from sklearn.preprocessing import LabelEncoder

le_vehicle = LabelEncoder()
df["Type_of_vehicle"] = le_vehicle.fit_transform(df["Type_of_vehicle"])

le_order = LabelEncoder()
df["Type_of_order"] = le_order.fit_transform(df["Type_of_order"])

from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression

df["distance"] = (
    (df["Restaurant_latitude"] - df["Delivery_location_latitude"])**2
    +
    (df["Restaurant_longitude"] - df["Delivery_location_longitude"])**2
) ** 0.5

X = df[[
    "Delivery_person_Age",
    "Delivery_person_Ratings",
    "distance",
    "Type_of_order",
    "Type_of_vehicle"
]]

y = df["Time_taken(min)"]

X_train, X_test, y_train, y_test = train_test_split(
    X, y,
    test_size=0.2,
    random_state=42
)

model = LinearRegression()

model.fit(X_train, y_train)

from sklearn.metrics import mean_absolute_error

y_pred = model.predict(X_test)

mae = mean_absolute_error(y_test, y_pred)

print(mae)

from sklearn.metrics import r2_score

r2 = r2_score(y_test, y_pred)
print(r2)
