import json
import requests
import smtplib
import pandas as pd

url = "https://kereby-rentals-api.signifly.io/api/rentals"
sender_email = "aws.testing.clamd@gmail.com"
receiver_email = 'c.lamd24@gmail.com'
password = 'zgrlijzvrxjehkej'
territory = ["København N", "København Ø", "Frederiksberg"]


def lambda_handler(event, context):
    print('Start scrape')
    new_rentals = 0
    final_message = ''
    # Read the items from the JSON file
    try:
        with open("rentals.json", "r") as file:
            rentals = json.load(file)
    except FileNotFoundError:
        pass
    
    response = requests.get(url, timeout=100)
    
    if response.status_code == 200:
        data = response.json()
        for item in data:
            if "id" in item:
                # Check for items with 2 or 3 rooms:
                if item['rooms'] >= 2 or item['rooms'] <= 3:

                    # Check the right territory:
                    if any([item['address']['city'] == i for i in territory]):
                        
                        # Check the price:
                        if item['monthlyRent']['value'] < 10000:
                        
                            # Check if the item is not already in the dictionary
                            if item["id"] not in rentals:
                                new_rentals += 1
                                # Add the item to the dictionary
                                rentals[item["id"]] = item
                                
                                 # Send an email notification
                                message = f"New rental found: {item['title']}\nPrice: {item['monthlyRent']['value']}\nRooms: {item['rooms']}\nAvailable From: {item['accessibleFrom']}\n"
                                final_message = final_message + message
                                
        if new_rentals == 0:
            final_message = "No new rentals found"
            
        server = smtplib.SMTP("smtp.gmail.com", 587)
        server.starttls()
        server.login(sender_email, password)
        server.sendmail(sender_email, receiver_email, final_message.encode('utf-8'))
        server.quit()
        
        with open("rentals.json", "w") as file:
            json.dump(rentals, file, indent=4)
        return {
        'statusCode': 200,
        'body': json.dumps('Successful Scrape!')
        }
    
    else:
        return {
            'statusCode': 200,
            'body': json.dumps('Unsuccessful Scrape :(')
        }

lambda_handler(1,1)