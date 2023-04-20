import streamlit as st
import pickle
import datetime
import numpy as np
#from flask import Flask,request,app,jsonify,url_for,render_template
import pandas as pd


##Load the model 
model = pickle.load(open('flight_fare_prediction.pkl','rb'))

def predict_flight_fare(Total_stop,Journey_day,Journey_month,Journey_year,dep_hours,dep_mintues,arr_hours,arr_mintues,
         dur_hour,dur_mint,
         type,
         Air_India,GoAir,IndiGo,Jet_Airways,Jet_Airways_Business,
         Multiple_carriers,Multiple_carriers_Premium_economy,SpiceJet,Trujet
         ,Vistara,Vistara_Premium_economy,
         S_Chennai,S_Delhi,S_Kolkata,S_Mumbai,
         D_Cochin,D_Delhi,D_Hyderabad,D_Kolkata,D_NewDelhi):
    
    prediction = model.predict([[Total_stop,Journey_day,Journey_month,Journey_year
           ,dep_hours,dep_mintues,
         arr_hours,arr_mintues,
         dur_hour,dur_mint,
         type,
         Air_India,GoAir,IndiGo,Jet_Airways,Jet_Airways_Business,
         Multiple_carriers,Multiple_carriers_Premium_economy,SpiceJet,Trujet
         ,Vistara,Vistara_Premium_economy,
         S_Chennai,S_Delhi,S_Kolkata,S_Mumbai,
         D_Cochin,D_Delhi,D_Hyderabad,D_Kolkata,D_NewDelhi]])
    
    prediction = np.round(prediction[0],2)
    return prediction
    

