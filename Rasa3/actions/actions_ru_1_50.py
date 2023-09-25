import csv
from typing import Any, Text, Dict, List

import redis
import yaml
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher


class ActionStudentDormitoryInfoRu(Action):  # 1
    def name(self) -> Text:
        return "action_student_dormitory_info_ru"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        user_message = tracker.latest_message['text']

        with open('../data/nlu_ru.yml', 'r') as file:
            nlu_data = yaml.safe_load(file)

        intent_name = "checking_the_queue_in_the_student_dormitory_ru"
        if intent_name in nlu_data['nlu'][1]['intent']:
            intent_examples = nlu_data['nlu'][1]['examples']
            if user_message in intent_examples:
                with open("../Muxlisa - Лист1.csv", mode='r') as file_reader:
                    csv_reader = csv.DictReader(file_reader, delimiter=',')
                    xizmat_nomi = 'Проверка очереди в студенческом общежитии (для студентов 1 курса)'
                    for rows in csv_reader:
                        if rows[
                            'Xizmat nomi - ru'
                        ] == xizmat_nomi:
                            detail_info = rows['Muxlisa text - RU']
                            link_ru = rows['Link ru']
                            dispatcher.utter_message(f"Название услуга: {xizmat_nomi} \n"
                                                     f"{detail_info}")
                            dispatcher.utter_message(f"Подробнее об услуге вы можете узнать по ссылке:"
                                                     f" <a href='{link_ru}'>{link_ru}</a>")

                            redis_client = redis.StrictRedis(host='localhost', port=6379, db=0)

                            redis_client.set(f"{intent_name}", xizmat_nomi)
                            redis_client.set(f"{intent_name}_description", detail_info)

                            print(f'service_name saved: {xizmat_nomi}\n'
                                  f'service_description saved: {detail_info}')
        else:
            dispatcher.utter_message(text='Простите, я не могу ответит на ваш вопрос')

        return []


class ActionApplyForStudentsDormitoryRu(Action):  # 2
    def name(self) -> Text:
        return "action_apply_for_students_dormitory_ru"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        user_message = tracker.latest_message['text']

        with open('../data/nlu_ru.yml', 'r') as file:
            nlu_data = yaml.safe_load(file)

        intent_name = "apply_for_students_dormitory_ru"
        if intent_name in nlu_data['nlu'][2]['intent']:
            intent_examples = nlu_data['nlu'][2]['examples']
            if user_message in intent_examples:
                with open("../Muxlisa - Лист1.csv", mode='r') as file_reader:
                    csv_reader = csv.DictReader(file_reader, delimiter=',')
                    xizmat_nomi = 'Подача заявления на размещение в студенческом общежитии (для студентов 1 курса)'
                    for rows in csv_reader:
                        if rows[
                            'Xizmat nomi - ru'
                        ] == xizmat_nomi:
                            detail_info = rows['Muxlisa text - RU']
                            link_ru = rows['Link ru']
                            dispatcher.utter_message(f"Название услуга: {xizmat_nomi} \n"
                                                     f"{detail_info}")
                            dispatcher.utter_message(f"Подробнее об услуге вы можете узнать по ссылке:"
                                                     f" <a href='{link_ru}'>{link_ru}</a>")

                            redis_client = redis.StrictRedis(host='localhost', port=6379, db=0)

                            redis_client.set(f"{intent_name}", xizmat_nomi)
                            redis_client.set(f"{intent_name}_description", detail_info)

                            print(f'service_name saved: {xizmat_nomi}\n'
                                  f'service_description saved: {detail_info}')
        else:
            dispatcher.utter_message(text='Простите, я не могу ответит на ваш вопрос')

        return []


class ActionPrivateInvitationOfForeignCitizensRu(Action):  # 3
    def name(self) -> Text:
        return "action_private_invitation_of_foreign_citizens_ru"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        user_message = tracker.latest_message['text']

        with open('../data/nlu_ru.yml', 'r') as file:
            nlu_data = yaml.safe_load(file)

        intent_name = "private_invitation_of_foreign_citizens_ru"
        if intent_name in nlu_data['nlu'][3]['intent']:
            intent_examples = nlu_data['nlu'][3]['examples']
            if user_message in intent_examples:
                with open("../Muxlisa - Лист1.csv", mode='r') as file_reader:
                    csv_reader = csv.DictReader(file_reader, delimiter=',')
                    xizmat_nomi = ('Подача документов для частного приглашения иностранных граждан'
                                   ' и лиц без гражданства в Республику Узбекистан')
                    for rows in csv_reader:
                        if rows[
                            'Xizmat nomi - ru'
                        ] == xizmat_nomi:
                            detail_info = rows['Muxlisa text - RU']
                            link_ru = rows['Link ru']
                            dispatcher.utter_message(f"Название услуга: {xizmat_nomi} \n"
                                                     f"{detail_info}")
                            dispatcher.utter_message(f"Подробнее об услуге вы можете узнать по ссылке:"
                                                     f" <a href='{link_ru}'>{link_ru}</a>")

                            redis_client = redis.StrictRedis(host='localhost', port=6379, db=0)

                            redis_client.set(f"{intent_name}", xizmat_nomi)
                            redis_client.set(f"{intent_name}_description", detail_info)

                            print(f'service_name saved: {xizmat_nomi}\n'
                                  f'service_description saved: {detail_info}')
        else:
            dispatcher.utter_message(text='Простите, я не могу ответит на ваш вопрос')

        return []


