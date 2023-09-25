import csv
from typing import Any, Text, Dict, List

import redis
import yaml
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher


class ActionStudentDormitoryInfoUz(Action):  # 1
    def name(self) -> Text:
        return "action_student_dormitory_info_uz"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        user_message = tracker.latest_message['text']
        with open('../data/nlu_uz.yml', 'r') as file:
            nlu_data = yaml.safe_load(file)

        intent_name = "checking_the_queue_in_the_student_dormitory_uz"
        if intent_name == nlu_data['nlu'][1]['intent']:
            intent_examples = nlu_data['nlu'][1]['examples']
            if user_message in intent_examples:
                with open("../Muxlisa - Лист1.csv", mode='r') as new_reader:
                    xizmat_nomi = 'Талабалар турар жойига навбатни текшириш (1-курс талабалари учун)'
                    csv_reader = csv.DictReader(new_reader, delimiter=',')
                    for rows in csv_reader:
                        if rows[
                            'Xizmat nomi - uz'
                        ] == xizmat_nomi:
                            detail_info = rows['Muxlisa text - UZ']
                            link_uz = rows['Link uz - lotincha']
                            dispatcher.utter_message(f"Xizmat: {xizmat_nomi} \n"
                                                     f"Xizmat haqida ma'lumot: {detail_info}")
                            dispatcher.utter_message(f"xizmatga o'tish uchun havola: <a href='{link_uz}'>{link_uz}</a>")

                            redis_client = redis.StrictRedis(host='localhost', port=6379, db=0)

                            redis_client.set(f"{intent_name}", xizmat_nomi)
                            redis_client.set(f"{intent_name}_description", detail_info)

                            print(f'service_name saved: {xizmat_nomi}\n'
                                  f'service_description saved: {detail_info}')
        else:
            dispatcher.utter_message(text='Uzr, men bu savolga javob beraolmayman')

        return []


class ActionApplyForStudentsDormitoryUz(Action):  # 2
    def name(self) -> Text:
        return "action_apply_for_students_dormitory_uz"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        user_message = tracker.latest_message['text']
        with open('../data/nlu_uz.yml', 'r') as file:
            nlu_data = yaml.safe_load(file)

        intent_name = "apply_for_students_dormitory_uz"
        if intent_name == nlu_data['nlu'][2]['intent']:
            intent_examples = nlu_data['nlu'][2]['examples']
            if user_message in intent_examples:
                with open('../Muxlisa - Лист1.csv', mode='r') as new_reader:
                    xizmat_nomi = 'Талабалар турар жойига жойлашиш учун ариза юбориш (1-курс талабалари учун)'
                    csv_reader = csv.DictReader(new_reader, delimiter=',')
                    for rows in csv_reader:
                        if rows['Xizmat nomi - uz'] == xizmat_nomi:
                            detail_info = rows['Muxlisa text - UZ']
                            link_uz = rows['Link uz - lotincha']
                            dispatcher.utter_message(f"Xizmat: {xizmat_nomi} \n"
                                                     f"Xizmat haqida ma'lumot: {detail_info}")
                            dispatcher.utter_message(f"xizmatga o'tish uchun havola: <a href='{link_uz}'>{link_uz}</a>")

                            redis_client = redis.StrictRedis(host='localhost', port=6379, db=0)

                            redis_client.set(f"{intent_name}", xizmat_nomi)
                            redis_client.set(f"{intent_name}_description", detail_info)

        else:
            dispatcher.utter_message(text='Uzr, men bu savolga javob beraolmayman')

        return []


class ActionPrivateInvitationOfForeignCitizensUz(Action):  # 3
    def name(self) -> Text:
        return "action_private_invitation_of_foreign_citizens_uz"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        user_message = tracker.latest_message['text']

        with open('../data/nlu_uz.yml', 'r') as file:
            nlu_data = yaml.safe_load(file)

        intent_name = 'private_invitation_of_foreign_citizens_uz'
        if intent_name == nlu_data['nlu'][3]['intent']:
            intent_example = nlu_data['nlu'][3]['examples']
            if user_message in intent_example:
                with open('../Muxlisa - Лист1.csv', mode='r') as new_reader:
                    xizmat_nomi = ('Чет эл фуқароси ва фуқаролиги бўлмаган шахсларни Ўзбекистон Республикасига хусусий '
                                   'таклиф қилишга ариза юбориш')
                    csv_reader = csv.DictReader(new_reader, delimiter=',')
                    for rows in csv_reader:
                        if rows['Xizmat nomi - uz'] == xizmat_nomi:
                            detail_info = rows['Muxlisa text - UZ']
                            link_uz = rows['Link uz - lotincha']
                            dispatcher.utter_message(f"Xizmat: {xizmat_nomi} \n"
                                                     f"Xizmat haqida ma'lumot: {detail_info}")
                            dispatcher.utter_message(f"xizmatga o'tish uchun havola: <a href='{link_uz}'>{link_uz}</a>")

                            redis_client = redis.StrictRedis(host='localhost', port=6379, db=0)

                            redis_client.set(f"{intent_name}", xizmat_nomi)
                            redis_client.set(f"{intent_name}_description", detail_info)

        else:
            dispatcher.utter_message("Uzr, men bu savolga javob beraolmayman")

        return []


