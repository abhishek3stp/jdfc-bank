from django.shortcuts import render, redirect
from home.models import Contact, Customer, Transaction
from django.contrib import messages


# Create your views here.
def home(request):
    return render(request, 'home.html')


def customer(request):
    customers = Customer.objects.all()
    context = { "customers" : customers}
    return render(request, 'customer.html', context)


def form(request, slug):
    sender = Customer.objects.get(account_no = slug)
    details = Customer.objects.exclude(account_no = slug)
    context = { "sender" : sender, "details" : details}
    return render(request, 'view.html', context)


def transaction(request):
    if request.method =="POST":
        sender_acc_no = request.POST['submit']
        sender = Customer.objects.get(account_no = sender_acc_no)
        receiver_name = request.POST['transfer_to']
        receiver = Customer.objects.get(name = receiver_name)
        money = request.POST['amount']

        if sender.amount >= int(money):
            sender.amount -= int(money)
            receiver.amount += int(money)
            sender.save()
            receiver.save()

            trans = Transaction()
            trans.source_name = sender.name
            trans.source_acc_no = sender.account_no
            trans.money_transfer = int(money)
            trans.destination_name = receiver.name
            trans.destination_acc_no = receiver.account_no
            trans.save()
            messages.success(request, 'Your money is successfully transfered.')
        else:
            messages.error(request, 'Amount is more then your Current balance.')
        
    return redirect('customer')


def history(request):
    details = Transaction.objects.all().order_by('-date')
    context = {"details" : details}
    return render(request, 'transaction.html', context)


def contact(request):
    if request.method=='POST':
        name = request.POST['name']
        email = request.POST['email']
        phone = request.POST['phone']
        content = request.POST['content']

        # Check whether this is a genuine contact request
        if len(name) < 5 or len(email) < 5 or len(phone) < 10 or len(content) < 5:
            messages.error(request, 'Please fill the form correctly.')
        
        else:
            contact = Contact(name=name, email=email, phone=phone, content=content)
            contact.save()
            messages.success(request, 'Your form submitted successfully, we will contact you soon.')
        
    return render(request, 'contact.html')