class ActionViewAirTicketsOnUzAirWaysRu(Action):  # 4
    def name(self) -> Text:
        return "action_view_air_tickets_on_uzairways_ru"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        user_message = tracker.latest_message['text']

        with open('../data/nlu_ru.yml', 'r') as file:
            nlu_data = yaml.safe_load(file)

        intent_name = 'view_airtickets_on_Uzairways_ru'
        if intent_name in nlu_data['nlu'][4]['intent']:
            intent_example = nlu_data['nlu'][4]['examples']
            if user_message in intent_example:
                with open('../Muxlisa - Лист1.csv', mode='r') as new_reader:
                    xizmat_nomi = 'Просмотр авиабилетов на сайте Uzbekistan Airways'
                    csv_reader = csv.DictReader(new_reader, delimiter=',')
                    for rows in csv_reader:
                        if rows['Xizmat nomi - ru'] == xizmat_nomi:
                            detail_info = rows['Muxlisa text - RU']
                            link_ru = rows['Link ru']
                            dispatcher.utter_message(f"Название услуга: {xizmat_nomi} \n"
                                                     f"{detail_info}")
                            dispatcher.utter_message(f"Подробнее об услуге вы можете узнать по ссылке:"
                                                     f" <a href='{link_ru}'>{link_ru}</a>")

                            redis_client = redis.StrictRedis(host='localhost', port=6379, db=0)

                            redis_client.set(f"{intent_name}", xizmat_nomi)
                            redis_client.set(f"{intent_name}_description", detail_info)
        else:
            dispatcher.utter_message("Простите, я не могу ответит на ваш вопрос")

        return []


class ActionObtainingCertificateOfReturnToUzbRu(Action):  # 5
    def name(self) -> Text:
        return "action_obtaining_certificate_of_return_to_UZB_ru"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        user_message = tracker.latest_message['text']

        with open("../data/nlu_ru.yml", "r") as file:
            nlu_data = yaml.safe_load(file)

        intent_name = "obtaining_certificate_of_return_to_UZB_ru"
        if intent_name in nlu_data['nlu'][5]['intent']:
            intent_example = nlu_data['nlu'][5]['examples']
            if user_message in intent_example:
                with open("../Muxlisa - Лист1.csv", "r") as new_reader:
                    xizmat_nomi = "Получение свидетельство на возвращение в Республику Узбекистан"
                    csv_reader = csv.DictReader(new_reader, delimiter=',')
                    for rows in csv_reader:
                        if rows['Xizmat nomi - ru'] == xizmat_nomi:
                            detail_info = rows['Muxlisa text - RU']
                            link_ru = rows['Link ru']
                            dispatcher.utter_message(f"Название услуга: {xizmat_nomi} \n"
                                                     f"{detail_info}")
                            dispatcher.utter_message(f"Подробнее об услуге вы можете узнать по ссылке:"
                                                     f" <a href='{link_ru}'>{link_ru}</a>")

                            redis_client = redis.StrictRedis(host='localhost', port=6379, db=0)

                            redis_client.set(f"{intent_name}", xizmat_nomi)
                            redis_client.set(f"{intent_name}_description", detail_info)
        else:
            dispatcher.utter_message("Простите, я не могу ответит на ваш вопрос")

        return []


