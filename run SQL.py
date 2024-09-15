import sqlite3
import dynamic_console_functions as dcf

conn = sqlite3.connect('Rock Scalers.db')
curs = conn.cursor()

query = 'sql/delete_customer_record.sql'

with open(query) as sql_select: curs.execute(sql_select.read())

try:
    output = [[]]
    for description in curs.description:
        output[0].append(description[0])
    output.append(curs.description)
    for line in curs:
        output.append(line)
    dcf.print_table(output, has_labels=False)
except:
    pass

conn.commit()
conn.close()