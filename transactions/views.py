from django.http import JsonResponse
from django.views import View
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
import json
from datetime import datetime

transactions = []
points_balance = {}

@method_decorator(csrf_exempt, name='dispatch')
class GetAllTransactionsView(View):
    def get(self, request):
        return JsonResponse(transactions, safe=False)

@method_decorator(csrf_exempt, name='dispatch')
class AddTransactionView(View):
    def post(self, request):
        data = json.loads(request.body)
        payer = data.get('payer')
        points = data.get('points')
        timestamp = data.get('timestamp')
        
        # Create and store the transaction
        transaction = {'payer': payer, 'points': points, 'timestamp': timestamp}
        transactions.append(transaction)

        # Update the points balance for the payer
        if payer in points_balance:
            points_balance[payer] += points
        else:
            points_balance[payer] = points

        return JsonResponse({'message': 'Transaction added'}, status=201)

@method_decorator(csrf_exempt, name='dispatch')
class AddBulkTransactionsView(View):
    def post(self, request):
        data = json.loads(request.body)
            
        for entry in data:
            payer = entry.get('payer')
            points = entry.get('points')
            timestamp = entry.get('timestamp')

            # Create and store each transaction
            transaction = {'payer': payer, 'points': points, 'timestamp': timestamp}
            transactions.append(transaction)

            # Update the points balance for the payer
            if payer in points_balance:
                points_balance[payer] += points
            else:
                points_balance[payer] = points

        return JsonResponse({'message': 'Bulk transactions added'}, status=201)

@method_decorator(csrf_exempt, name='dispatch')
class SpendPointsView(View):
    def post(self, request):
        data = json.loads(request.body)
        points_to_spend = data.get('points')
        spent = []
        total_spent = 0
        # Sort transactions by timestamp to spend the oldest points first
        sorted_transactions = sorted(transactions, key=lambda x: datetime.fromisoformat(x['timestamp'].replace("Z", "+00:00")))

        for transaction in sorted_transactions:
            # Check if spent all the spend ammount
            if total_spent >= points_to_spend:
                break
            
            payer = transaction['payer']
            available_points = transaction['points'] 
            total_points_of_payer = points_balance[payer]
            # Check if total points of payer is not zero
            if total_points_of_payer > 0:
                # Check if total points of payer is less than the transaction points 
                if total_points_of_payer < available_points:
                    spend_points = min(total_points_of_payer, points_to_spend - total_spent)
                else:
                    spend_points = min(available_points, points_to_spend - total_spent)
                points_balance[payer] -= spend_points
                total_spent += spend_points

                found = False
                # Update the spent points for each payer            
                for entry in spent:
                    if entry['payer'] == payer:
                        entry['points'] -= spend_points
                        found = True
                        break
                    
                if not found:
                    spent.append({'payer': payer, 'points': -spend_points})    
        
        return JsonResponse(spent, safe=False)

class GetBalanceView(View):
    def get(self, request):
        return JsonResponse(points_balance, safe=False)
