# get_data.py
import mysql.connector
import json
from datetime import datetime, timedelta, timezone
import configparser
import logging

# Configure logging
logging.basicConfig(filename='app.log', level=logging.INFO,
                    format='%(asctime)s - %(levelname)s - %(message)s')

def get_failed_snapshot_requests():
    config = configparser.ConfigParser()
    config.read('config.ini')

    db_config = config['database']
    username = db_config['username']
    password = db_config['password']
    host = db_config['host']
    port = int(db_config['port'])
    database = db_config['database']

    # Dynamic start and end datetimes (with timezone)
    end_time = datetime.now(timezone.utc)  # Current time in UTC
    duration = timedelta(days=1)  # Example: 1 day duration
    start_time = end_time - duration

    try:
        mydb = mysql.connector.connect(
            user=username,
            password=password,
            host=host,
            port=port,
            database=database
        )

        mycursor = mydb.cursor(dictionary=True)

    
        formatted_start_time = start_time.strftime('%Y-%m-%d %H:%M') # MySQL datetime format
        formatted_end_time = end_time.strftime('%Y-%m-%d %H:%M')


        query = f"""
        SELECT * 
        FROM alice_db.SNAPSHOT_OFFLINE_REQUEST sor 
        WHERE UPDATED_DATE BETWEEN '{start_time}' AND '{end_time}'
        AND STATUS = 'COMPLETED';
        """

        mycursor.execute(query)

        results = mycursor.fetchall()

        if not results:
            log_message = f"No failed snapshot requests found between {formatted_start_time} and {formatted_start_time}."
            print(log_message)
            logging.info(log_message)
            return
        

        log_message = f"Found {len(results)} failed snapshot requests between {formatted_start_time} and {formatted_end_time}."
        logging.info(log_message)
        for row in results:
            for key, value in row.items():
                if isinstance(value, datetime):
                    row[key] = value.isoformat() 

        json_results = json.dumps(results, indent=2)
        logging.info(json_results)
        logging.info("Successfully retrieved failed snapshot requests.")

    except mysql.connector.Error as err:
        error_message = f"Database error: {err}"
        print(error_message)
        logging.error(error_message)

    except Exception as e:
        error_message = f"An unexpected error occurred: {e}"
        print(error_message)
        logging.exception(error_message)

    finally:
        if mydb and mydb.is_connected():
            mycursor.close()
            mydb.close()

get_failed_snapshot_requests()