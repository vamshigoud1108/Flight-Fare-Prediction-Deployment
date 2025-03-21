import flask
from flask import request,render_template
import joblib
import pandas as pd

app = flask.Flask(__name__)
model = joblib.load(open('flight_fare_model.pkl','rb'))


@app.route('/',methods=['GET','POST'])
def doPredict():
  if request.method == 'POST':
    try:
        # Departure Date
        dep_date = request.form['dep_date']
        dep_dt = pd.to_datetime(dep_date, format="%Y-%m-%dT%H:%M")
        journey_day = dep_dt.day
        journey_month = dep_dt.month
        dep_hour = dep_dt.hour
        dep_min = dep_dt.minute
        
        # Arrival Date
        arr_date = request.form['arr_date']
        arr_dt = pd.to_datetime(arr_date, format="%Y-%m-%dT%H:%M")
        arr_hour = arr_dt.hour
        arr_min = arr_dt.minute

        # Duration
        duration = arr_dt - dep_dt
        dur_hour = duration.total_seconds() // 3600 
        dur_min = (duration.total_seconds() % 3600) // 60 

        # Source
        source = request.form['source']
        if (source == 'Kolkata'):
            s_Kolkata = 1
            s_Delhi = 0
            s_Chennai = 0
            s_Mumbai = 0
        elif (source == 'Delhi'):
            s_Kolkata = 0
            s_Delhi = 1
            s_Chennai = 0
            s_Mumbai = 0

        elif (source == 'Chennai'):
            s_Kolkata = 0
            s_Delhi = 0
            s_Chennai = 1
            s_Mumbai = 0
        elif (source == 'Mumbai'):
            s_Kolkata = 0
            s_Delhi = 0
            s_Chennai = 0
            s_Mumbai = 1     
        else:
            s_Kolkata = 0
            s_Delhi = 0
            s_Chennai = 0
            s_Mumbai = 0

        # Destination
        destination = request.form['destination']
        if  (destination == 'New_Delhi'):
            d_New_Delhi = 1
            d_Cochin = 0
            d_Kolkata = 0
            d_Delhi = 0
            d_Hyderabad = 0
        elif (destination == 'Cochin'):
            d_New_Delhi = 0
            d_Cochin = 1
            d_Kolkata = 0
            d_Delhi = 0
            d_Hyderabad = 0     
        elif (destination == 'Kolkata'):
            d_New_Delhi = 0
            d_Cochin = 0
            d_Kolkata = 1
            d_Delhi = 0
            d_Hyderabad = 0
        elif (destination == 'Delhi'):
            d_New_Delhi = 0
            d_Cochin = 0
            d_Kolkata = 0
            d_Delhi = 1
            d_Hyderabad = 0
        elif (destination == 'Hyderabad'):
            d_New_Delhi = 0
            d_Cochin = 0
            d_Kolkata = 0
            d_Delhi = 0
            d_Hyderabad = 1
        else:
            d_New_Delhi = 0
            d_Cochin = 0
            d_Kolkata = 0
            d_Delhi = 0
            d_Hyderabad = 0
            
        # Total Stops
        total_stops = int(request.form['stops'])

        # Airline
        airline = request.form['airline']
        if(airline=='Jet Airways'):
            Jet_Airways = 1
            IndiGo = 0
            Air_India = 0
            Multiple_carriers = 0
            SpiceJet = 0
            Vistara = 0
            GoAir = 0
            Multiple_carriers_Premium_economy = 0
            Jet_Airways_Business = 0
            Vistara_Premium_economy = 0
            Trujet = 0 

        elif (airline=='IndiGo'):
            Jet_Airways = 0
            IndiGo = 1
            Air_India = 0
            Multiple_carriers = 0
            SpiceJet = 0
            Vistara = 0
            GoAir = 0
            Multiple_carriers_Premium_economy = 0
            Jet_Airways_Business = 0
            Vistara_Premium_economy = 0
            Trujet = 0 

        elif (airline=='Air India'):
            Jet_Airways = 0
            IndiGo = 0
            Air_India = 1
            Multiple_carriers = 0
            SpiceJet = 0
            Vistara = 0
            GoAir = 0
            Multiple_carriers_Premium_economy = 0
            Jet_Airways_Business = 0
            Vistara_Premium_economy = 0
            Trujet = 0 
                
        elif (airline=='Multiple carriers'):
            Jet_Airways = 0
            IndiGo = 0
            Air_India = 0
            Multiple_carriers = 1
            SpiceJet = 0
            Vistara = 0
            GoAir = 0
            Multiple_carriers_Premium_economy = 0
            Jet_Airways_Business = 0
            Vistara_Premium_economy = 0
            Trujet = 0 
                
        elif (airline=='SpiceJet'):
            Jet_Airways = 0
            IndiGo = 0
            Air_India = 0
            Multiple_carriers = 0
            SpiceJet = 1
            Vistara = 0
            GoAir = 0
            Multiple_carriers_Premium_economy = 0
            Jet_Airways_Business = 0
            Vistara_Premium_economy = 0
            Trujet = 0 
                
        elif (airline=='Vistara'):
            Jet_Airways = 0
            IndiGo = 0
            Air_India = 0
            Multiple_carriers = 0
            SpiceJet = 0
            Vistara = 1
            GoAir = 0
            Multiple_carriers_Premium_economy = 0
            Jet_Airways_Business = 0
            Vistara_Premium_economy = 0
            Trujet = 0

        elif (airline=='GoAir'):
            Jet_Airways = 0
            IndiGo = 0
            Air_India = 0
            Multiple_carriers = 0
            SpiceJet = 0
            Vistara = 0
            GoAir = 1
            Multiple_carriers_Premium_economy = 0
            Jet_Airways_Business = 0
            Vistara_Premium_economy = 0
            Trujet = 0

        elif (airline=='Multiple carriers Premium economy'):
            Jet_Airways = 0
            IndiGo = 0
            Air_India = 0
            Multiple_carriers = 0
            SpiceJet = 0
            Vistara = 0
            GoAir = 0
            Multiple_carriers_Premium_economy = 1
            Jet_Airways_Business = 0
            Vistara_Premium_economy = 0
            Trujet = 0

        elif (airline=='Jet Airways Business'):
            Jet_Airways = 0
            IndiGo = 0
            Air_India = 0
            Multiple_carriers = 0
            SpiceJet = 0
            Vistara = 0
            GoAir = 0
            Multiple_carriers_Premium_economy = 0
            Jet_Airways_Business = 1
            Vistara_Premium_economy = 0
            Trujet = 0

        elif (airline=='Vistara Premium economy'):
            Jet_Airways = 0
            IndiGo = 0
            Air_India = 0
            Multiple_carriers = 0
            SpiceJet = 0
            Vistara = 0
            GoAir = 0
            Multiple_carriers_Premium_economy = 0
            Jet_Airways_Business = 0
            Vistara_Premium_economy = 1
            Trujet = 0
                
        elif (airline=='Trujet'):
            Jet_Airways = 0
            IndiGo = 0
            Air_India = 0
            Multiple_carriers = 0
            SpiceJet = 0
            Vistara = 0
            GoAir = 0
            Multiple_carriers_Premium_economy = 0
            Jet_Airways_Business = 0
            Vistara_Premium_economy = 0
            Trujet = 1

        else:
            Jet_Airways = 0
            IndiGo = 0
            Air_India = 0
            Multiple_carriers = 0
            SpiceJet = 0
            Vistara = 0
            GoAir = 0
            Multiple_carriers_Premium_economy = 0
            Jet_Airways_Business = 0
            Vistara_Premium_economy = 0
            Trujet = 0

        # Features
        features = [
        journey_day,
        journey_month,
        dep_hour,
        dep_min,
        arr_hour,
        arr_min,
        dur_hour,
        dur_min,
        total_stops, 
        s_Kolkata,
        s_Delhi,
        s_Chennai,
        s_Mumbai,
        d_New_Delhi,
        d_Cochin,
        d_Kolkata,
        d_Delhi,
        d_Hyderabad,
        Jet_Airways,
        IndiGo,
        Air_India,
        Multiple_carriers,
        SpiceJet,
        Vistara,
        GoAir,
        Multiple_carriers_Premium_economy,
        Jet_Airways_Business,
        Vistara_Premium_economy,
        Trujet
        ]

        # Prediction
        prediction = model.predict([features])

        # Output
        output = round(prediction[0])

        return render_template('index.html',prediction = f'Expected flight fare: ₹{output}')

    except Exception as e:
            return f"Error: {str(e)}"
  
  return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)