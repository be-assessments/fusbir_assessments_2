## Requirements Project Setup

- Python (Python 3.12.4)
- Visual Studio Code

## Installation
### Below is an example of installing and setting up your app.

1. Clone and open the repository in visual studio code:

```bash
git clone https://github.com/be-assessments/fusbir_assessment_2.git
cd fusbir_assessment_2
code .
```
2. Install django 
```bash
 pip install django
```
3. Run the app locally
```bash
python manage.py runserver
```

## Usage

Use this following endpoints to add transactions get the balances and spend points

## API Endpoints

### Get All Transactions
```bash
 /get_all
 ```
 #### Method: GET 
#### Response:
        [
            {
                "payer": "SHOPIFY",
                "points": 1000,
                "timestamp": "2024-07-02T14:00:00Z"
            },
            ...
        ]
 ### Add Transaction 
 ```bash  
 /add_transaction 
 ```
 #### Method: POST       
#### Request Body:        
            {
                "payer": "SHOPIFY",
                "points": 1000,
                "timestamp": "2024-07-02T14:00:00Z"
            }
#### Response:          
            {
                "message": "Transaction added"
            }
### Add Bulk Transactions
```bash
/add_bulk_transactions
```
 #### Method: POST   
#### Request Body:
        [
            {
                "payer": "SHOPIFY",
                "points": 1000,
                "timestamp": "2024-07-02T14:00:00Z"
            },
            ...
        ]
       
#### Response:
        {
            "message": "Bulk transactions added"
        }
### Spend Points
```bash
/spend
```
 #### Method: POST   
#### Request Body:
        {
            "points": 5000
        }
#### Response:        
        [
            {
                "payer": "SHOPIFY",
                "points": -1000
            },
            ...
        ]
### Get Balance
```bash
/balance
```
 #### Method: GET
#### Response:
        {
            "SHOPIFY": 3000,
            "EBAY": 500,
            ...
        }
