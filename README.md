# Server
create a file(Files) in the same folder as Server.exe(In Server.py file name is "Files")

In command line type: **Server.exe ip port**

If **ip** and **port** is not specified **localhost:5555** is used.  
As same as Client where **ip and port is the server where you want to connect**.

# Client
Run **Client.exe** you will see a list of files available on the server.  
If files not available it exit.

To download the file type "**get (index number of file)**" 

Example:
  0 hello_world.py  
\>get 0

**NOTE**: Server must be allowed to communicate through firewall on public.  
 1. To do that Control Panel/System and Security/Windows Defender Firewall/Allowed Apps/Change settings and add the application.  
 2. Pyinstaller is used to make exe file.

Coded by Aung Tay Zar Ko.
