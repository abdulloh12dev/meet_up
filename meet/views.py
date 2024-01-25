from django.shortcuts import render

def home_page(request):
    tickets = [
        {"tiket_name": "Marsga sayohat ", "price": 35000 ,  "description": "Xar kunlik" , "total": 6 },
        {"tiket_name": "yupiterga sayohat", "price": 25000 ,  "description": "Shanba-yakshanba" , "total": 8 },
    ]
    context = {
        "tickets" : tickets
    }
    return render(request , 'index.html' , context=context)
