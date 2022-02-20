def f1():
    try:
        flight_file=open("flights.txt","r")
        text=flight_file.read()
        print(text)
        flight_file.close()
        flight_file=open("flights.txt","a")
        flight_file.write("\n whatup broooo")
        flight_file.close()
    except Exception as e:
        print(e,"Error occurred")
        if flight_file.closed:
            print("File is closed")
        else:
            print("File is open")


def f2():
    try:
        fi1=open("newFile.txt", "w+")
        fi1.write("""Need more time?
        Change your due dates and pick up where you left off in a new session.""")
        print("file created")
    except Exception as e:
        print(e)
    finally:
        fi1.close()
        print('file closed')
        
f2()