class ActionCertificationOfApplicantsForJudicialManagersRu(Action):  # 6
    def name(self) -> Text:
        return "action_certification_of_applicants_for_judicial_managers_ru"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        user_message = tracker.latest_message['text']

        with open("../data/nlu_ru.yml", "r") as file:
            nlu_data = yaml.safe_load(file)

        intent_name = "certification_of_applicants_for_judicial_managers_ru"
        if intent_name in nlu_data['nlu'][6]['intent']:
            intent_example = nlu_data['nlu'][6]['examples']
            if user_message in intent_example:
                with open("../Muxlisa - Лист1.csv", "r") as new_reader:
                    xizmat_nomi = ("Аттестация (переаттестация) претендентов на судебных управляющих и выдача"
                                   " им квалификационного аттестата")
                    csv_reader = csv.DictReader(new_reader, delimiter=',')
                    for rows in csv_reader:
                        if rows['Xizmat nomi - ru'] == xizmat_nomi:
                            detail_info = rows['Muxlisa text - RU']
                            link_ru = rows['Link ru']
                            dispatcher.utter_message(f"Название услуга: {xizmat_nomi} \n"
                                                     f"{detail_info}")
                            dispatcher.utter_message(f"Подробнее об услуге вы можете узнать по ссылке:"
                                                     f" <a href='{link_ru}'>{link_ru}</a>")

                            redis_client = redis.StrictRedis(host='localhost', port=6379, db=0)

                            redis_client.set(f"{intent_name}", xizmat_nomi)
                            redis_client.set(f"{intent_name}_description", detail_info)
        else:
            dispatcher.utter_message("Простите, я не могу ответит на ваш вопрос")

        return []


class ActionRegistrationOfPermanentResidenceAbroadRu(Action):  # 7
    def name(self) -> Text:
        return "action_registration_of_permanent_residence_abroad_ru"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        user_message = tracker.latest_message['text']

        with open("../data/nlu_ru.yml", "r") as file:
            nlu_data = yaml.safe_load(file)

        intent_name = "registration_of_permanent_residence_abroad_ru"
        if intent_name in nlu_data['nlu'][7]['intent']:
            intent_example = nlu_data['nlu'][7]['examples']
            if user_message in intent_example:
                with open("../Muxlisa - Лист1.csv", "r") as new_reader:
                    xizmat_nomi = "Оформление документов на постоянное местожительства за рубежом"
                    csv_reader = csv.DictReader(new_reader, delimiter=',')
                    for rows in csv_reader:
                        if rows['Xizmat nomi - ru'] == xizmat_nomi:
                            detail_info = rows['Muxlisa text - RU']
                            link_ru = rows['Link ru']
                            dispatcher.utter_message(f"Название услуга: {xizmat_nomi} \n"
                                                     f"{detail_info}")
                            dispatcher.utter_message(f"Подробнее об услуге вы можете узнать по ссылке:"
                                                     f" <a href='{link_ru}'>{link_ru}</a>")

                            redis_client = redis.StrictRedis(host='localhost', port=6379, db=0)

                            redis_client.set(f"{intent_name}", xizmat_nomi)
                            redis_client.set(f"{intent_name}_description", detail_info)
        else:
            dispatcher.utter_message("Простите, я не могу ответит на ваш вопрос")

        return []


class ActionApplicantTestResultRu(Action):  # 8
    def name(self) -> Text:
        return "action_applicant_test_result_ru"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        user_message = tracker.latest_message['text']

        with open("../data/nlu_ru.yml", "r") as file:
            nlu_data = yaml.safe_load(file)

        intent_name = "applicant_test_result_ru"
        if intent_name in nlu_data['nlu'][8]['intent']:
            intent_example = nlu_data['nlu'][8]['examples']
            if user_message in intent_example:
                with open("../Muxlisa - Лист1.csv", "r") as new_reader:
                    xizmat_nomi = "Ознакомление с результатом тестовых испытаний абитуриента"
                    csv_reader = csv.DictReader(new_reader, delimiter=',')
                    for rows in csv_reader:
                        if rows['Xizmat nomi - ru'] == xizmat_nomi:
                            detail_info = rows['Muxlisa text - RU']
                            link_ru = rows['Link ru']
                            dispatcher.utter_message(f"Название услуга: {xizmat_nomi} \n"
                                                     f"{detail_info}")
                            dispatcher.utter_message(f"Подробнее об услуге вы можете узнать по ссылке:"
                                                     f" <a href='{link_ru}'>{link_ru}</a>")

                            redis_client = redis.StrictRedis(host='localhost', port=6379, db=0)

                            redis_client.set(f"{intent_name}", xizmat_nomi)
                            redis_client.set(f"{intent_name}_description", detail_info)
        else:
            dispatcher.utter_message("Простите, я не могу ответит на ваш вопрос")

        return []


