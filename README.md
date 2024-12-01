# Soccer Player Value Prediction Web App

## Overview
This web application predicts the market value of a soccer 
player based on their age, games played, and goals scored. 
The model used for predictions is a linear regression model trained on a dataset of soccer player statistics.
## Model Limitations
Simplicity of the Model: The model used is a linear regression model, which may 
not capture more complex relationships between features and the target variable (market value).

Limited Features: The model only uses three features (age, games played, and goals scored), 
but the market value of a player is likely influenced by many other factors, such as position, team performance, and league level.

Training Data: The model was trained on a specific dataset of soccer player statistics, 
and its performance may vary when applied to players outside of the dataset.

Assumptions: The model assumes that age, games played, and goals scored are sufficient 
to predict the market value of a player, which may not be accurate in all cases.

## Running the App
### Installation Steps
Clone this repository to your local machine:

''' git clone <repo URL> '''

bash
Copy code
git clone <repository_url>
cd <repository_folder>
Set up a virtual environment (optional, but recommended):

bash
Copy code
python -m venv venv
Activate the virtual environment:

Windows:
bash
Copy code
venv\Scripts\activate
Mac/Linux:
bash
Copy code
source venv/bin/activate
Install the required dependencies:

bash
Copy code
pip install -r requirements.txt
Running the App
Ensure your virtual environment is activated (if you're using one).

Start the Flask development server by running the following command:

bash
Copy code
python app.py
Open a web browser and go to http://127.0.0.1:5000/ to use the app.

Input Instructions
Enter the age, games played, and goals scored of a player into the input fields on the web page.
Click the "Predict" button to get the predicted market value of the player.
