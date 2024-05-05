class ChecarCpf:
	def __init__(self,cpf):
		self.cpf = str(cpf)
		
	def tratamento(self):
		self.cpf = [x for x in self.cpf if x.isnumeric()]
		if len(self.cpf)==11:
		    return True
		elif len(self.cpf)>11:
		    self.cpf[:11]
		    return True
		else:
		    return False
		    
	def calculo(self):
	    self.primeiros = self.cpf[:9]
	    self.verificadores = self.cpf[9:]
	    for k in range(2):
	        if k == 0:
	        	self.mult = list(range(10,1,-1))
	        if k == 1:
	        	self.mult = list(range(11,1,-1))
	        soma = 0
	        for i,num in enumerate(self.primeiros):
	            soma += int(num)*self.mult[i]
	        resto = soma % 11
	        if resto == 0 or resto ==1:
	            final = 0 
	        else:
	            final = 11 - resto
	        if final == int(self.verificadores[k]):
	            self.primeiros.append(self.verificadores[k])
	            if k==1:
	                self.primeiros.insert(3,".")
	                self.primeiros.insert(7,".")
	                self.primeiros.insert(11,"-")
	                self.cpf = ''.join(self.primeiros)
	                return True
	        else:
	            return False