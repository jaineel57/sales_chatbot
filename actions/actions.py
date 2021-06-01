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

# Opening JSON file
f = open('karam_data_dump.json',)

# returns JSON object as a dictionary
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

         val1 = str(imp['total_sales'])
         print(val1)
         final_message = "The overall sales of the company are :" +" "+val1
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
         print(val4)
         final_message = "The client who had highest sales is :" +" "+val4

         dispatcher.utter_message(final_message)

         return []

class Actionmax_customer_return_info(Action):

     def name(self) -> Text:
         return "action_max_customer_return_info"

     def run(self, dispatcher: CollectingDispatcher,
             tracker: Tracker,
             domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
         val6 = str(imp['max_customer_return_info'])
         print(val6)
         final_message = "The custmer who had maximum returns is :" +" "+val6

         dispatcher.utter_message(final_message)

         return []

class Actionregion_product_info(Action):

     def name(self) -> Text:
         return "action_region_product_info"

     def run(self, dispatcher: CollectingDispatcher,
             tracker: Tracker,
             domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
         val7 = imp['region_product_info']
         print(val7)
         final_message = "The region with highest sales is :" +" "+val7
         dispatcher.utter_message(final_message)

         return []

class Actiontotal_returns(Action):

     def name(self) -> Text:
         return "action_total_returns"

     def run(self, dispatcher: CollectingDispatcher,
             tracker: Tracker,
             domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
         val8 = str(imp['total_returns'])
         print(val8)
         final_message = "The overall returns of the company :" +" "+val8
         dispatcher.utter_message(final_message)

         return []


class Actionreturns_category_amount(Action):

     def name(self) -> Text:
         return "action_returns_category_amount"

     def run(self, dispatcher: CollectingDispatcher,
             tracker: Tracker,
             domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
         val9 = str(imp['returns_category_amount'])
         print(val9)
         final_message = "The category with maximum returns in terms of amount is :" +" "+val9
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
         final_message = "The maximum returns in terms of quantity are :" +" "+val10
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
         final_message = "Total yearly sales are :" +" "+val11
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
         final_message = "Total monthly sales are :" +" "+val12
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
         final_message = "The dealer with highest sales of products is :" +" "+val13
         dispatcher.utter_message(final_message)

         return []