class ActionViewAirTicketsOnUzAirWaysUz(Action):  # 4
    def name(self) -> Text:
        return "action_view_air_tickets_on_uzairways_uz"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        user_message = tracker.latest_message['text']

        with open('../data/nlu_uz.yml', 'r') as file:
            nlu_data = yaml.safe_load(file)

        intent_name = 'view_airtickets_on_Uzairways_uz'
        if intent_name == nlu_data['nlu'][4]['intent']:
            intent_example = nlu_data['nlu'][4]['examples']
            if user_message in intent_example:
                with open('../Muxlisa - Лист1.csv', mode='r') as new_reader:
                    xizmat_nomi = 'Uzbekistan Airways saytidagi aviachiptalar'
                    csv_reader = csv.DictReader(new_reader, delimiter=',')
                    for rows in csv_reader:
                        if rows['Xizmat nomi - uz'] == xizmat_nomi:
                            detail_info = rows['Muxlisa text - UZ']
                            link_uz = rows['Link uz - lotincha']
                            dispatcher.utter_message(f"Xizmat: {xizmat_nomi} \n"
                                                     f"Xizmat haqida ma'lumot: {detail_info}")
                            dispatcher.utter_message(f"xizmatga o'tish uchun havola: <a href='{link_uz}'>{link_uz}</a>")

                            redis_client = redis.StrictRedis(host='localhost', port=6379, db=0)

                            redis_client.set(f"{intent_name}", xizmat_nomi)
                            redis_client.set(f"{intent_name}_description", detail_info)

        else:
            dispatcher.utter_message('Uzr, men bu savolga javob beraolmayman')

        return []


class ActionObtainingCertificateOfReturnToUzbUz(Action):  # 5
    def name(self) -> Text:
        return "action_obtaining_certificate_of_return_to_UZB_uz"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        user_message = tracker.latest_message['text']

        with open("../data/nlu_uz.yml", "r") as file:
            nlu_data = yaml.safe_load(file)

        intent_name = "obtaining_certificate_of_return_to_UZB_ru"
        if intent_name in nlu_data['nlu'][5]['intent']:
            intent_example = nlu_data['nlu'][5]['examples']
            if user_message in intent_example:
                with open("../Muxlisa - Лист1.csv", "r") as new_reader:
                    xizmat_nomi = "O‘zbekiston Respublikasiga qaytish uchun guvohnoma olish"
                    csv_reader = csv.DictReader(new_reader, delimiter=',')
                    for rows in csv_reader:
                        if rows['Xizmat nomi - uz'] == xizmat_nomi:
                            detail_info = rows['Muxlisa text - UZ']
                            link_ru = rows['Link ru']
                            dispatcher.utter_message(f"Xizmat: {xizmat_nomi} \n"
                                                     f"Xizmat haqida ma'lumot: {detail_info}")
                            dispatcher.utter_message(f"xizmatga o'tish uchun havola: <a href='{link_ru}'>{link_ru}</a>")

                            redis_client = redis.StrictRedis(host='localhost', port=6379, db=0)

                            redis_client.set(f"{intent_name}", xizmat_nomi)
                            redis_client.set(f"{intent_name}_description", detail_info)
        else:
            dispatcher.utter_message("Uzr, men bu savolga javob beraolmayman")

        return []


class ActionCertificationOfApplicantsForJudicialManagersUz(Action):  # 6
    def name(self) -> Text:
        return "action_certification_of_applicants_for_judicial_managers_uz"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        user_message = tracker.latest_message['text']

        with open("../data/nlu_uz.yml", "r") as file:
            nlu_data = yaml.safe_load(file)

        intent_name = "certification_of_applicants_for_judicial_managers_uz"
        if intent_name in nlu_data['nlu'][6]['intent']:
            intent_example = nlu_data['nlu'][6]['examples']
            if user_message in intent_example:
                with open("../Muxlisa - Лист1.csv", "r") as new_reader:
                    xizmat_nomi = ("Суд бошқарувчилари талабгорларини аттестациядан (қайта аттестациядан) ўтказиш ва"
                                   " уларга малака аттестатини бериш")
                    csv_reader = csv.DictReader(new_reader, delimiter=',')
                    for rows in csv_reader:
                        if rows['Xizmat nomi - uz'] == xizmat_nomi:
                            detail_info = rows['Muxlisa text - UZ']
                            link_ru = rows['Link ru']
                            dispatcher.utter_message(f"Xizmat: {xizmat_nomi} \n"
                                                     f"Xizmat haqida ma'lumot: {detail_info}")
                            dispatcher.utter_message(f"xizmatga o'tish uchun havola: <a href='{link_ru}'>{link_ru}</a>")

                            redis_client = redis.StrictRedis(host='localhost', port=6379, db=0)

                            redis_client.set(f"{intent_name}", xizmat_nomi)
                            redis_client.set(f"{intent_name}_description", detail_info)
        else:
            dispatcher.utter_message("Uzr, men bu savolga javob beraolmayman")

        return []


