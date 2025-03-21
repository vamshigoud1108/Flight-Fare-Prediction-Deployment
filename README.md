# Flight Fare Prediction-Deployment
![](https://media.istockphoto.com/id/155439315/photo/passenger-airplane-flying-above-clouds-during-sunset.jpg?s=612x612&w=0&k=20&c=LJWadbs3B-jSGJBVy9s0f8gZMHi2NvWFXa3VJ2lFcL0=)

## Project Overview
This project aims to predict flight fares based on various input parameters such as departure and arrival times, source, destination, number of stops, and airline preferences. It leverages machine learning to provide accurate fare estimates and is deployed using Render for real-time predictions.

## Live Demo
Check out the live application here.[Flight Fare Predictor](https://flight-fare-predictor-gmoy.onrender.com/)

## Dataset
The dataset contains flight details including:
- Airline
- Date of Journey
- Source
- Destination
- Route
- Duration
- Total Stops
- Additional Info
- Price(Target variable)

## Technologies Used
- **Frontend**: HTML, CSS
- **Backend**: Flask(Python)
- **Machine Learning**: Scikit-learn (for model training)
- **Deployment**: Render

## Folder Structure
```
Flight-Fare-Prediction-Deployment/
│-- static/                
│   │-- css
|       |-- style.css
|   |-- images                 
│-- templates/             
│   │-- index.html     
│-- Data_Train.xlsx   
│-- README.md          
│-- app.py       
│-- flight_fare_model.pkl 
│-- flight_fare_prediction.ipynb             
│-- requirements.txt         
```

## Model Training Process
1. Data Preprocessing
  - Handling Outliers
  - Encoded Categorical Features
2. Model Selection and Training
  - Trained multiple regression models
    - Decison Tree 
    - Random Forest 
    - Xgboost
  - Evaluated performance using MAE, MSE, RMSE and R² Score.
  - Selected the best-performing model on accuracy and generalization ability
3. Model Deployment
  - Tuned hyperparameters to enhance accuracy.
  - Saved the trained model using Joblib.
  - Built a Flask web application for real-time predictions.
  - Deployed the application using Render.

## Installation
### Prerequisites
Ensure you have Python installed along with the required dependencies.

### Install Dependencies
```
pip install -r requirements.txt
```

### Running the application
1. Clone the repository:
```
git clone https://github.com/your-username/flight-fare-prediction.git
```
2. Navigate to the project directory:
```
cd flight-fare-prediction
```
3. Run the Flask application:
```
python app.py
```
4. Open a web browser and navigate to:
```
 http://127.0.0.1:5000
 ```

## Usage 
- Enter flight details in the web form.
- Click the "Predict" button.
- The predicted flight fare will be displayed on the screen.

## Example Prediction
Example user input:
```bash
Departure Date & Time: 21-03-2025 09:30 
Arrival Date & Time: 22-03-2025 13:15
Source: Mumbai
Destination: Hyderabad
Stopage: 1
Airline: Air India
```
Output:
```
Expected flight fare: ₹ 14,229
```

## Important Disclaimer
This project is created for learning and demonstration purposes only. The predictions should not be used for actual financial or travel decisions.

## Future Improvements
- Improve model accuracy with additional features.
- Add more airlines and destinations.
- Implement real-time API integration for live fare updates.
- Deploy the application on additional cloud platforms.



