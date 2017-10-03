import rpyc







proxy = rpyc.connect('localhost', 8001) # connection function to connect to server by creation of an object
#print(trapezoidal(lambda x:x**2,5,10,100))
answer = proxy.root.trapezoidal(lambda x:x**2,5,10,100)
print(answer)
# calls the proxy object which calls the root.compute function
#root accesses the rpyc service class created in the server script and compute is the function in the server class
# compute function had a prefix keyword exposed so that it can be availed to the client from the server side

