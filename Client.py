import socket
import sys


ip = 'localhost'
port = 5555
try:
	ip = str(sys.argv[1])
	port = int(sys.argv[2])
except IndexError:
	pass


class Client:
	def __init__(self, address=(ip, port)):
		client = socket.socket()
		client.connect(address)
		print(f'[*] Connected to {address}.\n')
		self.client = client
		Client.main(self)	
	
	def main(self):	
		file_list = self.client.recv(1024)	
		print(file_list.decode())

		if file_list.decode() == 'No files available on this server.':
			return

		while True:
			try:
				request = input('\n>')
			except KeyboardInterrupt:
				break
			if request == '' or request == ' ':
				continue
			self.client.send(request.encode())
			Client._Receive_file(self)

	def _Receive_file(self):
		F_naze = self.client.recv(1024).decode()
		if F_naze[0:7] == '[error]':
			print(F_naze)
			return 
		F_name = F_naze.split()[0]
		F_size = F_naze.split()[1]
		#################
		#Sometimes in receiving file_size some bytes were receive.
		#below code is to fix that.
		RB = False
		try:
			F_naze = int(F_size)
		except:
			for n, i in emumerate(F_size):
				try:
					i = int(i)
				except:
					RB = True
					byte = F_size[n:].encode()
					F_size = int(F_size[:n]) - (n+1)
					break
		###################

		with open(F_name, 'wb') as FILE:
			if RB:
				FILE.write(byte.encode())
			Client.Receive_file(self, FILE, F_size)
		FILE.close()

	def Receive_file(self, file, buffer):
		times = (int(buffer) // 4096) + 1
		recv_buffer = 0
		if times == 1:
			data = self.client.recv(int(buffer))
			file.write(data)
			recv_buffer += len(data)
		else:
			for i in range(times):
				data = self.client.recv(4096)
				file.write(data)
				recv_buffer += len(data)
		if recv_buffer == int(buffer):
			return 
		else:
			return Client.Receive_file(self, file, int(buffer) - recv_buffer)


Client()
