import csv
import pandas as p
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score
from sklearn.preprocessing import StandardScaler

print("welcome week 2 project")
print(" step:1::::::::Setup of datas")
print("2::::::::::Training of model")
print("3:::::::::::User input")
c='y'
model = None
scaler = None  # Initialize scaler variable

while c == 'y':
    ch = int(input("enter choice: "))
    if ch == 1:
        # Data set
        data = [
            ['strength', 'intelligence', 'speed', 'agility', 'durability', 'superhero'],
            [8, 7, 6, 5, 9, 'Superman'],
            [5, 9, 4, 7, 6, 'Batman'],
            [6, 6, 9, 8, 5, 'Flash'],
            [7, 8, 5, 6, 7, 'Wonder Woman'],
            [9, 5, 7, 6, 8, 'Thor'],
            [4, 10, 3, 9, 4, 'Iron Man'],
            [7, 6, 8, 7, 6, 'Spider-Man'],
            [6, 7, 6, 8, 7, 'Black Panther'],
            [5, 8, 5, 9, 5, 'Captain America'],
            [8, 6, 7, 5, 8, 'Hulk'],
            [10, 10, 10, 10, 10, "God"]
        ]
        # Write operation
        with open('superhero.csv', 'w', newline='') as file:
            writer = csv.writer(file)
            writer.writerows(data)
        print("Expanded data written to superhero.csv")
    elif ch == 2:
        print("Model Training")
        data = p.read_csv("superhero.csv")
        x = data[['strength', 'intelligence', 'speed', 'agility', 'durability']]
        y = data['superhero']

        # Scale the data
        scaler = StandardScaler()
        x_scaled = scaler.fit_transform(x)

        x_train, x_test, y_train, y_test = train_test_split(x_scaled, y, test_size=0.2, random_state=42)
        model = LogisticRegression(max_iter=1000)
        model.fit(x_train, y_train)
        y_pred = model.predict(x_test)
        accuracy = accuracy_score(y_test, y_pred)
        print("Model training completed.")
    elif ch == 3:
        if model is not None and scaler is not None:
            strength = int(input("Rate your strength (1-10): "))
            intelligence = int(input("Rate your intelligence (1-10): "))
            speed = int(input("Rate your speed (1-10): "))
            agility = int(input("Rate your agility (1-10): "))
            durability = int(input("Rate your durability (1-10): "))
            traits = [[strength, intelligence, speed, agility, durability]]

            # Convert traits to DataFrame
            traits_df = p.DataFrame(traits, columns=['strength', 'intelligence', 'speed', 'agility', 'durability'])

            # Scale the input traits
            traits_scaled = scaler.transform(traits_df)

            prediction = model.predict(traits_scaled)
            print(f'Your superhero match is: {prediction[0]}')
        else:
            print("Model is not trained yet. Please train the model first by selecting option 2.")
    else:
        print("Input Error")
    c = input("do you want to continue (y/n): ").lower()
