# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/custom-actions


# This is a simple example for a custom action which utters "Hello World!"

from typing import Any, Text, Dict, List

from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
import sys
sys.path.append('/Users/jd/Documents/GitHub/sales_chatbot') #/Users/jd/Documents/GitHub/sales_chatbot path for the file
import queries
#import queries /Users/jd/Desktop/sales_chatbot/queries.py
import pandas as pd
a = queries.convert_json()
imp = json.loads(a)

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

         dispatcher.utter_message(val1)

         return []


class Actionchange_sales(Action):

     def name(self) -> Text:
         return "action_change_sales"

     def run(self, dispatcher: CollectingDispatcher,
             tracker: Tracker,
             domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
         val2 = imp['change_sales']
         dispatcher.utter_message(val2)

         return []


class Actionclients_info(Action):

     def name(self) -> Text:
         return "action_clients_info"

     def run(self, dispatcher: CollectingDispatcher,
             tracker: Tracker,
             domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
         val3 = imp['clients_info']
         dispatcher.utter_message(val3)

         return []


class Actionmax_clients_info(Action):

     def name(self) -> Text:
         return "action_max_clients_info"

     def run(self, dispatcher: CollectingDispatcher,
             tracker: Tracker,
             domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
         val4 = imp['max_client_info']
         dispatcher.utter_message(val4)

         return []

class Actionmax_customer_return_info(Action):

     def name(self) -> Text:
         return "action_max_customer_return_info"

     def run(self, dispatcher: CollectingDispatcher,
             tracker: Tracker,
             domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
         val6 = imp['max_customer_return_info']
         dispatcher.utter_message(val6)

         return []

class Actionregion_product_info(Action):

     def name(self) -> Text:
         return "action_region_product_info"

     def run(self, dispatcher: CollectingDispatcher,
             tracker: Tracker,
             domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
         val7 = imp['region_product_info']
         dispatcher.utter_message(val7)

         return []

class Actiontotal_returns(Action):

     def name(self) -> Text:
         return "action_total_returns"

     def run(self, dispatcher: CollectingDispatcher,
             tracker: Tracker,
             domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
         val8 = imp['total_returns']
         dispatcher.utter_message(val8)

         return []


class Actionreturns_category_amount(Action):

     def name(self) -> Text:
         return "action_returns_category_amount"

     def run(self, dispatcher: CollectingDispatcher,
             tracker: Tracker,
             domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
         val9 = imp['returns_category_amount']
         dispatcher.utter_message(val9)

         return []

class Actionreturns_category_quantity(Action):

     def name(self) -> Text:
         return "action_returns_category_quantity"

     def run(self, dispatcher: CollectingDispatcher,
             tracker: Tracker,
             domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
         val10 = imp['returns_category_quantity']
         dispatcher.utter_message(val10)

         return []


class Actionyearly_sales_distribution_category(Action):

     def name(self) -> Text:
         return "action_yearly_sales_distribution_category"

     def run(self, dispatcher: CollectingDispatcher,
             tracker: Tracker,
             domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
         val11 = imp['yearly_sales_distribution_category']
         dispatcher.utter_message(val11)

         return []

class Actionmonthly_sales_distribution_category(Action):

     def name(self) -> Text:
         return "action_monthly_sales_distribution_category"

     def run(self, dispatcher: CollectingDispatcher,
             tracker: Tracker,
             domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
         val12 = imp['monthly_sales_distribution_category']
         dispatcher.utter_message(val12)

         return []


class Actiondealer_sales_info(Action):

     def name(self) -> Text:
         return "action_dealer_sales_info"

     def run(self, dispatcher: CollectingDispatcher,
             tracker: Tracker,
             domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
         val13 = imp['dealer_sales_info']
         dispatcher.utter_message(val13)

         return []
