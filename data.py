while True:

    com = input("Write command: ")

    if com == "server.stop":

        print("Fatal error! Please go to server settings and allow access to admin commands (remote.admin_func) ")

    if com == "server.connect":

        print("Error! Please update data files in server settings (get.data_new.data)")

    if com == "server.save":

        print("Error! No access to server files ")

    if com == "server.restart":

        print("Error! No access to server administrative commands")

    if com == "server.ip":

        print("109.201.108.255")
