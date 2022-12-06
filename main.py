#!/usr/bin/env python3
import json
from time import sleep
  
f = open('data.json')
  
stock = json.load(f)
nav = ['Stock', 'Shopping' ,'Packing', 'Change']
type = ["Luxury", "Essential", "Gift"]
basket = []
screen = 0
log = 0
def login() :
    print('\n---------------------------------------------------------------\n')
    print('Log as : \n\t1-User\n\t2-Admin')
    log = int(input('-> '))
    navigation(log)

def navigation(log) : 
    print('\n---------------------------------------------------------------\n')
    print(log)
    print('\t\tYou are loged as', 'User' if log == 1 else 'Admin')
    while (1) : 
        print('Go to : \n\t1 - Stock\n\t2 - Shopping\n\t3 - Packing\n\t4 - Change\n\t5 - Quit')
        screen = int(input('-> '))
        if screen == 5 :
            break
        print('\n---------------------------------------------------------------\n')
        Stock() if screen == 1 else Shopping() if screen == 2 else Packing() if screen == 3 else Change()

def Stock() : 
    while (1):
        print('\t\tStock')
        choice = int(input('Go to : \n\t1 - Add Item\n\t2 - View Item\n\t3 - Remove Item\n\t4 - Quit\n->'))
        if choice == 1 :
            AddItem()
        elif choice == 4 : 
            break
        else :
            ViewItem(choice)

def AddItem() : 
    print('\t\tAdd Item')
    item = {
        "name" : input('Item Name\n\t-> '),
        "type" : int(input('Item Type : \n\t1 - Luxury\n\t2 - Essential\n\t3 - Gift\n\t -> ')) - 1,
        "exp" : input('Expiration date \n\t-> '),
        "quantity" : int(input('Quantity\n\t-> '))
    }
    stock.append(item)
    print(item["name"] + " added to Stock")
    input('\n[enter to go back]')
    print('\n---------------------------------------------------------------\n')


def ViewItem(choice) : 
    print('\t\tView Item') 
    print("  - {:<15} {:<15} {:<15} {:<15}\n".format('Name','Type', 'Exp Date', 'Quantity'))
    x = 1
    for item in stock :
        print(x," - {:<15} {:<15} {:<15} {:<15}".format(item["name"], type[item["type"]], item["exp"], item["quantity"]))
        x -= -1
    if choice == 3 : 
        item = int(input('ID of Item to remove\n\t->')) - 1
        old = stock[item]
        stock.pop(item)
        print(old["name"], "as been removed")
    input('\n[enter to go back]')
    print('\n---------------------------------------------------------------\n')


def Shopping() : 
    print('\t\tAdd Item to Estimate') 
    print("  - {:<15} {:<15} {:<15} \n".format('Name', 'Quantity', 'Price €'))
    ItemToBasket()
    choice = int(input('\n\t1 - Add new item\n\t2 - Show Estimate\n\t3 - Quit\n\t -> '))

    while (1):
        if choice == 2 :
            Estimate()
        elif choice == 1 : 
            ItemToBasket()
        elif choice == 3:
            removeItem()
        elif choice == 4:
            ShowBasket()
        else :
            basket.clear()
            break
        choice = int(input('\n\t1 - Add new item\n\t2 - Show Estimate\n\t3 - Remove Item\n\t4 - Go to Basket\n\t5 - Quit\n\t -> '))
    print('\n---------------------------------------------------------------\n')

def ItemToBasket() :
        x = 1
        for item in stock :
            print(x," - {:<15} {:<15} {:<15}".format(item["name"], item["quantity"], EstimateSelf(item)))
            x -= -1
        item = int(input('\nID of item -> ')) - 1
        quantity = int(input('\nQuantity -> '))
        stock[item]["quant"] = quantity
        basket.append(stock[item])
        print(stock[item]['name'], 'add to basket\n\n')
        print('\n---------------------------------------------------------------\n')


def removeItem() :
    item = int(input('ID of Item to remove\n\t->')) - 1
    old = basket[item]
    basket.pop(item)
    print(old["name"], "as been removed")

def EstimateSelf(item) :
    cost = 50 if item["type"] == 0 else 30 if item["type"] == 1 else 20
    return (cost)


def EstimateVAT(item) :
    cost = 60 if item["type"] == 0 else 33 if item["type"] == 1 else 21
    return (cost * item["quant"])

def Estimate() : 
    print("  - {:<15} {:<15} {:<15} \n".format('Name', 'Quantity', 'Price € with VAT'))
    x = 1
    for item in basket :
        print(x," - {:<15} {:<15} {:<15}".format(item["name"], item["quant"], EstimateVAT(item)))
        x -= -1

def ShowBasket() : 
    cost = 0
    vat = 0
    for item in basket :
        cost += EstimateSelf(item) * item['quant']
        vat += EstimateVAT(item)
        
    print('\n---------------------------------------------------------------\n')    
    print('Bill : \n\tcost :\t\t', cost, '\n\t+VAT :\t\t', vat-cost, '\n\ttotal : \t', vat)
def Packing() : 
    print('\t\tPacking')
def Change() : 
    print('\t\tChange')

login()
#
#
# if screen == 1 :
#        item = {
#            "name" : input('Item Name\n\t-> '),
#            "type" : int(input('Item Type : \n\t1-Luxury\n\t2-Essential\n\t3-Gift\n\t -> ')) - 1,
#            "exp" : input(' expiration date \n\t-> '),
#            "quantity" : int(input('quantity\n\t-> '))
#        }
#        stock.append(item)
#        print(item["name"] + " added to Stock")
#    if screen == 2 : 
#        print('  \tName\tType\tExp Date\tQuantity')
#        for item in stock : 
#            print('--\t',item["name"], '\t', type[item["type"]],'\t', item["exp"],'\t', item["quantity"] )
#    if screen == 3 :
#        while (1) :  
#            x = 1
#            for item in stock : 
#                print('--',x,'\t',item["name"])
#                x -= -1
#            choice = int(input('\n1-Add Item to Estimation\n2-Show Estimation\n -> '))
#            if choice == 1 : 
#                item = int(input('Item Number-> ')) - 1
#                basket.append(stock[item])
#                print(item['name'], 'add to basket')
#                print(stock[item['name']], 'add to basket')
#            elif choice == 2 : 
#                x = 1
#                for item in basket : 
#                    print('--',x,'\t',item["name"])
#                    x -= -1
#    if screen == 4 : 
#        print('4')


   