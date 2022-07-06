from concurrent import futures
import time
import grpc
import sys
import subprocess

sys.path.append("/usr/app/grpc_compiled")
import main_pb2
import main_pb2_grpc

def greet(name):
	return f"Good Morning, {name}"

def executeFunction(functionName, parameter):
	return eval(f"{functionName}(\"{parameter}\")")

def installPackage(packageLst):
	try:
		for ele in packageLst:
			subprocess.check_call([sys.executable, "-m", "pip", "install", ele])
	except:
		return 1
	return 0


class Service(main_pb2_grpc.MainServiceServicer):
	def ExecFunction(self, request, context):
		print("Recived ExecFucntion Job!")
		replyMessage = executeFunction(request.functionName, request.name)
		return main_pb2.functionResult(reply=replyMessage)
	def InstallPackage(self, request, context):
		print("Recieved package install Job!")
		replyMessage = installPackage(request.packageList)
		return main_pb2.packageStatus(packageCode=int(replyMessage))

def serve():
	server = grpc.server(futures.ThreadPoolExecutor(max_workers=4))
	main_pb2_grpc.add_MainServiceServicer_to_server(Service(), server)
	server.add_insecure_port('[::]:8080')
	server.start()
	print("Server started. Awaiting jobs.. ")
	try:
		while True:
			time.sleep(60*60*24)
	except KeyboardInterrupt:
		server.stop(0)

if __name__ == '__main__':
	serve()