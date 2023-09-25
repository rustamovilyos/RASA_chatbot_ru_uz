import psycopg2
import yaml


def DataUpdate():
    """
    Pushes Descriptive Analytics Data to the Database
    """
    db = psycopg2.connect(
        host="localhost",
        database="rasadb",
        user="rasauser",
        password="rasapass"
    )

    my_cursor = db.cursor()

    # Открываем и читаем файл nlu.yml
    with open("data/nlu.yml", "r") as nlu_file:
        nlu_data = yaml.safe_load(nlu_file)

    # Получаем данные из nlu_data и вставляем их в базу данных
    for item in nlu_data["nlu"]:
        if "intent" in item and "examples" in item:
            intent = item["intent"]
            examples = item["examples"]

            # Проверяем существование таблицы rasainfo
            my_cursor.execute("SELECT EXISTS (SELECT 1 FROM information_schema.tables WHERE table_name = 'rasainfo')")
            table_exists = my_cursor.fetchone()[0]

            if not table_exists:
                # Если таблица не существует, создаем ее
                my_cursor.execute("""
                        CREATE TABLE rasainfo (
                            service_name TEXT,
                            service_description TEXT
                        )
                    """)
                db.commit()
                print("Table 'rasainfo' created successfully.")

            postgres_insert_query = """
                    INSERT INTO rasainfo(service_name, service_description)
                    VALUES (%s, %s);
                """

            my_cursor.execute(postgres_insert_query, (intent, examples))
            db.commit()

            print("Record inserted successfully into table")

    db.close()


DataUpdate()
