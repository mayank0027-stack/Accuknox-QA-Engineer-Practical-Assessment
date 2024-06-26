import requests
import time

def check_application_status(url):
    try:
        response = requests.get(url)
        if response.status_code == 200:
            print(response)
            return "Application is up and running."
        else:
            return f"Application is down. Status code: {response.status_code}"
    except requests.exceptions.RequestException as e:
        return f"Error connecting to the application: {str(e)}"

if __name__ == "__main__":
    application_url = input("Enter the URL of the application to check: ")

    while True:
        status = check_application_status(application_url)
        print(status)
        time.sleep(60)  # Check status every 60 seconds
