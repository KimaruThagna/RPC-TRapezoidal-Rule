import rpyc
from rpyc.utils.server import ThreadedServer






class MyService(rpyc.Service):
	def exposed_trapezoidal(self,f, a, b, n):
		
		h = float(b - a) / n
		s = 0.0
		s += f(a)/2.0
		for i in range(1, n):
			s += f(a + i*h)
		s += f(b)/2.0
		return s * h


t = ThreadedServer(MyService, port = 8001)# handles each request using a new thread as opposed to handling requests with a new process
t.start()