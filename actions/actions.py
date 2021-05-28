# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/custom-actions


# This is a simple example for a custom action which utters "Hello World!"

from typing import Any, Text, Dict, List
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
import queries


class ActionHelloWorld(Action):

     def name(self) -> Text:
         return "action_hello_world"

     def run(self, dispatcher: CollectingDispatcher,
             tracker: Tracker,
             domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

         dispatcher.utter_message(text="Hello World!")

         return []

class Actiontotal_sales(Action):

     def name(self) -> Text:
         return "action_total_sales"

     def run(self, dispatcher: CollectingDispatcher,
             tracker: Tracker,
             domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

         dispatcher.utter_message(text="run sql query for total_sales")

         return []


class Actionchange_sales(Action):

     def name(self) -> Text:
         return "action_change_sales"

     def run(self, dispatcher: CollectingDispatcher,
             tracker: Tracker,
             domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

         dispatcher.utter_message(text="run sql query for change_sales")

         return []


class Actionclients_info(Action):

     def name(self) -> Text:
         return "action_clients_info"

     def run(self, dispatcher: CollectingDispatcher,
             tracker: Tracker,
             domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

         dispatcher.utter_message(text="run sql query for clients_info")

         return []


class Actionmax_clients_info(Action):

     def name(self) -> Text:
         return "action_max_clients_info"

     def run(self, dispatcher: CollectingDispatcher,
             tracker: Tracker,
             domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

         dispatcher.utter_message(text="run sql query for max_clients_info")

         return []

class Actionmax_customer_return_info(Action):

     def name(self) -> Text:
         return "action_max_customer_return_info"

     def run(self, dispatcher: CollectingDispatcher,
             tracker: Tracker,
             domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

         dispatcher.utter_message(text="run sql query for max_customer_return_info")

         return []

class Actionregion_product_info(Action):

     def name(self) -> Text:
         return "action_region_product_info"

     def run(self, dispatcher: CollectingDispatcher,
             tracker: Tracker,
             domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

         dispatcher.utter_message(text="run sql query for region_product_info")

         return []

class Actiontotal_returns(Action):

     def name(self) -> Text:
         return "action_total_returns"

     def run(self, dispatcher: CollectingDispatcher,
             tracker: Tracker,
             domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

         dispatcher.utter_message(text="run sql query for total_returns")

         return []


class Actionreturns_category_amount(Action):

     def name(self) -> Text:
         return "action_returns_category_amount"

     def run(self, dispatcher: CollectingDispatcher,
             tracker: Tracker,
             domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

         dispatcher.utter_message(text="run sql query for returns_category_amount")

         return []

class Actionreturns_category_quantity(Action):

     def name(self) -> Text:
         return "action_returns_category_quantity"

     def run(self, dispatcher: CollectingDispatcher,
             tracker: Tracker,
             domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

         dispatcher.utter_message(text="run sql query for returns_category_quantity")

         return []


class Actionyearly_sales_distribution_category(Action):

     def name(self) -> Text:
         return "action_yearly_sales_distribution_category"

     def run(self, dispatcher: CollectingDispatcher,
             tracker: Tracker,
             domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

         dispatcher.utter_message(text="run sql query for yearly_sales_distribution_category")

         return []

class Actionmonthly_sales_distribution_category(Action):

     def name(self) -> Text:
         return "action_monthly_sales_distribution_category"

     def run(self, dispatcher: CollectingDispatcher,
             tracker: Tracker,
             domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

         dispatcher.utter_message(text="run sql query for monthly_sales_distribution_category")

         return []


class Actiondealer_sales_info(Action):

     def name(self) -> Text:
         return "action_dealer_sales_info"

     def run(self, dispatcher: CollectingDispatcher,
             tracker: Tracker,
             domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

         dispatcher.utter_message(text="run sql query for dealer_sales_info")

         return []
