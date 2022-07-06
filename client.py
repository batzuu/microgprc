import grpc
import sys

sys.path.append("/Users/batzumb/devdev/ni-related/execfunmicro/grpc_compiled")
import main_pb2
import main_pb2_grpc

def run():
	channel = grpc.insecure_channel('localhost:8080')
	stub = main_pb2_grpc.MainServiceStub(channel)
	if (sys.argv[1] == "2"):
		n = int(input('Enter number of packages to install: '))
		lst = []
		for i in range(n):
			ele = input()
			lst.append(ele)
		query = main_pb2.packageData(
			packageList=lst
		)
		response = stub.InstallPackage(query)
		print(response.packageCode)
	elif (sys.argv[1] == "1"):
		fname = sys.argv[2]
		parameter = sys.argv[3]
		query = main_pb2.functionData(
			functionName=fname,
			name=parameter
		)
		response = stub.ExecFunction(query)
		print(response.reply)


if __name__ == "__main__":
	run()
