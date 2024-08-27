
import csv
import pprint
import connect
import pandas as pd

#loading data into a dataframe
filename = 'Data/leeds_09-05-2023_09-00-00.csv'
keys = ('Date and time', 'Location','Name', 'Order', 'Total', 'Payment Type', 'Card Number')
with open (filename, 'r') as data:
    reader = csv.DictReader(data,keys)
    mugshot = list()
    for row in reader:
        mugshot.append(row)

def remove_sens_data(input_data_list : list,sens_data_keys:list):
    for dicts in input_data_list:
        for key in sens_data_keys:
            if key in dicts:
                del dicts[key]

def split_date_time(input_data_list : list):
    for dicts in input_data_list:
        dt_temp = dicts["Date and time"]
        date = dt_temp[0:10]
        time = dt_temp[11:16]
        dicts["Date"] = date
        dicts["Time"] = time
        del dicts["Date and time"]
#Splitting orders into name , price and quantity

def split_order(input_data_list : list):
    for dicts in input_data_list:
        product_dupe_tag = 0
        order_dicts_list=[]
        split_order_list = dicts["Order"].split(", ")
        for orders in split_order_list:
            product_dupe_tag = 0
            #order_list.append(orders.split(" - "))
            templist = orders.split(" - ")
            if len(templist)>2:
                price = templist[len(templist)-1]
                name = ""
                for items in templist:  
                    if items != price:
                        name += items
                    name +=" "
                    name.rstrip()
            else:
                name = templist[0]
                price = templist[1]
            for products in order_dicts_list:
                if products["Name"] == name:
                    products["Quantity"] = products["Quantity"] + 1
                    product_dupe_tag=1
            if product_dupe_tag !=1:
                quantity = 1
                order_dicts_list.append({"Name":name,"Price":price,"Quantity":quantity})
                product_dupe_tag = 0

        dicts["Order_dict"] = order_dicts_list
        del dicts["Order"]

def build_transactions_df(transactions_data):
    transactions_list = []
    unique_prods=[]
    for index,transaction in transactions_data.iterrows():
                
                transactions_list.append({"date":transaction.get('Date'),
                    "time" :transaction.get('Time'),
                    "city":transaction.get('Location'),
                    "total_cost":transaction.get('Total'),
                    "payment_method":transaction.get('Payment Type')})
    transactions_df = pd.DataFrame(transactions_list) 
    print(transactions_df)    
    for index,transaction in transactions_data.iterrows():
        for items in transaction.get('Order_dict'):
            unique_prods.append((items['Name'],items['Price']))
        unique_prods = [t for t in (set(tuple(i) for i in unique_prods))]   
    products_df = pd.DataFrame(unique_prods)
    products_df.columns = ["name","price"]
    print(products_df)
    transactions_df.to_csv("TRANSACTIONSDF.csv",sep=",",index=False)
    products_df.to_csv("productsDF.csv",sep=",",index=False)
    data_df = pd.DataFrame(transactions_data)
    print(data_df)
    data_df.to_csv("data.csv",sep=",",index=False)
    
                


    
remove_sens_data(mugshot,['Name','Card Number'])
split_date_time(mugshot)
split_order(mugshot)
df = pd.DataFrame(mugshot)
build_transactions_df(df)