def main():
    #st.title("Flight Fare Prediction Website")
    html_template = """
    <h1 style='color: linear-gradient;'>FareFinder: Your Flight Fare Predictor</h1>
    <p>Fly with Confidence! Predict Your Flight Fares with Ease.</p>
"""
    st.markdown(html_template,unsafe_allow_html=True)

    col1, col2 = st.columns(2)

    # Date of Journey
    with col1:
        dep_date = st.date_input('Enter Departure Date', value=datetime.date.today(), min_value=datetime.date(1900, 1, 1), max_value=datetime.date(2100, 12, 31), key='departure_input')
        Journey_day = int(pd.to_datetime(dep_date, format="%Y-%m-%dT%H:%M").day)
        Journey_month = int(pd.to_datetime(dep_date, format ="%Y-%m-%dT%H:%M").month)
        Journey_year  = int(pd.to_datetime(dep_date,format="%Y-%m-%dT%H:%M").year)

    #Departure
    dep_hours = int(pd.to_datetime(dep_date, format="%Y-%m-%dT%H:%M").hour)
    dep_mintues = int(pd.to_datetime(dep_date, format="%Y-%m-%dT%H:%M").minute)

    #Arrival
    with col2:
        arr_date = st.date_input('Enter Arrival Date', value=datetime.date.today(), min_value=datetime.date(1900, 1, 1), max_value=datetime.date(2100, 12, 31), key='arrival_input')
        arr_hours = int(pd.to_datetime(arr_date, format="%Y-%m-%dT%H:%M").hour)
        arr_mintues = int(pd.to_datetime(arr_date, format="%Y-%m-%dT%H:%M").minute)    

    #Duration
    dur_hour = dep_hours - arr_hours
    dur_mint = dep_mintues - arr_mintues

    #print("Departure Date",dep_date)
    #print("Arrival Date",arr_date)
    #print("Duration hour",dur_hour)
    #print("Duration mintues",dur_mint)

    # Display the selected date
    #print(dep_date)
    #print(Journey_day)
    #print(Journey_month)
    #print(Journey_year)
    #print("Dep_hours",dep_hours)
    #print("Dep_mintues",dep_mintues)

    with col1:
        source_city_name = ['Banglore', 'Kolkata', 'Delhi', 'Chennai', 'Mumbai']
        destination_city_name = ['New Delhi', 'Banglore', 'Cochin', 'Kolkata', 'Delhi', 'Hyderabad']
        source = st.selectbox('Select a source city',source_city_name)

        if (source == 'Kolkata'):
            S_Kolkata = 1
            S_Delhi = 0
            S_Chennai = 0
            S_Mumbai = 0
   
        elif (source == 'Delhi'):
            S_Kolkata = 0
            S_Delhi = 1
            S_Chennai = 0
            S_Mumbai = 0

        elif (source == 'Chennai'):
            S_Kolkata = 0
            S_Delhi = 0
            S_Chennai = 1
            S_Mumbai = 0  

        elif (source == 'Mumbai'):
            S_Kolkata = 0
            S_Delhi = 0
            S_Chennai = 0
            S_Mumbai = 1

        else:
            S_Kolkata = 0
            S_Delhi = 0
            S_Chennai = 0
            S_Mumbai = 0        

    with col2:
        destination_city_name_updated = [option for option in destination_city_name if option != source]
        destination = st.selectbox('Select a detination city',destination_city_name_updated)

        if (destination == 'New Delhi'):
            D_NewDelhi = 1
            D_Cochin = 0
            D_Kolkata = 0
            D_Delhi = 0
            D_Hyderabad = 0
    
        elif (destination == 'Cochin'):
            D_NewDelhi = 0
            D_Cochin = 1
            D_Kolkata = 0
            D_Delhi = 0
            D_Hyderabad = 0

        elif (destination == 'Kolkata'):
            D_NewDelhi = 0
            D_Cochin = 0
            D_Kolkata = 1
            D_Delhi = 0
            D_Hyderabad = 0

        elif (destination == 'Delhi'):
            D_NewDelhi = 0
            D_Cochin = 0
            D_Kolkata = 0
            D_Delhi = 1
            D_Hyderabad = 0

        elif (destination == 'Hyderabad'):
            D_NewDelhi = 0
            D_Cochin = 0
            D_Kolkata = 0
            D_Delhi = 0
            D_Hyderabad = 1

        else:
            D_NewDelhi = 0
            D_Cochin = 0
            D_Kolkata = 0
            D_Delhi = 0
            D_Hyderabad = 0 
        
     #Selecting an airline
    airline = st.selectbox('Select an Airline',
                           ('IndiGo', 'Air India', 'Jet Airways', 'SpiceJet',
       'Multiple carriers', 'GoAir', 'Vistara', 'Air Asia',
       'Vistara Premium economy', 'Jet Airways Business',
       'Multiple carriers Premium economy', 'Trujet'))
    
    #Encode the airline option
    if (airline =='IndiGo'):
        IndiGo = 1
        Air_India = 0
        Jet_Airways = 0
        SpiceJet = 0
        Multiple_carriers = 0
        GoAir = 0
        Vistara = 0
        Vistara_Premium_economy = 0
        Jet_Airways_Business = 0
        Multiple_carriers_Premium_economy = 0
        Trujet = 0

    elif (airline=='Air India'):  
        IndiGo = 0
        Air_India = 1
        Jet_Airways = 0
        SpiceJet = 0
        Multiple_carriers = 0
        GoAir = 0
        Vistara = 0
        Vistara_Premium_economy = 0
        Jet_Airways_Business = 0
        Multiple_carriers_Premium_economy = 0
        Trujet = 0

    elif (airline=='Jet Airways'):  
        IndiGo = 0
        Air_India = 0
        Jet_Airways = 1
        SpiceJet = 0
        Multiple_carriers = 0
        GoAir = 0
        Vistara = 0
        Vistara_Premium_economy = 0
        Jet_Airways_Business = 0
        Multiple_carriers_Premium_economy = 0
        Trujet = 0   

    elif (airline=='SpiceJet'):  
        IndiGo = 0
        Air_India = 0
        Jet_Airways = 0
        SpiceJet = 1
        Multiple_carriers = 0
        GoAir = 0
        Vistara = 0
        Vistara_Premium_economy = 0
        Jet_Airways_Business = 0
        Multiple_carriers_Premium_economy = 0
        Trujet = 0      

    elif (airline=='Multiple carriers'):  
        IndiGo = 0
        Air_India = 0
        Jet_Airways = 0
        SpiceJet = 0
        Multiple_carriers = 1
        GoAir = 0
        Vistara = 0
        Vistara_Premium_economy = 0
        Jet_Airways_Business = 0
        Multiple_carriers_Premium_economy = 0
        Trujet = 0 

    elif (airline=='GoAir'):  
        IndiGo = 0
        Air_India = 0
        Jet_Airways = 0
        SpiceJet = 0
        Multiple_carriers = 0
        GoAir = 1
        Vistara = 0
        Vistara_Premium_economy = 0
        Jet_Airways_Business = 0
        Multiple_carriers_Premium_economy = 0
        Trujet = 0      
    
    elif (airline=='Vistara'):  
        IndiGo = 0
        Air_India = 0
        Jet_Airways = 0
        SpiceJet = 0
        Multiple_carriers = 0
        GoAir = 0
        Vistara = 1
        Vistara_Premium_economy = 0
        Jet_Airways_Business = 0
        Multiple_carriers_Premium_economy = 0
        Trujet = 0 

    elif (airline=='Vistara Premium economy'):  
        IndiGo = 0
        Air_India = 0
        Jet_Airways = 0
        SpiceJet = 0
        Multiple_carriers = 0
        GoAir = 0
        Vistara = 0
        Vistara_Premium_economy = 1
        Jet_Airways_Business = 0
        Multiple_carriers_Premium_economy = 0
        Trujet = 0 
 
    elif (airline=='Multiple carriers Premium economy'):  
        IndiGo = 0
        Air_India = 0
        Jet_Airways = 0
        SpiceJet = 0
        Multiple_carriers = 0
        GoAir = 0
        Vistara = 0
        Vistara_Premium_economy = 0
        Jet_Airways_Business = 0
        Multiple_carriers_Premium_economy = 1
        Trujet = 0  
          
    elif (airline=='Jet Airways Business'):  
        IndiGo = 0
        Air_India = 0
        Jet_Airways = 0
        SpiceJet = 0
        Multiple_carriers = 0
        GoAir = 0
        Vistara = 0
        Vistara_Premium_economy = 0
        Jet_Airways_Business = 1
        Multiple_carriers_Premium_economy = 0
        Trujet = 0  

    elif (airline=='Trujet'):  
        IndiGo = 0
        Air_India = 0
        Jet_Airways = 0
        SpiceJet = 0
        Multiple_carriers = 0
        GoAir = 0
        Vistara = 0
        Vistara_Premium_economy = 0
        Jet_Airways_Business = 0
        Multiple_carriers_Premium_economy = 0
        Trujet = 1

    else:  
        IndiGo = 0
        Air_India = 0
        Jet_Airways = 0
        SpiceJet = 0
        Multiple_carriers = 0
        GoAir = 0
        Vistara = 0
        Vistara_Premium_economy = 0
        Jet_Airways_Business = 0
        Multiple_carriers_Premium_economy = 0
        Trujet = 0        

    with col1:        
        stop = st.selectbox("Enter no.of stops",('non-stop', '1 stop', '2 stops', '3 stops','4 stops'))

        if (stop == 'non_stop'):
            Total_stop=0
        elif (stop == '1 stop'):
            Total_stop=1
        elif (stop == '2 stops'):
            Total_stop=2
        elif (stop == '3 stops'):
            Total_stop=3
        else:
            Total_stop=4        

    with col2:
        type = st.selectbox("Part of Day you want to travel",('Day','Night'))    

        if (type == 'Day'):
            type = 1
        else:
            type = 0              

    #print("____________________________________")
    #print([Total_stop,Journey_day,Journey_month,Journey_year
    #       ,dep_hours,dep_mintues,
    #      arr_hours,arr_mintues,
    #     dur_hour,dur_mint,
    #     type,
    #     Air_India,GoAir,IndiGo,Jet_Airways,Jet_Airways_Business,
    #     Multiple_carriers,Multiple_carriers_Premium_economy,SpiceJet,Trujet
    #     ,Vistara,Vistara_Premium_economy,
    #     S_Chennai,S_Delhi,S_Kolkata,S_Mumbai,
    #     D_Cochin,D_Delhi,D_Hyderabad,D_Kolkata,D_NewDelhi
    #    ])

    result =""
     
    if st.button('Predict'):
        result = predict_flight_fare(Total_stop,Journey_day,Journey_month,Journey_year,dep_hours,dep_mintues,arr_hours,arr_mintues,dur_hour,dur_mint,
         type,Air_India,GoAir,IndiGo,Jet_Airways,Jet_Airways_Business,Multiple_carriers,Multiple_carriers_Premium_economy,SpiceJet,Trujet
         ,Vistara,Vistara_Premium_economy,S_Chennai,S_Delhi,S_Kolkata,S_Mumbai,D_Cochin,D_Delhi,D_Hyderabad,D_Kolkata,D_NewDelhi)
    st.success("The price of the flight is {}: ".format(result))
    
    if st.button("About"):
        st.text("The model uses RandomForestRegressor as Algorithm Trained by UTKARSH SINGH")


if __name__=='__main__':
    main()    
    