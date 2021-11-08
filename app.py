from flask import Flask, request, render_template
# import sklearn
import pickle
import pandas as pd
app = Flask(__name__)

file = open("pickle/model.pkl","rb")
model = pickle.load(file)
file.close()

file = open("pickle/robust.pkl", "rb")
robust = pickle.load(file)
file.close()

file = open("pickle/label.pkl", "rb")
label = pickle.load(file)
label_country = label["country"]
label_year = label["year"]
file.close()


countries = ['Albania', 'Antigua and Barbuda', 'Argentina', 'Armenia', 'Aruba',
       'Australia', 'Austria', 'Azerbaijan', 'Bahamas', 'Bahrain',
       'Barbados', 'Belarus', 'Belgium', 'Belize',
       'Bosnia and Herzegovina', 'Brazil', 'Bulgaria', 'Cabo Verde',
       'Canada', 'Chile', 'Colombia', 'Costa Rica', 'Croatia', 'Cuba',
       'Cyprus', 'Czech Republic', 'Denmark', 'Dominica', 'Ecuador',
       'El Salvador', 'Estonia', 'Fiji', 'Finland', 'France', 'Georgia',
       'Germany', 'Greece', 'Grenada', 'Guatemala', 'Guyana', 'Hungary',
       'Iceland', 'Ireland', 'Israel', 'Italy', 'Jamaica', 'Japan',
       'Kazakhstan', 'Kiribati', 'Kuwait', 'Kyrgyzstan', 'Latvia',
       'Lithuania', 'Luxembourg', 'Macau', 'Maldives', 'Malta',
       'Mauritius', 'Mexico', 'Mongolia', 'Montenegro', 'Netherlands',
       'New Zealand', 'Nicaragua', 'Norway', 'Oman', 'Panama', 'Paraguay',
       'Philippines', 'Poland', 'Portugal', 'Puerto Rico', 'Qatar',
       'Republic of Korea', 'Romania', 'Russian Federation',
       'Saint Kitts and Nevis', 'Saint Lucia',
       'Saint Vincent and Grenadines', 'San Marino', 'Serbia',
       'Seychelles', 'Singapore', 'Slovakia', 'Slovenia', 'South Africa',
       'Spain', 'Sri Lanka', 'Suriname', 'Sweden', 'Switzerland',
       'Thailand', 'Trinidad and Tobago', 'Turkey', 'Turkmenistan',
       'Ukraine', 'United Arab Emirates', 'United Kingdom',
       'United States', 'Uruguay', 'Uzbekistan']

@app.route("/")
def index():
    return render_template("index.html",countries = countries)


@app.route("/predict", methods=["GET", "POST"])
def predict():
    if request.method == "POST":

        country = request.form["country"]
        year = int(request.form["year"])
        gender = int(request.form["gender"])
        age_group = int(request.form["age_group"])
        suicide_count = int(request.form["suicide_count"])
        population = int(request.form["population"])
        gdp_for_year = int(request.form["gdp_for_year"])
        gdp_per_capita = int(request.form["gdp_per_capita"])
        generation = int(request.form["generation"])
        
        country = label_country.transform([str(country)])[0]
        year = label_year.transform([year])[0]
        transformed_data = robust.transform([[suicide_count, population, gdp_for_year,gdp_per_capita]])
        suicide_count = float(transformed_data[0,0])
        population = float(transformed_data[0,1])
        gdp_for_year = float(transformed_data[0,2])
        gdp_per_capita = float(transformed_data[0,3])
        prediction = model.predict([[
                country ,      
                year,           
                gender ,             
                age_group ,          
                suicide_count ,       
                population ,         
                gdp_for_year ,      
                gdp_per_capita ,    
                generation       
        ]])
        
        output = round(prediction[0], 3)

        return render_template('index.html',countries = countries, prediction_text="Suicide Rate is {} / 100k population. ".format(output))

    return render_template("index.html",countries = countries)


if __name__ == "__main__":
    app.run(debug=True)