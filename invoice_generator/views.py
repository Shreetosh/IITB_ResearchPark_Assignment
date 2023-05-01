from django.shortcuts import render, redirect
from .models import Invoice
from django.http import FileResponse
import io
from reportlab.lib import colors
from reportlab.lib.pagesizes import letter, inch
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle, Paragraph
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib.colors import HexColor
import json
import datetime

# Create your views here.

def gen_invoice(request):
    if request.method == "POST":
        #retrieve the cookie data sent through javascript
        data = json.loads(request.COOKIES.get('data'))
        n = data[0]
        items = data[1]
        quantities = data[2]
        prices = data[3]
        tax = []
        amount = []
        date_time = datetime.datetime.now()

        #logic for allocating bill number:
        invoice_no=0
        my_invoices = Invoice.objects.all()
        if len(my_invoices)==0:
            invoice_no = 1
        else:
            invoice_no = int(my_invoices.latest('date_time').invoice_no) + 1

        #Getting all other form fields and saving them:
        customer_name = request.POST.get('customer_name')
        customer_phone = request.POST.get('customer_phone')
        customer_email = request.POST.get('customer_email')
        #Calculating tax and amount for each item:
        for i in range(n):
            tax.append(round(float(0.18)*float(prices[i])*float(quantities[i]),2))
            amount.append(round(float(prices[i])*float(quantities[i]) + tax[i],2))
        gen_invoice = Invoice(invoice_no = invoice_no, date_time = date_time, customer_name = customer_name, 
                              customer_phone = customer_phone, 
                              customer_email = customer_email, items=items, prices=prices, 
                              quantities=quantities, tax=tax, amount=amount)
        gen_invoice.save()

        #create pdf:
        doc = SimpleDocTemplate(f"{invoice_no}.pdf", pagesize=letter)
        elements = []
        total_amount = 0
        for i in range(n):
            total_amount = total_amount + amount[i]
        styles = getSampleStyleSheet()
        heading_style = styles['Heading1']
        heading_style.fontSize = 24
        heading_style.leading = 36
        heading_style.alignment = 1  # center alignment
        heading_style.textColor = HexColor('#0000ff')  # blue color
        heading_text = 'Invoice'
        heading = Paragraph(heading_text, heading_style)
        elements.append(heading)
        body_style = styles['Normal']
        body_style.fontSize = 12
        body_style.leading = 18
        body_style.alignment = 0  # left alignment
        body_text = f'Invoice No:{invoice_no}<br/>Date&Time:{date_time}<br/>Customer Name:{customer_name}<br/>Customer Phone:{customer_phone}<br/>Customer Email:{customer_email}<br/>'
        body = Paragraph(body_text, body_style)
        elements.append(body)
        #Invoice table:
        table_data= [['Item Name', 'Price', 'Quantity', 'Tax', 'Amount']]
        for i in range(n):
            table_data.append([f'{items[i]}',f'{prices[i]}',f'{quantities[i]}',f'{tax[i]}',f'{amount[i]}'])
        table = Table(table_data)
        style = TableStyle([
            ('BACKGROUND',(0,0),(-1,0),colors.green),
            ('TEXTCOLOR',(0,0),(-1,0),colors.white),
            ('ALIGN',(0,0),(-1,-1),'CENTER'),
            ('BACKGROUND',(0,1),(-1,-1),colors.beige),
        ])
        table.setStyle(style)
        elements.append(table)
        body_style = styles['Normal']
        body_style.fontSize = 12
        body_style.leading = 18
        body_style.alignment = 0  # left alignment
        body_text = f'Total Amount = {total_amount}'
        total = Paragraph(body_text, body_style)
        elements.append(total)
        doc.build(elements)
    return render(request, 'invoice.html')


