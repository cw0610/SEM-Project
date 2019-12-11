import json

from typing import Dict, Text, Any, List, Union, Optional
from rasa_sdk import Tracker
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.events import SlotSet
from rasa_sdk.forms import FormAction
from rasa_sdk import Action
from access_database import SQL_Database

class SearchForm(FormAction):
    def name(self):
        return "searching_form"

    def required_slots(self, tracker) -> List[Text]:
        return ["attribute", "key_attribute", "key"]

    def slot_mappings(self) -> Dict[Text, Union[Dict, List[Dict]]]:
        return {
            "attribute": [
                self.from_text(),
            ],
            "key_attribute": [
                self.from_text(),
            ],
            "key": [
                self.from_text(),
            ],
        }

    def submit(
            self,
            dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any],
    ) -> List[Dict]:
        print("Run Form Action Search")
        attribute = tracker.get_slot("attribute")
        print("Detect Attribute: ")
        print(attribute)
        key = tracker.get_slot("key")
        print("Detect Keyword: ")
        print(key)
        key_attribute = tracker.get_slot("key_attribute")
        print("Detect Key Attribute: ")
        print(key_attribute)
        output = SQL_Database.get_output(attribute, key, key_attribute)
        output_len = len(output)
        if len(output) != 0:
            string = f"I found {output_len} vehicle(s) related to your request :"
            dispatcher.utter_message(string)
            if attribute == key_attribute:
                for i in range(len(output)):
                    string = f"Result {i+1}"
                    dispatcher.utter_message(string)
                    string = f"- {attribute} : {output[i][0]}"
                    dispatcher.utter_message(string)
            else:
                for i in range(len(output)):
                    string = f"Result {i + 1}"
                    dispatcher.utter_message(string)
                    string = f"- Given {key_attribute} : {output[i][1]}"
                    dispatcher.utter_message(string)
                    string = f"- Result {attribute} : {output[i][0]}"
                    dispatcher.utter_message(string)
        else:
            dispatcher.utter_message(f"Sorry, I did not found any related result regarding to your request")

        return [SlotSet("attribute", None),
                SlotSet("key", None),
                SlotSet("key_attribute", None)]

class ActionSearch(Action):

    def name(self):
        return "action_searching"

    def run(self, dispatcher, tracker, domain):
        print("Run Form Action Search")
        attribute = tracker.get_slot("attribute")
        print("Detect Attribute: ")
        print(attribute)
        key = tracker.get_slot("key")
        print("Detect Keyword: ")
        print(key)
        key_attribute = tracker.get_slot("key_attribute")
        print("Detect Key Attribute: ")
        print(key_attribute)
        output = SQL_Database.get_output(attribute, key, key_attribute)
        output_len = len(output)
        if len(output) != 0:
            string = f"I found {output_len} vehicle(s) related to your request :"
            dispatcher.utter_message(string)
            if attribute == key_attribute:
                for i in range(len(output)):
                    string = f"Result {i+1}"
                    dispatcher.utter_message(string)
                    string = f"- {attribute} : {output[i][0]}"
                    dispatcher.utter_message(string)
            else:
                for i in range(len(output)):
                    string = f"Result {i + 1}"
                    dispatcher.utter_message(string)
                    string = f"- Given {key_attribute} : {output[i][1]}"
                    dispatcher.utter_message(string)
                    string = f"- Result {attribute} : {output[i][0]}"
                    dispatcher.utter_message(string)
        else:
            dispatcher.utter_message(f"Sorry, I did not found any related result regarding to your request")

        return [SlotSet("attribute", None),
                SlotSet("key", None),
                SlotSet("key_attribute", None)]

class ActionDefaultFallback(Action):
    def name(self):
        return "action_fallback"

    def run(self, dispatcher, tracker, domain):

        dispatcher.utter_message("Sorry, I do not understand. Can you rephrase?")

        return []