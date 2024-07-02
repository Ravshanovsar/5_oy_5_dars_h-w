import psycopg2

db_name = 'oy_5_dars_5_homework'
password = 'google_0330'
host = 'localhost'
port = 5432
user = 'postgres'
conn = psycopg2.connect(dbname = db_name,
                        user = user,
                        password = password,
                        host = host,
                        port = port)
cur = conn.cursor()


# create_table_users_query = """create table users(
# id bigserial primary key,
# firstName varchar(250),
# lastName varchar(250),
# age int,
# gender varchar(50),
# phone varchar(250),
# username varchar(250),
# password varchar(250)
# );"""
#
# cur.execute(create_table_users_query)
# conn.commit()


class User():

    def show_users():
        select_from_query = """select * from users"""
        cur.execute(select_from_query)
        conn.commit()

    def show_user():
        user_id = int(input("User ID --> "))
        select_from_query = f"""select * from users where Id = {user_id}"""
        cur.execute(select_from_query)
        conn.commit()

    def delete_user():
        user_id = int(input("User ID --> "))
        delete_query = f"""delete from users where id = {user_id}"""
        cur.execute(delete_query)
        conn.commit()

    def update_user():
        print("1. FirstName")
        print("2. LastName")
        print("3. Age")
        print("4. Gender")
        print("5. Phone")
        print("6. Username")
        print("7. Password")
        ch = int(input(""))
        match ch:
            case 1:
                user_id = int(input("User ID --> "))
                new = input("NEW FirstName --> ")
                update_data_query = f"""UPDATE users
                SET firstName = {new}
                WHERE id = {user_id};"""
                cur.execute(update_data_query)
                conn.commit()
            case 2:
                user_id = int(input("User ID --> "))
                new = input("NEW LastName --> ")
                update_data_query = f"""UPDATE users
                SET lastName = {new}
                WHERE id = {user_id};"""
                cur.execute(update_data_query)
                conn.commit()
            case 3:
                user_id = int(input("User ID --> "))
                new = input("NEW Age --> ")
                update_data_query = f"""UPDATE users
                SET age = {new}
                WHERE id = {user_id};"""
                cur.execute(update_data_query)
                conn.commit()
            case 4:
                user_id = int(input("User ID --> "))
                new = input("NEW Gender --> ")
                update_data_query = f"""UPDATE users
                SET gender = {new}
                WHERE id = {user_id};"""
                cur.execute(update_data_query)
                conn.commit()
            case 5:
                user_id = int(input("User ID --> "))
                new = input("NEW Phone --> ")
                update_data_query = f"""UPDATE users
                SET phone = {new}
                WHERE id = {user_id};"""
                cur.execute(update_data_query)
                conn.commit()
            case 6:
                user_id = int(input("User ID --> "))
                new = input("NEW Username --> ")
                update_data_query = f"""UPDATE users
                SET username = {new}
                WHERE id = {user_id};"""
                cur.execute(update_data_query)
                conn.commit()
            case 7:
                user_id = int(input("User ID --> "))
                new = input("NEW Password --> ")
                update_data_query = f"""UPDATE users
                SET password = {new}
                WHERE id = {user_id};"""
                cur.execute(update_data_query)
                conn.commit()

    def save():
        FirstName = input("first_name --> ")
        LastName = input("lastName --> ")
        Age = input("age --> ")
        Gender = input("gender --> ")
        Phone = input("phone --> ")
        Username = input("username --> ")
        Password = input("password --> ")

        insert_into_query = """insert into users(id, firstName, lastName, age, gender, phone, username, password)
        values (FirstName, LastName, Age, Gender, Phone, Username, Password);"""
        cur.execute(insert_into_query)
        conn.commit()

def main_menu():
    print("1. Show Users")
    print("2. Show User")
    print("3. Delete User")
    print("4. Update User")
    print("5. Save User")
    c = int(input("choose one option -->"))
    match c:
        case 1:
            User.show_users()
        case 2:
            User.show_user()
        case 3:
            User.delete_user()
        case 4:
            User.update_user()
        case 5:
            User.save()




main_menu()