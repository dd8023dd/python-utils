import requests

# 余额查询工具

if __name__ == '__main__':

    url = 'https://api.openai.com/dashboard/billing/credit_grants'
    api_key = "你的apikey"
    headers = {
        "Authorization": "Bearer " + api_key,
        "Content-Type": "application/json"
    }
    response = requests.get(url, headers=headers)
    print(response.text)




