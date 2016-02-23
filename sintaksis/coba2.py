class BujurSangkar():
	def __init__(self,sisi):
		self.sisi= sisi
	
	def hitung_luas(self):
		return self.sisi*self.sisi
		
bs1=BujurSangkar(10)
print (bs1.hitung_luas())