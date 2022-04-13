import json
bankdata_string= '''{"accounts": [
        {
            "name":"John Smith",
            "account_number":"0001",
            "account_type":"Savings",
            "amount":"$100.00 TTD"
        },
        {
           "name":"Julie Johnson",
           "account_number":"0002",
           "account_type":"Chequing", 
           "amount":"$2000.00 TTD"
        },
        {
            "name":"Jim Douglas",
            "account_number":"0003",
            "account_type":"Chequing",
            "amount":"$400.00 TTD"
        },
        {
            "name":"Jade Jagpath",
            "account_number":"0004",
            "account_type":"Savings",
            "amount":"$5000.00 TTD"
        },
        {
            "name":"Bob Dawson",
            "account_number":"0005",
            "account_type":"Savings",
            "amount":"$500.00 TTD"
        }
    ]
}'''


data=json.loads(bankdata_string)
accountnumber=input("Enter A Account Number To Begin A Search: ")

for account in data['accounts']:
    if(account['account_number']==accountnumber):
        print("Your Account Details Are: \n")
        print("Name: " +account['name'])
        print("Account Number: " + account['account_number'])
        print("Account Type: " + account['account_type'])
        print("Balance Amount: " + account['amount'])