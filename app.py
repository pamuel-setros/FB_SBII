from flask import Flask, jsonify, render_template_string
import pandas as pd

app = Flask(__name__)

df = pd.read_csv('salesinfo.csv')

df['InvoiceDate'] = pd.to_datetime(df['InvoiceDate'])
df = df.sort_values('InvoiceDate')

df['running_total'] = df.groupby('Country')['running_total'].transform('max')

# Prepare data for the line chart (sum across all countries)
daily = df.groupby('InvoiceDate').agg({'running_total':'sum'}).reset_index()
daily['InvoiceDate'] = daily['InvoiceDate'].dt.strftime('%Y-%m-%d')

# Prepare data for the map (total by country)
country_sales = df.groupby('Country').agg({'running_total':'max'}).reset_index()

@app.route('/data')
def data():
    return jsonify({
        'line': daily.to_dict(orient='list'),
        'map': country_sales.to_dict(orient='list')
    })

@app.route('/')
def index():
    return render_template_string(open('index.html').read())

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
