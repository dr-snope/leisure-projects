import mysql.connector
import msvcrt
import sys

def get_masked_input(prompt="Enter Password: ", mask="*") -> str:
    print(prompt, end="", flush=True)
    password = []

    while True:
        char = msvcrt.getch()

        if char in (b"\r", b"\n"):
            print()
            break
        elif char == b"\x08":
            if password:
                password.pop()
                sys.stdout.write("\b \b")
                sys.stdout.flush()

        elif char == b"\x03":
            raise KeyboardInterrupt

        elif char in (b"\x00", b"\xe0"):
            msvcrt.getch()

        else:
            try:
                decoded = char.decode("utf-8")
                password.append(decoded)
                sys.stdout.write(mask)
                sys.stdout.flush()
            except UnicodeDecodeError:
                pass

    return "".join(password)

def connect(func_password, func_database=None, func_host='localhost', func_user='root'):

    func_database = func_database or None
    func_host = func_host or 'localhost'
    func_user = func_user or 'root'

    try:
        connection = mysql.connector.connect(
            host = func_host,
            user = func_user,
            password = func_password,
            database = func_database
        )
        return connection
    except mysql.connector.Error as err:
        print('-------------------------------------------------------------------------')
        print(f"Connection failed: {err}")
        print('-------------------------------------------------------------------------')
        return None
    
def show_databases(connection):
    if not (connection and connection.is_connected()):
        print('-------------------------------------------------------------------------')
        print("                  Database connection is not active.")
        print('-------------------------------------------------------------------------')
        return None
    
    cursor = connection.cursor()
    try:
        cursor.execute('SHOW DATABASES')
        record = cursor.fetchall()
        
        for key, data in enumerate(record):
            print(f'{key+1}: {list(data)[0]}')
        
    except mysql.connector.Error as err:
        connection.rollback()
        print('-------------------------------------------------------------------------')
        print(f'Error: {err}')
        print('-------------------------------------------------------------------------')
        return None
    finally:
        cursor.close()
    

def change_database(connection, dbname):
    if not (connection and connection.is_connected()):
        print('-------------------------------------------------------------------------')
        print("                  Database connection is not active.")
        print('-------------------------------------------------------------------------')
        return None
    
    cursor = connection.cursor()
    try:
        cursor.execute(f'USE {dbname}')
        print('-------------------------------------------------------------------------')
        print('                          Database Changed')
        print('-------------------------------------------------------------------------')
    
    except mysql.connector.Error as err:
        connection.rollback()
        print('-------------------------------------------------------------------------')
        print(f'Error: {err}')
        print('-------------------------------------------------------------------------')
    finally:
        cursor.close()
    

def show_tables(connection):
    if not connection or not connection.is_connected():
        print('-------------------------------------------------------------------------')
        print("                  Database connection is not active.")
        print('-------------------------------------------------------------------------')
        return None
    
    cursor = connection.cursor()
    try:
        cursor.execute('SHOW TABLES')
        tables = cursor.fetchall()
        print('-----------------------------ALL TABLES----------------------------------')
        for (table,) in tables:
            print(table)
        print('-------------------------------------------------------------------------')
    except mysql.connector.Error as err:
        connection.rollback()
        print('-------------------------------------------------------------------------')
        print(f"Query error: {err}")
        print('-------------------------------------------------------------------------')
        return None
    finally:
        cursor.close()
    

def run_query(connection, query):
    if not connection or not connection.is_connected():
        print('-------------------------------------------------------------------------')
        print("                  Database connection is not active.")
        print('-------------------------------------------------------------------------')
        return None

    cursor = connection.cursor()
    try:
        cursor.execute(query)
        if cursor.with_rows:
            records = cursor.fetchall()
            print('---------------------------------DATA------------------------------------')
            for row in records:
                print(row)
        else:
            connection.commit()
        print('-------------------------------------------------------------------------')
        print('                          Query Executed!')
        print('-------------------------------------------------------------------------')
    except mysql.connector.Error as err:
        connection.rollback()
        print('-------------------------------------------------------------------------')
        print(f"Query error: {err}")
        print('-------------------------------------------------------------------------')
        return None
    finally:
        cursor.close()
    

print('-------------------------------------------------------------------------')
print('                    Python-MySQL-Connectivity Program                    ')
print('-------------------------------------------------------------------------')

while True:
    password = get_masked_input("Enter Password: ")
    host = input('Enter Host(Blank for default): ').strip()
    user = input('Enter Username(Blank for default): ').strip()
    db = input('Enter Database(Blank to select later): ').strip()
    db_conn = connect(password, db, host, user)
    if db_conn and db_conn.is_connected():
        print('-------------------------------------------------------------------------')
        print("                       Connection Successful!")
        print('-------------------------------------------------------------------------')
        break
    else:
        print('                         Please try again')
        print('-------------------------------------------------------------------------')

while True:
    print('                                Menu                                     ')
    print('-------------------------------------------------------------------------')
    print('1)  Database Selector')
    print('2)  Table Displayer')
    print('3)  Query Executor')
    print('4)  Quit')

    
    try:
        choice = int(input('Enter Your Choice: '))
    except ValueError:
        print('-------------------------------------------------------------------------')
        print("Please enter a valid number from the menu")
        print('-------------------------------------------------------------------------')
        continue

    match choice:
        case 1:
            show_databases(db_conn)
            db = input('Enter Database name: ')
            change_database(db_conn, db)
        case 2:
            show_tables(db_conn)
        case 3:
            query = input('Enter query: ')
            run_query(db_conn, query)
        case 4:
            confirm = input('Are you sure you want to quit?(Y/N): ')
            if confirm.lower().strip() == 'y':
                db_conn.close()
                print('-------------------------------------------------------------------------')
                print('                               Goodbye!')
                print('-------------------------------------------------------------------------')
                print('                    Python-MySQL-Connectivity Program                    ')
                print('-------------------------------------------------------------------------')
                break
            else:
                print('-------------------------------------------------------------------------')
        case _:
            print('Invalid Choice')
