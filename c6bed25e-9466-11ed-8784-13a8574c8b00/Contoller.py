import sqlite3
import time
try:
    conn = sqlite3.connect("users.db")

    c = conn.cursor()
    tablecheck = []
    ftchal = []
    c.execute("""CREATE TABLE IF NOT EXISTS USERS (perm text, user text)""")
    c.execute("""CREATE TABLE IF NOT EXISTS ADMIN (prefix text, user text)""")
    c.execute("""CREATE TABLE IF NOT EXISTS CHECKLIST (member text, checks text)""")
    #fetchall
    def fetchal(table, get_data=None):
        global ftchal
        if get_data == None:
            print("\n" * 50 + 'Fetching All...')
            c.execute("SELECT * FROM {0}".format(table))
            print(c.fetchall())
        elif get_data != None:
            c.execute("SELECT * FROM {0}".format(table))
            ftchal = c.fetchall()
            return(ftchal)
    #add
    def add_admin(table, user):
        c.execute("INSERT INTO {0} VALUES ('Admin', '{1}')".format(table, user))
        conn.commit()
        print("\n" * 50 + 'User Added!')
    #Update
    def update_table(table, perm, userr, search1, search2):
        print("\n" * 50 + 'Table Updated!')
        if table == 'ADMIN':
            c.execute(f"""UPDATE {table} SET prefix = '{perm}', user = '{userr}' WHERE prefix = '{search1}' AND user = '{search2}'""")
            conn.commit()
            c.execute("SELECT * FROM {0}".format(table))
            t = c.fetchall()
            return(t)
        if table == 'USERS':
            c.execute(f"""UPDATE {table} SET perm = '{perm}', user = '{userr}' WHERE perm = '{search1}' AND user = '{search2}'""")
            conn.commit()
            c.execute("SELECT * FROM {0}".format(table))
            t = c.fetchall()
    timee = 0.75
    def Nuke(table):
        global timee
        global tablecheck
        global ftchal
        fetchal(table, True)
        if ftchal == tablecheck:
            print('Error Table Contents Don\'t Exist')
        else:
            print('Nuking Table Now')
            time.sleep(timee)
            print('Nuking Table Now.')
            time.sleep(timee)
            print('Nuking Table Now..')
            time.sleep(timee)
            print('Nuking Table Now...')
            time.sleep(timee)
            print('Nuking Table Now')
            time.sleep(timee)
            print('Nuking Table Now.')
            time.sleep(timee)
            print('Nuking Table Now..')
            time.sleep(timee)
            c.execute(f"""DELETE FROM {table}""")
            conn.commit()
            print(f'NUKED {table}')
    # ('OWNER', 'Hentai Papa#1931')]
    def whilee():
        while True:
            do_what = input('What Function Would You Like To Call\nupdate_table\nadd_admin\nfetchal\n:').lower()
            if do_what == 'update_table':
                d1 = input('What Table Are You Updating          :')
                d4 = input('What Perm Are You Searching For      :')
                d5 = input('What User Are You Searching For      :')
                d2 = input('What Perm Are You Setting It To      :')
                d3 = input('What User Are You Setting It To      :')
                update_table(d1, d2, d3, d4, d5)
            if do_what == 'add_admin':
                d1 = input('What Table Are You adding a admin to :')
                d2 = input('What User Are Making A Admin         :')
                add_admin(d1, d2)
            if do_what == 'fetchal':
                d1 = input('What Table Are You Fetching          :')
                fetchal(d1)
            if do_what == 'nuke':
                d1244525424524522 = input('what Table:                                            ')
                d2123123123655222 = input('Are you sure you want to do this:                      ').lower()
                d3423342342355777 = input('You Realise this will delete EVERYTHING in This table: ').lower()
                d4132112312313123 = input('This is your LAST chance make a decicision: yes or no: ').lower()
                if d2123123123655222 == 'yes' and d3423342342355777 == 'yes' and d4132112312313123 == 'yes':
                    Nuke(d1244525424524522)
                else:
                    print('\n'*50)
                    print('Thank god you choosed not to nuke it')

    whilee()
except sqlite3.OperationalError:
    print('Error')
    whilee()