class ActionRegistrationOfPermanentResidenceAbroadUz(Action):  # 7
    def name(self) -> Text:
        return "action_registration_of_permanent_residence_abroad_uz"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        user_message = tracker.latest_message['text']

        with open("../data/nlu_uz.yml", "r") as file:
            nlu_data = yaml.safe_load(file)

        intent_name = "registration_of_permanent_residence_abroad_uz"
        if intent_name in nlu_data['nlu'][7]['intent']:
            intent_example = nlu_data['nlu'][7]['examples']
            if user_message in intent_example:
                with open("../Muxlisa - Лист1.csv", "r") as new_reader:
                    xizmat_nomi = "Хорижга доимий яшашга чиқишни расмийлаштириш"
                    csv_reader = csv.DictReader(new_reader, delimiter=',')
                    for rows in csv_reader:
                        if rows['Xizmat nomi - uz'] == xizmat_nomi:
                            detail_info = rows['Muxlisa text - UZ']
                            link_ru = rows['Link ru']
                            dispatcher.utter_message(f"Xizmat: {xizmat_nomi} \n"
                                                     f"Xizmat haqida ma'lumot: {detail_info}")
                            dispatcher.utter_message(f"xizmatga o'tish uchun havola: <a href='{link_ru}'>{link_ru}</a>")

                            redis_client = redis.StrictRedis(host='localhost', port=6379, db=0)

                            redis_client.set(f"{intent_name}", xizmat_nomi)
                            redis_client.set(f"{intent_name}_description", detail_info)
        else:
            dispatcher.utter_message("Uzr, men bu savolga javob beraolmayman")

        return []


class ActionApplyTestResultUz(Action):  # 8
    def name(self) -> Text:
        return "action_apply_test_result_uz"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        user_message = tracker.latest_message['text']

        with open("../data/nlu_uz.yml", "r") as file:
            nlu_data = yaml.safe_load(file)

        intent_name = "applicant_test_result_uz"
        if intent_name in nlu_data['nlu'][8]['intent']:
            intent_example = nlu_data['nlu'][8]['examples']
            if user_message in intent_example:
                with open("../Muxlisa - Лист1.csv", "r") as new_reader:
                    xizmat_nomi = "Тракторчи-машинист гувоҳномасини алмаштириш ёки йўқолгани ўрнига янгисини олиш"
                    csv_reader = csv.DictReader(new_reader, delimiter=',')
                    for rows in csv_reader:
                        if rows['Xizmat nomi - uz'] == xizmat_nomi:
                            detail_info = rows['Muxlisa text - UZ']
                            link_ru = rows['Link ru']
                            dispatcher.utter_message(f"Xizmat: {xizmat_nomi} \n"
                                                     f"Xizmat haqida ma'lumot: {detail_info}")
                            dispatcher.utter_message(f"xizmatga o'tish uchun havola: <a href='{link_ru}'>{link_ru}</a>")

                            redis_client = redis.StrictRedis(host='localhost', port=6379, db=0)

                            redis_client.set(f"{intent_name}", xizmat_nomi)
                            redis_client.set(f"{intent_name}_description", detail_info)
        else:
            dispatcher.utter_message("Uzr, men bu savolga javob beraolmayman")


class ActionDripIrrigationInfoUz(Action):  # 12
    def name(self) -> Text:
        return "action_drip_irrigation_info_uz"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        user_message = tracker.latest_message['text']

        with open('../data/nlu_uz.yml', 'r') as file:
            nlu_data = yaml.safe_load(file)

        intent_name = "calculate_drip_irrigation_uz"
        if intent_name in nlu_data['nlu'][8]['intent']:
            intent_examples = nlu_data['nlu'][8]['examples']
            if user_message in intent_examples:
                with open("../Muxlisa - Лист1.csv", mode='r') as file_reader:
                    csv_reader = csv.DictReader(file_reader, delimiter=',')
                    xizmat_nomi = 'Томчилатиб суғориш калькулятори'
                    for rows in csv_reader:
                        if rows['Xizmat nomi - ru'] == xizmat_nomi:
                            detail_info = rows['Muxlisa text - UZ']
                            link_uz = rows['Link uz - lotincha']
                            dispatcher.utter_message(f"Xizmat: {xizmat_nomi} \n"
                                                     f"Xizmat haqida ma'lumot: {detail_info}")
                            dispatcher.utter_message(f"Xizmatdan foydalanish va to'liq ma'lumot olish uchun havola:"
                                                     f" <a href='{link_uz}'>{link_uz}</a>")

                            redis_client = redis.StrictRedis(host='localhost', port=6379, db=0)

                            redis_client.set(f"{intent_name}", xizmat_nomi)
                            redis_client.set(f"{intent_name}_description", detail_info)

                            redis_client.close()
                            print(f'service_name saved: {xizmat_nomi}\n'
                                  f'service_description saved: {detail_info}')
        else:
            dispatcher.utter_message(text='Uzr, men bu savolga javob beraolmayman')

        return []