class ActionSubmitApplicationForTractorDriverExamRu(Action):  # 9
    def name(self) -> Text:
        return "action_submit_application_for_tractor_driver_exam_ru"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        user_message = tracker.latest_message['text']

        with open("../data/nlu_ru.yml", "r") as file:
            nlu_data = yaml.safe_load(file)

        intent_name = "submit_application_for_tractor_driver_exam_ru"
        if intent_name in nlu_data['nlu'][9]['intent']:
            intent_example = nlu_data['nlu'][9]['examples']
            if user_message in intent_example:
                with open("../Muxlisa - Лист1.csv", "r") as new_reader:
                    xizmat_nomi = ("Подача заявление на сдачу экзамена на получение водительского удостоверения"
                                   " тракториста")
                    csv_reader = csv.DictReader(new_reader, delimiter=',')
                    for rows in csv_reader:
                        if rows['Xizmat nomi - ru'] == xizmat_nomi:
                            detail_info = rows['Muxlisa text - RU']
                            link_ru = rows['Link ru']
                            dispatcher.utter_message(f"Название услуга: {xizmat_nomi} \n"
                                                     f"{detail_info}")
                            dispatcher.utter_message(f"Подробнее об услуге вы можете узнать по ссылке:"
                                                     f" <a href='{link_ru}'>{link_ru}</a>")

                            redis_client = redis.StrictRedis(host='localhost', port=6379, db=0)

                            redis_client.set(f"{intent_name}", xizmat_nomi)
                            redis_client.set(f"{intent_name}_description", detail_info)
        else:
            dispatcher.utter_message("Простите, я не могу ответит на ваш вопрос")

        return []


class ActionReplacingTractorDriversLicenseRu(Action):  # 10
    def name(self) -> Text:
        return "action_replacing_tractor_drivers_license_ru"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        user_message = tracker.latest_message['text']

        with open("../data/nlu_ru.yml", "r") as file:
            nlu_data = yaml.safe_load(file)

        intent_name = "replacing_tractor_drivers_license_ru"
        if intent_name in nlu_data['nlu'][10]['intent']:
            intent_example = nlu_data['nlu'][10]['examples']
            if user_message in intent_example:
                with open("../Muxlisa - Лист1.csv", "r") as new_reader:
                    xizmat_nomi = ("Подача заявление на замену удостоверения тракториста или получение нового"
                                   " взамен утерянного")
                    csv_reader = csv.DictReader(new_reader, delimiter=',')
                    for rows in csv_reader:
                        if rows['Xizmat nomi - ru'] == xizmat_nomi:
                            detail_info = rows['Muxlisa text - RU']
                            link_ru = rows['Link ru']
                            dispatcher.utter_message(f"Название услуга: {xizmat_nomi} \n"
                                                     f"{detail_info}")
                            dispatcher.utter_message(f"Подробнее об услуге вы можете узнать по ссылке:"
                                                     f" <a href='{link_ru}'>{link_ru}</a>")

                            redis_client = redis.StrictRedis(host='localhost', port=6379, db=0)

                            redis_client.set(f"{intent_name}", xizmat_nomi)
                            redis_client.set(f"{intent_name}_description", detail_info)
        else:
            dispatcher.utter_message("Простите, я не могу ответит на ваш вопрос")

        return []


class ActionDripIrrigationInfoRu(Action):  # 11
    def name(self) -> Text:
        return "action_drip_irrigation_info_ru"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        user_message = tracker.latest_message['text']

        with open('../data/nlu_ru.yml', 'r') as file:
            nlu_data = yaml.safe_load(file)

        intent_name = "calculate_drip_irrigation_ru"
        if intent_name in nlu_data['nlu'][11]['intent']:
            intent_examples = nlu_data['nlu'][11]['examples']
            if user_message in intent_examples:
                with open("../Muxlisa - Лист1.csv", mode='r') as file_reader:
                    csv_reader = csv.DictReader(file_reader, delimiter=',')
                    xizmat_nomi = 'Калькулятор капельного орошения'
                    for rows in csv_reader:
                        if rows['Xizmat nomi - ru'] == xizmat_nomi:
                            detail_info = rows['Muxlisa text - RU']
                            link_ru = rows['Link ru']
                            dispatcher.utter_message(f"Название услуга: {xizmat_nomi} \n"
                                                     f"{detail_info}")
                            dispatcher.utter_message(f"Подробнее об услуге вы можете узнать по ссылке:"
                                                     f" <a href='{link_ru}'>{link_ru}</a>")

                            redis_client = redis.StrictRedis(host='localhost', port=6379, db=0)

                            redis_client.set(f"{intent_name}", xizmat_nomi)
                            redis_client.set(f"{intent_name}_description", detail_info)

                            redis_client.close()
                            print(f'service_name saved: {xizmat_nomi}\n'
                                  f'service_description saved: {detail_info}')
        else:
            dispatcher.utter_message(text='Простите, я не могу ответит на ваш вопрос')

        return []
