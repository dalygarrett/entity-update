import csv
import requests

# API endpoint and parameters
BASE_URL = "https://api.yextapis.com/v2/accounts/{{accountId}}/entities/{{entityId}}"
API_KEY = "1d10e9c6c5527c0c0e00eb54b8acbfa4"
API_VERSION = "20230825"
HEADERS = {
    "Content-Type": "application/json"
}
BODY = {
    "c_publishPages": True
}

def make_api_call(account_id, entity_id):
    url = BASE_URL.replace("{{accountId}}", account_id).replace("{{entityId}}", entity_id)
    params = {
        "api_key": API_KEY,
        "v": API_VERSION
    }
    
    response = requests.put(url, json=BODY, params=params, headers=HEADERS)
    return response

def main():
    csv_file = "input.csv"  # Replace with your CSV file's path
    api_responses = []

    with open(csv_file, "r") as file:
        csv_reader = csv.reader(file)
        
        for row in csv_reader:
            if len(row) >= 2:
                account_id = row[0]
                entity_id = row[1]
                
                response = make_api_call(account_id, entity_id)
                
                response_data = {
                    "account_id": account_id,
                    "entity_id": entity_id,
                    "status_code": response.status_code
                }
                
                if response.status_code != 200:
                    response_data["response_content"] = response.text

                api_responses.append(response_data)

                print(f"API Response for Account ID {account_id} and Entity ID {entity_id}:")
                print(response.status_code)
                print(response.text)
                print("=" * 50)

    return api_responses

if __name__ == "__main__":
    api_responses = main()
    print("API Responses:")
    for response in api_responses:
        print(response)
