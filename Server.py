import os
import sys
import socket
import threading

ip = 'localhost'
port = 5555

try:
	ip = sys.argv[1]
	port = sys.argv[2]
except IndexError:
	pass


global file_dic
global file_list
file_list = ''
file_dic = {}

os.chdir('Files')
files = os.listdir()
if files != []:
	for index, file in enumerate(files):
		file_list += str(index) + ' ' + file + '\n'

	for i in range(len(files)):
		file_dic[i] = files[i]

	def Get(file):
		DOWN = open(file, 'rb')
		data = DOWN.read()
		DOWN.close()
		return data



class Server:
	def __init__(self, ip=(ip, port)):
		server = socket.socket()
		server.bind(ip)
		server.listen()
		print(f'[*] Server is listening on {ip}.')
		self.server = server
		self.file_dic = file_dic
		self.file_list = file_list
		while True:
			client, addr = server.accept()
			print(f'{addr[0]} : {addr[1]} connected.')
			main = threading.Thread(target=Server.main, args=(self, client, addr))
			main.start()

	def main(self, client, addr):
		if self.file_list == '':
			client.send('No files available on this server.'.encode())
			print(f'{addr[0]} {addr[1]} left the server.')
			return
		client.send(self.file_list.encode())
		while True:
			try:
				request = client.recv(1024).decode()
			########Error Handling#########
			except ConnectionResetError:
				print(f'{addr[0]} {addr[1]} left the server.')
				return
			try:
				if request.split()[0] != 'get':
					client.send(f'[error] Error command ({request.split()[0]}).'.encode())
					continue
			except IndexError:
				print(f'{addr[0]} {addr[1]} left the server.')
				return
			else:
				try:
					index = request.split()[1] #get the index of the file
				except IndexError:
					client.send(f'[error] File not specified.'.encode())
					continue
				try:
					file = self.file_dic[int(index)] #file name that match the index
				except KeyError:
					client.send(f'[error] Unknown Index Number ({index}).'.encode())
					continue
			########Error Handling#########
				Server.SendFile(addr, client, file)

	def SendFile(addr, client, file):
		F_data = Get(file)
		F_size = os.stat(file).st_size
		client.send((file + ' ' + str(F_size)).encode())
		client.send(F_data)
		print(f'{addr[0]} {addr[1]} downloaded {file}.')
		return 


Server()