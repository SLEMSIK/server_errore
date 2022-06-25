import pyfiglet
import time
def system():


  print(pyfiglet.figlet_format("VYACHESLAV system")) 

  time.sleep(3)

  info = input("К сожалению произошла ошибка доступа к зашифрованному каналу связи VYACHESLAV SYSTEM!\n") 

  if info == "server.get_data":

    print(pyfiglet.figlet_format("SERVER DATA")) 

    print("Статус сервера - 200") 

    time.sleep(3)

    print("Зашифрованный канал - OK")

    time.sleep(2)

    print("Заблокированых каналов - 1")

    time.sleep(5)

    print("Не определённых каналов - 649")

    time.sleep(3)

    print("Помех для каналов - 17")
    data1 = input("restart system\n") 

      if data1 == "yes":
        system()
  

  if info == "server.channel_restart":

    time.sleep(10)

    print("Каналы успешно обновлены")

    data1 = input("restart system\n") 

    if data1 == "yes":
    

       print(pyfiglet.figlet_format("VYACHESLAV system")) 

        time.sleep(2)

        input("Доступ к системе успешно установлен!\n") 

              

             
              
              
              

