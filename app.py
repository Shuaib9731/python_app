import tkinter as tk
from tkinter import messagebox
import numpy as np
from sklearn.linear_model import LinearRegression

class LinearRegressionGUI:
    def __init__(self, master):
        self.master = master
        self.master.title("Simple Linear Regression")
        
        # Labels and Entry widgets for X and Y values
        self.label_x = tk.Label(master, text="Enter X value:")
        self.label_x.grid(row=0, column=0, padx=10, pady=5, sticky="e")
        
        self.entry_x = tk.Entry(master)
        self.entry_x.grid(row=0, column=1, padx=10, pady=5)
        
        self.label_y = tk.Label(master, text="Enter Y value:")
        self.label_y.grid(row=1, column=0, padx=10, pady=5, sticky="e")
        
        self.entry_y = tk.Entry(master)
        self.entry_y.grid(row=1, column=1, padx=10, pady=5)
        
        # Buttons for training the model and making predictions
        self.train_button = tk.Button(master, text="Train Model", command=self.train_model)
        self.train_button.grid(row=2, columnspan=2, padx=10, pady=5)
        
        self.predict_button = tk.Button(master, text="Predict", command=self.predict)
        self.predict_button.grid(row=3, columnspan=2, padx=10, pady=5)
        
        # Initialize Linear Regression model and data
        self.model = LinearRegression()
        self.X = []
        self.y = []
        
    def train_model(self):
        try:
            # Extract X and Y values from the Entry widgets
            x = float(self.entry_x.get())
            y = float(self.entry_y.get())
            
            # Append X and Y values to the data lists
            self.X.append([x])
            self.y.append(y)
            
            # Convert data lists into numpy arrays
            X_train = np.array(self.X)
            y_train = np.array(self.y)
            
            # Train the Linear Regression model
            self.model.fit(X_train, y_train)
            messagebox.showinfo("Training", "Model trained successfully!")
            
        except ValueError:
            messagebox.showerror("Error", "Please enter valid numeric values for X and Y.")
    
    def predict(self):
        try:
            # Extract X value from the Entry widget
            x = float(self.entry_x.get())
            
            # Predict Y value using the trained model
            prediction = self.model.predict([[x]])
            messagebox.showinfo("Prediction", f"Predicted value for X={x}: {prediction[0]}")
            
        except ValueError:
            messagebox.showerror("Error", "Please enter a valid numeric value for X.")
        

def main():
    # Create the main Tkinter window and the LinearRegressionGUI instance
    root = tk.Tk()
    app = LinearRegressionGUI(root)
    root.mainloop()

if __name__ == "__main__":
    main()
