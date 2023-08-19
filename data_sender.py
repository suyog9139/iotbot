import requests
import pandas as pd
import schedule
import time

def send_temperature_data():
    csv_file = 'IOT-temp.csv'
    url = 'http://localhost:8000/api/upload-temperature/'  # Change this URL if needed

    df = pd.read_csv(csv_file)
    temperature_values = df['temp'].tolist()

    # Send one temperature value
    if temperature_values:
        temperature = temperature_values.pop(0)
        data = {'temperature': temperature}
        response = requests.post(url, json=data)
        if response.status_code == 201:
            print('Temperature data sent successfully:', data)
        else:
            print('Failed to send temperature data:', data)

schedule.every(1).minutes.do(send_temperature_data)  # Send one temperature value per minute

while True:
    schedule.run_pending()
    time.sleep(1)
