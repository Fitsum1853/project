from flask import Flask, render_template, request
import pickle
import numpy as np

# Initialize Flask app
app = Flask(__name__)

# Load the trained model
model = pickle.load(open("data/soccer_model.pkl", "rb"))

@app.route('/')
def index():
    """
    Render the home page with the form for user input.
    """
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    """
    Handle the form submission, make predictions using the model, 
    and render the result page with the predicted value.
    """
    try:
        # Get user input from the form
        age = float(request.form['age'])
        games = float(request.form['games'])
        goals = float(request.form['goals'])

        # Prepare the input data for the model
        input_data = np.array([[age, games, goals]])

        # Make prediction (log-transformed value)
        log_prediction = model.predict(input_data)[0]

        # Convert log value back to original scale
        predicted_value = np.expm1(log_prediction)

        # Render the result template
        return render_template('result.html', predicted_value=predicted_value)

    except Exception as e:
        # Handle any errors that occur
        return f"An error occurred: {e}"

if __name__ == '__main__':
    # Run the Flask app
    app.run(debug=True)