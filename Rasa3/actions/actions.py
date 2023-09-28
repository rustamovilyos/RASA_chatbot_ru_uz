# from actions_ru_1_50 import *
# from actions_uz_1_50 import *

# Path: Rasa3/actions/actions.py

import csv
import redis
import yaml
from typing import Any, Text, Dict, List

from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher


class ActionServiceInfoRu(Action):
    def name(self) -> Text:
        return "action_service_info_ru"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        user_message = tracker.latest_message["text"]
        message_language = tracker.latest_message["intent"]["name"][-2:]
        if message_language == "ru":
            found_info = False
            print(tracker.latest_message)
            with open("../data/nlu_ru.yml", "r", encoding="utf-8") as file:
                data = yaml.safe_load(file)
                print(len(data["nlu"]))
            for intent_num in range(len(data["nlu"])):
                intent_name = data["nlu"][intent_num]["intent"]
                intent_examples = data["nlu"][intent_num]["examples"]
                examples_list = intent_examples[2:].split('\n')
                if user_message in intent_examples:
                    with open("../Muxlisa.xlsx - Лист1.csv", "r", encoding="utf-8") as file_reader:
                        csv_reader = csv.reader(file_reader, delimiter=',')
                        for rows in csv_reader:
                            if examples_list[0] in rows[5]:
                                detail_info = rows[7]
                                link_ru = rows[2]
                                dispatcher.utter_message(f"Название услуги: {rows[5]}")
                                dispatcher.utter_message(f"Информация об услуге: {detail_info}")
                                dispatcher.utter_message(f"Чтобы воспользоваться сервисом и получить полную информацию,"
                                                         f" перейдите по ссылке:"
                                                         f" <a href='{link_ru}'>{link_ru}</a>")

                                redis_client = redis.StrictRedis(host='localhost', port=6379, db=0)

                                redis_client.set(f"{intent_name}", intent_name)
                                redis_client.set(f"{intent_name}_description", detail_info)

                                redis_client.close()
                                found_info = True
                                print(f'service_name saved: {intent_name}\n'
                                      f'service_description saved: {detail_info}')
                                return []

                if found_info:
                    break
            if not found_info:
                dispatcher.utter_message(text='Простите, я не могу ответить на ваш вопрос')
            return []
        else:
            print("message language is not ru")


class ActionServiceInfoUz(Action):
    def name(self) -> Text:
        return "action_service_info_uz"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        user_message = tracker.latest_message["text"]
        message_language = tracker.latest_message["intent"]["name"][-2:]
        if message_language == "uz":
            found_info = False
            with open("../data/nlu_uz.yml", "r", encoding="utf-8") as file:
                data = yaml.safe_load(file)
                print(len(data["nlu"]))
            for intent_num in range(len(data["nlu"])):
                intent_name = data["nlu"][intent_num]["intent"]
                intent_examples = data["nlu"][intent_num]["examples"]

                if user_message in intent_examples:
                    examples_list = intent_examples[2:].split('\n')
                    print(examples_list)
                    with open("../Muxlisa.xlsx - Лист1.csv", "r", encoding="utf-8") as file_reader:
                        csv_reader = csv.reader(file_reader, delimiter=',')
                        for rows in csv_reader:
                            if examples_list[0] in rows[9]:
                                detail_info = rows[8]
                                link_uz = rows[3]
                                dispatcher.utter_message(f"Xizmat: {rows[9]}")
                                dispatcher.utter_message(f"Xizmat haqida ma'lumot: {detail_info}")
                                dispatcher.utter_message(f"Xizmatdan foydalanish va to'liq ma'lumot olish uchun havola:"
                                                         f" <a href='{link_uz}'>{link_uz}</a>")

                                redis_client = redis.StrictRedis(host='localhost', port=6379, db=0)

                                redis_client.set(f"{intent_name}", intent_name)
                                redis_client.set(f"{intent_name}_description", detail_info)

                                redis_client.close()
                                found_info = True
                                print(f'service_name saved: {intent_name}\n'
                                      f'service_description saved: {detail_info}')
                                return []

                if found_info:
                    break
            if not found_info:
                dispatcher.utter_message(text='Uzr, men bu savolga javob beraolmayman')
            return []
        else:
            print("message language is not uz")
