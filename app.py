from flask import Flask, render_template, request, redirect, url_for, session
import joblib
import pandas as pd
import os

app = Flask(__name__, template_folder='src')
app.secret_key = 'your_secret_key'  # Needed for session handling

# Load your model using joblib

try:
    saved_model = joblib.load('Diamond-Price-Prediction-Model-Project-Final.pkl')
    print("Model loaded successfully.")
except Exception as e:
    print("Error loading model:", e)


@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        try:
            # Retrieve form data
            new_data = {
                'carat': [float(request.form['carat'])],
                'depth': [float(request.form['depth'])],
                'table': [float(request.form['table'])],
                'x': [float(request.form['x'])],
                'y': [float(request.form['y'])],
                'z': [float(request.form['z'])],
                'cut': [request.form['cut']],
                'color': [request.form['color']],
                'clarity': [request.form['clarity']]
            }
            
            # Convert the dictionary to a DataFrame
            new_data_df = pd.DataFrame(new_data)

            # Make predictions
            predictions = saved_model.predict(new_data_df)
            prediction_text = f'Predicted value: ${predictions[0]:.2f}'

            # Store prediction in session
            session['prediction_text'] = prediction_text
        except Exception as e:
            session['prediction_text'] = f"An error occurred: {str(e)}"
        
        # Redirect to the result route
        return redirect(url_for('result'))

    return render_template('form.html')

@app.route('/result', methods=['GET'])
def result():
    # Retrieve prediction text from session
    prediction_text = session.get('prediction_text', 'No prediction made.')
    return render_template('result.html', prediction_text=prediction_text)

if __name__ == "__main__":
    app.run(debug=True)
