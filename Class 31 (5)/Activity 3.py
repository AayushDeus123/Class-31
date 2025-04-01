#Polymorphism
class India:
    def Capital(self):
        print('The capital of India is New Delhi')
    def Language(self):
        print('The national language of India is Hindi')
    def Type(self):
        print('India is a developing country')
        
class USA:
    def Capital(self):
        print('\nThe capital of USA is Washington DC')
    def Language(self):
        print('The national language of USA is English')
    def Type(self):
        print('USA is a developed country')
        
class Japan:
    def Capital(self):
        print('\nThe capital of Japan is Tokyo')
    def Language(self):
        print('The national language of Japan is Japanese')
    def Type(self):
        print('Japan is a developed country')
        
class Malaysia:
    def Capital(self):
        print('\nThe capital of Malaysia is Kuala Lampur')
    def Language(self):
        print('The national language of Malaysia is Malay')
    def Type(self):
        print('Malaysia is a developing country')
        
i = India()
u = USA()
j = Japan()
m = Malaysia()

a = [i,u,j,m]     

for x in a:
    x.Capital()
    x.Language()
    x.Type()