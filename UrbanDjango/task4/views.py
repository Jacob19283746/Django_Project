from django.shortcuts import render

# Create your views here

def exchange(request):
    coins = ['BTC-RUB', 'USDT-RUB', 'BTC-USDT', 'ETH-USDT', 'USDC-USDT']
    context = {
        'coins': coins
    }
    return render(request, 'exchange.html', context)

def cart(request):
    return render(request, 'cart.html')

def platform(request):
    return render(request, 'platform.html')
