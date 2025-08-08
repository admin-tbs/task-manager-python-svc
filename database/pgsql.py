import psycopg2

connection = psycopg2.connect(
    database="postgres", user="postgres", password="123"
)

# def connect_db():
    # try:
cursor = connection.cursor()
    #     yield cursor
    # except:
    #     print("Error while connectting")
    # finally:
    #     cursor.close()

# read
def read_task():
    # cursor = connect_db()
    select_query = "select * from internship.task_manager;"
    cursor.execute(select_query)
    for row in cursor.fetchall():
        print(row)

# create
def create_task(title, desc, status):
    # cursor = connect_db()
    # cursor = next(cursor)
    query = "INSERT INTO internship.task_manager (title, description, status) VALUES (%s, %s, %s);"
    cursor.execute(query, (title, desc, status))
    connection.commit()

def update_task(task_id, title=None, desc=None, status=None):
    query = "UPDATE internship.task_manager SET"
    if title:
        query += f" title = '{title}',"
    if desc:
        query += f" description = '{desc}',"
    if status:
        query += f" status = '{status}'"
    if task_id:
        query += " where id = %s"
    
    cursor.execute(query, (str(task_id)))
    connection.commit()

def delete_task(task_id):
    query = "DELETE FROM internship.task_manager WHERE id = %s"
    cursor.execute(query, (str(task_id)))
    connection.commit()

create_task("Intership Project", "Task Manager Project", "In Progress")
read_task()
update_task(2,status="Complete")
delete_task(1)

cursor.close()