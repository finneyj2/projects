import numpy as np
import sqlite3

def makeConnection(sqlite_file):
    #driver to open the database and return the connection.
	#define the database filename
    print(" database file: " + sqlite_file)
	# define the conn, or the database object
    conn = sqlite3.connect(sqlite_file)
        # load the file
    return(conn)
    # send the database connection to the rest of the program.
    # end of make connection()

def runQuery(query_str, conn):
    # Method to perform the query; the query string and conn are be passed into this function.
    result = conn.execute(query_str)
    return result.fetchall()


sqlite_file = "salary.sqlite3"
conn = makeConnection(sqlite_file)

table = "colSalary"
table2 = "degSalary"
table3 = "regSalary"
Dvar = "Undergraduate_Major"
Cvar1 = "School_Name"
Cvar2 = "School_Type"
Cvar3 = "deptName"
Cvar4 = "Starting_Median_Salary"
Cvar5 = "Mid_Career_Median_Salary"
Cvar6 = "Mid_Career_10th_Percentile_Salary"
Cvar7 = "Mid_Career_90th_Percentile_Salary"

QueryStr = "select " + Cvar1 + "," + Cvar2 + " from " + table
result = runQuery(QueryStr, conn)

def runStatsMean():
    MoneyStr = "select " + Cvar4 + " from " + table2
    total = conn.execute(QueryStr)
    all = total.fetchall()
    # apply the command to the database
    totalM = conn.execute(MoneyStr)
    allM = totalM.fetchall()
    practice = np.array(allM)
    R = []
    for x in practice[1:]:
        x = str(x[0])
        x = x.replace("$", "")
        x = x.replace(",", "")
        R.append(float(x))

    aveM = np.mean(R)
    print(aveM)

def runStatsMean10():
    MoneyStr = "select " + Cvar6 + " from " + table2
    total = conn.execute(QueryStr)
    all = total.fetchall()
    # apply the command to the database
    totalM = conn.execute(MoneyStr)
    allM = totalM.fetchall()
    practice = np.array(allM)
    R = []
    for x in practice[1:]:
        x = str(x[0])
        x = x.replace("$", "")
        x = x.replace(",", "")
        R.append(float(x))

    aveM = np.mean(R)
    print(aveM)
    return aveM

def runStatsMeanMid():
    MoneyStr = "select " + Cvar5 + " from " + table2
    total = conn.execute(QueryStr)
    all = total.fetchall()
    # apply the command to the database
    totalM = conn.execute(MoneyStr)
    allM = totalM.fetchall()
    practice = np.array(allM)
    R = []
    for x in practice[1:]:
        x = str(x[0])
        x = x.replace("$", "")
        x = x.replace(",", "")
        R.append(float(x))

    aveM = np.mean(R)
    print(aveM)

def runStatsMean90():
    MoneyStr = "select " + Cvar7 + " from " + table2
    total = conn.execute(QueryStr)
    all = total.fetchall()
    # apply the command to the database
    totalM = conn.execute(MoneyStr)
    allM = totalM.fetchall()
    practice = np.array(allM)
    R = []
    for x in practice[1:]:
        x = str(x[0])
        x = x.replace("$", "")
        x = x.replace(",", "")
        R.append(float(x))

    aveM = np.mean(R)
    print(aveM)

def statsStd():
    MoneyStr = "select " + Cvar4 + " from " + table
    total = conn.execute(QueryStr)
    all = total.fetchall()
    # apply the command to the database
    totalM = conn.execute(MoneyStr)
    allM = totalM.fetchall()
    practice = np.array(allM)
    R = []
    for x in practice[1:]:
        x = str(x[0])
        x = x.replace("$", "")
        x = x.replace(",", "")
        R.append(float(x))

    med = np.std(R)
    print(med)

if __name__ == '__main__':
    runStatsMean()
    runStatsMean10()
    runStatsMeanMid()
    runStatsMean90()
    statsStd()
#for i in result:
    #print(" " + '{0}'.format(i))
