# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/custom-actions


# This is a simple example for a custom action which utters "Hello World!"

from typing import Any, Text, Dict, List

from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
import pandas as pd
import json
import decimal
def currencyInIndiaFormat(n):

  d = decimal.Decimal(str(n))
  if d.as_tuple().exponent < -2:
    s = str(n)
  else:
    s = '{0:.2f}'.format(n)
  l = len(s)
  i = l-1
  res = ''
  flag = 0
  k = 0
  while i>=0:
    if flag==0:
      res = res + s[i]
      if s[i]=='.':
        flag = 1
    elif flag==1:
      k = k + 1
      res = res + s[i]
      if k==3 and i-1>=0:
        res = res + ','
        flag = 2
        k = 0
    else:
      k = k + 1
      res = res + s[i]
      if k==2 and i-1>=0:
        res = res + ','
        flag = 2
        k = 0
    i = i - 1

  return res[::-1]
# Opening JSON file
f = open('/karam_data_dump.json',)

# returns JSON object as a dictionary
#imp = {"max_customer_return_info": "district_food_and_supplies_controller", "total_sales": 97515187, "max_client_info": "reliance_jio_infocomm_limited", "region_product_info": "mro", "total_returns": 5713054.0, "returns_category_amount": "fall_protection", "returns_category_quantity": 93056.0, "yearly_sales_distribution_category": 1612231018.55548, "monthly_sales_distribution_category": 27220400.38, "dealer_sales_info": "PN6000-RIL(WTV-25M)"}
imp = json.load(f)

class ActionHelloWorld(Action):

     def name(self) -> Text:
         return "action_hello_world"

     def run(self, dispatcher: CollectingDispatcher,
             tracker: Tracker,
             domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

         check = 5

         dispatcher.utter_message(check)


         return []

class Actiontotal_sales(Action):

     def name(self) -> Text:
         return "action_total_sales"

     def run(self, dispatcher: CollectingDispatcher,
             tracker: Tracker,
             domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

         val1 = imp['total_sales']
         val1 = str(currencyInIndiaFormat(val1))
         print(val1)
         final_message = "The overall sales of the company for this quarter is :" +" "+val1+' '+"INR"
         dispatcher.utter_message(final_message)

         return []


class Actionchange_sales(Action):

     def name(self) -> Text:
         return "action_change_sales"

     def run(self, dispatcher: CollectingDispatcher,
             tracker: Tracker,
             domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
         val2 = str(imp['change_sales'])
         print(val2)

         dispatcher.utter_message(val2)

         return []


class Actionclients_info(Action):

     def name(self) -> Text:
         return "action_clients_info"

     def run(self, dispatcher: CollectingDispatcher,
             tracker: Tracker,
             domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
         val3 = str(imp['clients_info'])
         print(val3)

         dispatcher.utter_message(val3)

         return []


class Actionmax_clients_info(Action):

     def name(self) -> Text:
         return "action_max_clients_info"

     def run(self, dispatcher: CollectingDispatcher,
             tracker: Tracker,
             domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
         val4 = str(imp['max_client_info'])
         val4 = val4.upper()
         print(val4)
         final_message = "The client who had highest sales for this quarter is :" +" "+val4

         dispatcher.utter_message(final_message)

         return []

class Actionmax_customer_return_info(Action):

     def name(self) -> Text:
         return "action_max_customer_return_info"

     def run(self, dispatcher: CollectingDispatcher,
             tracker: Tracker,
             domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
         val6 = str(imp['max_customer_return_info'])
         val6 = val6.upper()
         print(val6)
         final_message = "The customer who had maximum returns for this quarter is :" +" "+val6

         dispatcher.utter_message(final_message)

         return []

class Actionregion_product_info(Action):

     def name(self) -> Text:
         return "action_region_product_info"

     def run(self, dispatcher: CollectingDispatcher,
             tracker: Tracker,
             domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
         val7 = imp['region_product_info']
         val7 = val7.upper()
         print(val7)
         final_message = "The region with highest sales for this quarter is :" +" "+val7
         dispatcher.utter_message(final_message)

         return []

class Actiontotal_returns(Action):

     def name(self) -> Text:
         return "action_total_returns"

     def run(self, dispatcher: CollectingDispatcher,
             tracker: Tracker,
             domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
         val8 = imp['total_returns']
         val8 = str(currencyInIndiaFormat(val8))
         print(val8)
         final_message = "The overall returns of the company for this quarter is :" +" "+val8+' '+"INR"
         dispatcher.utter_message(final_message)

         return []


class Actionreturns_category_amount(Action):

     def name(self) -> Text:
         return "action_returns_category_amount"

     def run(self, dispatcher: CollectingDispatcher,
             tracker: Tracker,
             domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
         val9 = str(imp['returns_category_amount'])
         val9 = val9.upper()
         print(val9)
         final_message = "The category with maximum returns in terms of amount for this quarter is :" +" "+val9
         dispatcher.utter_message(final_message)

         return []

class Actionreturns_category_quantity(Action):

     def name(self) -> Text:
         return "action_returns_category_quantity"

     def run(self, dispatcher: CollectingDispatcher,
             tracker: Tracker,
             domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
         val10 = str(imp['returns_category_quantity'])
         print(val10)
         final_message = "The maximum returns in terms of quantity for this quarter is :" +" "+val10
         dispatcher.utter_message(final_message)

         return []


class Actionyearly_sales_distribution_category(Action):

     def name(self) -> Text:
         return "action_yearly_sales_distribution_category"

     def run(self, dispatcher: CollectingDispatcher,
             tracker: Tracker,
             domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
         val11 = str(imp['yearly_sales_distribution_category'])
         print(val11)
         final_message = "Total yearly sales for this quarter is :" +" "+val11
         dispatcher.utter_message(final_message)

         return []

class Actionmonthly_sales_distribution_category(Action):

     def name(self) -> Text:
         return "action_monthly_sales_distribution_category"

     def run(self, dispatcher: CollectingDispatcher,
             tracker: Tracker,
             domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
         val12 = str(imp['monthly_sales_distribution_category'])
         print(val12)
         final_message = "Total sales for this quarter is :" +" "+val12
         dispatcher.utter_message(final_message)

         return []


class Actiondealer_sales_info(Action):

     def name(self) -> Text:
         return "action_dealer_sales_info"

     def run(self, dispatcher: CollectingDispatcher,
             tracker: Tracker,
             domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
         val13 = str(imp['dealer_sales_info'])
         print(val13)
         final_message = "The dealer with highest sales of products for this quarter is :" +" "+val13
         dispatcher.utter_message(final_message)

         return []
