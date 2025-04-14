'''
Output MySQL table creator
'''
import mysql.connector


# Налаштування конфігурації SQL бази даних
jdbc_url = "jdbc:mysql://217.61.57.46:3306/olympic_dataset"
# jdbc_table = "athlete_bio"
jdbc_user = "neo_data_admin"
jdbc_password = "Proyahaxuqithab9oplp"

# Підключення до бази даних
db_connection = mysql.connector.connect(
    host="217.61.57.46",
    port=3306,
    user="neo_data_admin",
    password="Proyahaxuqithab9oplp",
    database="olympic_dataset"
)

# Створення курсора для виконання запитів
db_cursor = db_connection.cursor()

# Створення таблиці
sql_query = """
    CREATE TABLE IF NOT EXISTS avg_stats_vvv (
        id INT AUTO_INCREMENT PRIMARY KEY,
        sport VARCHAR(255),
        medal VARCHAR(255),
        sex VARCHAR(255),
        country_noc VARCHAR(255),
        avg_height DOUBLE,
        avg_weight DOUBLE,
        timestamp DATETIME
    );
"""

db_cursor.execute(sql_query)

# Закриття підключення
db_connection.close()