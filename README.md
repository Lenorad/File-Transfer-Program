# Server
1. Create a file(Files) in the same folder as Server.exe(In Server.exe file name is "Files")
2. In command line type: **Server.exe ip port**
3. If **ip** and **port** is not specified **localhost:5555** is used.  
4. As same as Client where **ip and port is the server where you want to connect**.

# Client
1. Run **Client.exe** you will see a list of files available on the server.  
2. If files not available it exit.
3. To download the file type "**get (index number of file)**" 
4. Example:
  0 hello_world.py  
  get 0

**NOTE**
1. Server must be allowed to communicate through firewall on public.  
2. To do that Control Panel/System and Security/Windows Defender Firewall/Allowed Apps/Change settings and add the application.  
3. Pyinstaller is used to make exe file.
4. Server ip-address is your router ip-address.

Coded by Aung Tay Zar Ko.
